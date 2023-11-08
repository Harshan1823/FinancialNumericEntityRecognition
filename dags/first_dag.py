from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta 
import pandas as pd
from pathlib import Path
import sys

root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from dags import PROJECT_FOLDER
from dags.src.data import DATASET_NAME
from dags.src.data.download import download_and_store_data
from dags.src.data.logger_info import setup_logger
from dags.src.data.data_split import split_data
from dags.src.data.pre_process import conver_to_list
# split_data(PROJECT_FOLDER)


logger  = setup_logger(root_dir, 'download_data')

dag_owner = 'Harshan_Ganugula'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 1
        }

dag = DAG(dag_id='first_dag_run',
        default_args=default_args,
        description='This dag loads the data and pre-process data.',
        start_date=datetime(2023,1,1),
        schedule_interval='@daily',
        catchup=False,
        tags=['data', 'pre-processing'])

download_data_dag = PythonOperator(
    task_id = 'download_and_store_data',
    python_callable = download_and_store_data,
    op_kwargs = {'DATASET_NAME': DATASET_NAME, 'logger': logger, 'root_dir': PROJECT_FOLDER},
    dag = dag
)

split_data_dag = PythonOperator(
    task_id = 'split_data',
    python_callable = split_data,
    op_kwargs = {'PROJECT_FOLDER': PROJECT_FOLDER},
    dag = dag
)

convert_train_list_dag = PythonOperator(
    task_id = 'Convert_TRAIN_List',
    python_callable = conver_to_list,
    execution_timeout=timedelta(minutes=10),  # set the timeout to 30 minutes
    op_kwargs = {'PROJECT_FOLDER': PROJECT_FOLDER, "FILE": "train"},
    dag = dag
)


convert_test_list_dag = PythonOperator(
    task_id = 'Convert_TEST_List',
    python_callable = conver_to_list,
    op_kwargs = {'PROJECT_FOLDER': PROJECT_FOLDER, "FILE": "test"},
    dag = dag
)

download_data_dag >> split_data_dag >> [convert_test_list_dag, convert_train_list_dag] # type: ignore