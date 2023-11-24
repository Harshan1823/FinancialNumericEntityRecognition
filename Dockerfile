# Use the official Airflow image as the base image
FROM apache/airflow:2.7.2

# Install additional dependencies
RUN pip install tensorflow numpy pandas scikit-learn datasets

# Copy your project files into the Docker image
COPY . /opt/airflow

# Set the working directory
WORKDIR /opt/airflow

# Specify the user and group that will run the commands inside the container
USER airflow:airflow
