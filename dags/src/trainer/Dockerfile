FROM python:3.9-slim

WORKDIR /

ENV AIP_STORAGE_URI=gs://finer_data_bk/model
ENV BUCKET_NAME=finer_data_bk

COPY trainer /trainer

RUN pip install --no-cache-dir tensorflow gcsfs google-cloud-storage scikit-learn joblib grpcio python-dotenv mlflow numpy

CMD ["python3", "/trainer/gcp_train.py"]