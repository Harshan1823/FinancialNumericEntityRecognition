from airflow import DAG
from airflow.decorators import task
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta 
import pandas as pd
from pathlib import Path
import sys

root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from src.data.loading_data import load_data
from src.data.download_data import download_and_store_data
dag_owner = 'Harshan_Ganugula'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

dag = DAG(dag_id='first_dag_run',
        default_args=default_args,
        description='This dag loads the data and pre-process data.',
        start_date=datetime(2023,1,1),
        schedule_interval='@daily',
        catchup=False,
        tags=['data', 'pre-processing'])

download_data_dag = PythonOperator(
    task_id = 'download_data',
    python_callable = download_and_store_data,
    dag = dag
)

load_data_dag = PythonOperator(
    task_id = 'load_data',
    python_callable = load_data,
    dag = dag
)

download_data_dag >> load_data_dag