import os
import re
import json
import pickle
import joblib
import shutil
import numpy as np
from pathlib import Path
from google.cloud import storage
import tensorflow as tf
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from tensorflow.keras.preprocessing.sequence import pad_sequences

load_dotenv()

# Now you can use os.getenv to access your environment variables
app = Flask(__name__)

def initialize_variables():
    """
    Initialize environment variables.
    Returns:
        tuple: The project id and bucket name.
    """
    project_id = os.getenv("PROJECT_ID")
    bucket_name = os.getenv("BUCKET_NAME")
    return project_id, bucket_name

def initialize_client_and_bucket(bucket_name):
    """
    Initialize a storage client and get a bucket object.
    Args:
        bucket_name (str): The name of the bucket.
    Returns:
        tuple: The storage client and bucket object.
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    return storage_client, bucket

def load_tokeniser(bucket, pickle_file_path='model_store/tokenizerV1.pkl'):
    """
    Load normalization stats from a blob in the bucket.
    Args:
        bucket (Bucket): The bucket object.
        pickle_file (str): The name of the blob containing the stats.
    Returns:
        dict: The loaded stats.
    """
    print("Pulling Tokenizer from storage")
    local_temp_file = "temp_tokenizer.pkl"

    # Download the pickle file from the bucket
    blob = bucket.blob(pickle_file_path)
    blob.download_to_filename(local_temp_file)

    # Load the pickle file
    with open(local_temp_file, 'rb') as file:
        tokenizer = pickle.load(file)

    # Clean up: Remove the local temporary file after loading
    os.remove(local_temp_file)
    print("Downloaded Tokeniser")
    return tokenizer

def load_model(bucket, bucket_name, models_prefix='model/gcp_'):
    """
    Fetch and load the latest model from the bucket.
    Args:
        bucket (Bucket): The bucket object.
        bucket_name (str): The name of the bucket.
    Returns:
        _BaseEstimator: The loaded model.
    """

    # List all blobs in the models directory and find the latest model
    blobs = list(bucket.list_blobs(prefix=models_prefix))
    model_folders = {}
    for blob in blobs:
        match = re.search(r'gcp_model_(\d+)-(\d+)', blob.name)
        if match:
            print("Match Name: ", blob.name)
            timestamp = int(match.group(1) + match.group(2))  # Concatenate the timestamp
            model_folders[timestamp] = blob.name.split('/')[1]  # Extract folder name

    if not model_folders:
        raise Exception("No model folders found in the specified bucket and prefix.")

    latest_model_folder = model_folders[max(model_folders.keys())]
    print("Latest Model: ", latest_model_folder)
    
    model_dir = f'gs://finer_data_bk/model/{latest_model_folder}/'
    print("Model Directory: ", model_dir)
    model = tf.keras.models.load_model(model_dir)
    print("Loaded Model")
    # Clean up: Remove the local directory after loading the model
    # shutil.rmtree(local_model_dir)

    return model

def process_string(s):
    # Check if the string represents a number (integer or decimal)
    pattern = r'^\d{1,3}(,\d{3})*(\.\d+)?$|^(\d+\.?\d*)$'
    # Check if the string represents a number
    if re.match(pattern, s):
        return "[num]"
    else:
        return s.lower()
    
def process_list(input_list):
    return [process_string(s) for s in input_list]

@app.route(os.environ['AIP_HEALTH_ROUTE'], methods=['GET'])
def health_check():
    """Health check endpoint that returns the status of the server.
    Returns:
        Response: A Flask response with status 200 and "healthy" as the body.
    """
    return {"status": "healthy"}

@app.route(os.environ['AIP_PREDICT_ROUTE'], methods=['POST'])
def predict():
    """
    Prediction route that normalizes input data, and returns model predictions.
    Returns:
        Response: A Flask response containing JSON-formatted predictions.
    """
    request_json = request.get_json()
    request_instances = request_json['instances']
    input = request_instances[0]['text_input'].split()
    np_len = len(input)
    pro_inp = process_list(input)
    tok_inp = tokeniser.texts_to_sequences([pro_inp])
    pad_inp = pad_sequences(tok_inp, maxlen=32, padding='post')
    prediction = model.predict(pad_inp)
    label_prediction = np.argmax(prediction, axis = 2)[0][:np_len].tolist()
    print(label_prediction)
    prediction = {"predictions":label_prediction}
    return jsonify(prediction)
    

project_id, bucket_name = initialize_variables()
print(project_id, bucket_name)
storage_client, bucket = initialize_client_and_bucket(bucket_name)
tokeniser = load_tokeniser(bucket)
model = load_model(bucket, bucket_name)

if __name__ == '__main__':
    print("Started predict.py ")
    app.run(host='0.0.0.0', port=8080)