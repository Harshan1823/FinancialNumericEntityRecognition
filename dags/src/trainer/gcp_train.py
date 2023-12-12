import gcsfs
import time
import numpy as np
import pandas as pd
import tensorflow as tf
from datetime import datetime
from model import CustomNERModelV5
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import train_test_split
from google.cloud import storage, logging, bigquery
from google.cloud.bigquery import SchemaField
from google.api_core.exceptions import NotFound
from google.oauth2 import service_account
from google.logging.type import log_severity_pb2 as severity
from tensorflow.keras.preprocessing.sequence import pad_sequences

service_account_file = '/trainer/finerteam8-00bf2670c240.json'
credentials = service_account.Credentials.from_service_account_file(service_account_file)
client = logging.Client(credentials=credentials)
logger = client.logger('Training_pipeline')

def read_json_from_gcs(file_path):
    """
    Reads a JSON file from Google Cloud Storage into a pandas DataFrame.

    :param bucket_name: str, Name of the GCS bucket
    :param file_path: str, Path to the JSON file within the GCS bucket
    :return: DataFrame, The content of the JSON file as a pandas DataFrame
    """
    # Create a GCSFileSystem object
    fs = gcsfs.GCSFileSystem()
    # Construct the full path to the file in GCS
    full_path = file_path
    # Read the file into a pandas DataFrame
    with fs.open(full_path) as f:
        df = pd.read_json(f, lines=True)
    return df

def generate_class_weights():
    train_df = read_json_from_gcs('gs://finer_data_bk/train/train_token.json')
    # Flatten the train_labels
    flattened_labels = np.concatenate(train_df['ner_tags'])
    # Now compute class weights
    class_weights = compute_class_weight('balanced', classes=np.unique(flattened_labels), y=flattened_labels)

    # Convert class weights to a dictionary
    class_weights_dict = {i: weight for i, weight in enumerate(class_weights)}
    return class_weights_dict

def upload_model_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a model to the specified GCS bucket

    :param bucket_name: str, Name of the GCS bucket
    :param source_file_name: str, Local path to the model file
    :param destination_blob_name: str, Desired path in GCS bucket
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"Model {source_file_name} uploaded to {bucket_name}/{destination_blob_name}.")


def pre_process_split_data(pad_len):
    print("Reading the training data from GCS")
    train_df = read_json_from_gcs('gs://finer_data_bk/train/train_token.json')
    train_padded = pad_sequences(train_df['token_data'], maxlen=pad_len, padding='post')
    train_labels = pad_sequences(train_df['ner_tags'], maxlen=pad_len, padding='post')
    train_padded_split, val_padded_split, train_labels_split, val_labels_split = train_test_split(train_padded, train_labels, test_size=0.25, random_state=42)
    return train_padded_split, val_padded_split, train_labels_split, val_labels_split

def train():
   
   hyperparameter_sets = [
    #   {'d_model': 32, 'dff': 512, 'num_heads': 2, 'lstm_units': 64, 'rate': 0.1},
        {'d_model': 64, 'dff': 256, 'num_heads': 4, 'lstm_units': 128, 'rate': 0.2}
        # {'d_model': 128, 'dff': 128, 'num_heads': 6, 'lstm_units': 256, 'rate': 0.3},
        # {'d_model': 256, 'dff': 64, 'num_heads': 8, 'lstm_units': 64, 'rate': 0.4},
        # {'d_model': 32, 'dff': 512, 'num_heads': 10, 'lstm_units': 128, 'rate': 0.5}
    ]
   num_tokens = 23056
   num_tags = 170
   epochs = 3
   pad_len = 32
   class_weights_dict = generate_class_weights()
   train_padded_split, val_padded_split, train_labels_split, val_labels_split = pre_process_split_data(pad_len)
   for i, hparams in enumerate(hyperparameter_sets):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    model_name = f"gcp_model_{timestamp}"
    model = CustomNERModelV5(num_tokens, num_tags, hparams['d_model'], hparams['num_heads'], hparams['dff'], hparams['lstm_units'], hparams['rate'])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])
        
    start_time = time.time()
    history = model.fit(train_padded_split, train_labels_split, 
        epochs=epochs, 
        validation_data=(val_padded_split, val_labels_split), 
        class_weight=class_weights_dict)
    end_time = time.time()

    print(f"Time taken to train: {end_time-start_time} seconds")
    gcs_model_path = f"gs://finer_data_bk/model/{model_name}"
    model.save(gcs_model_path)

if __name__ == "__main__":
    train()