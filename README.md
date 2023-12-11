# Financial Numeric Entity Recognition

print("""
This project, titled "Financial Numeric Entity Recognition," is at the forefront of applying advanced machine learning techniques and MLOps practices to the intricate field of financial data analysis. It aims to automate the way numeric entities in financial documents are identified and processed. By automating the recognition of these entities, the projects engineered to enhance the accuracy and efficiency of financial data processing, thereby addressing a crucial need in the finance sector.   

At the core of this project is a blend of powerful technologies and methodologies:

Python: As the backbone programming language, Python offers a combination of simplicity and power, providing a versatile platform for data manipulation, numerical computations, and machine learning model development. Its rich ecosystem of libraries and frameworks is instrumental in every phase of this project, from data preprocessing to model training and evaluation.

Airflow: Airflow plays a pivotal role in scheduling and orchestrating the workflow of our project. By defining Directed Acyclic Graphs (DAGs), we can meticulously schedule tasks such as data extraction, transformation, loading (ETL), and model training. Each task in our data pipeline is encapsulated as an Airflow operator, ensuring a controlled execution sequence and dependency management. For instance, a DAG in our setup may be designed to first download financial datasets, and perform data cleaning and numeric entity extraction, followed by feeding the processed data into TensorFlow models for NLP tasks.

TensorFlow: As a leading machine learning framework, TensorFlow is utilized for developing and training sophisticated machine learning models. These models are central to the project's objective of recognizing and interpreting financial numeric entities. TensorFlow's advanced capabilities allow for the implementation of deep learning techniques, which are essential in handling the complexities of financial data.

Docker: Docker containers are instrumental in our project for creating isolated environments tailored to specific parts of our workflow, such as data preprocessing, model training, and model inference. This isolation ensures that our application remains consistent across different stages, including development, testing, and production environments. Docker Compose is particularly useful for orchestrating these multi-container setups, effectively managing complex interdependencies within our application, like linking databases, Airflow components, and web servers.

MLflow: MLflow is utilized for managing the machine learning lifecycle, including experimentation, deployment, and auditing. It allows us to systematically track experiments, model training parameters, and results, thereby enabling a comparative analysis of different models and approaches. MLflow is particularly effective in monitoring the performance of our TensorFlow models, assisting us in fine-tuning parameters for optimal results.

Flask: Flask is employed as a lightweight web framework to deploy our TensorFlow models. It facilitates the creation of RESTful APIs, allowing for easy and accessible model inference. Flask’s simplicity and flexibility make it an ideal choice for quickly deploying models and serving predictions over the web.

Vertex AI: Vertex AI is leveraged in our FinancialNumericEntityRecognition project to streamline the deployment and scaling of our machine learning models, especially those developed using TensorFlow. It offers an integrated environment that simplifies the process of training, tuning, and deploying models at scale. We utilize Vertex AI for its advanced ML operations capabilities, which include automated model training (AutoML) and custom model training pipelines. This integration allows us to efficiently manage the lifecycle of our NLP models, from development to production, ensuring seamless and scalable deployment. Furthermore, Vertex AI's robust monitoring and management tools help in maintaining model performance, tracking usage metrics, and updating models as needed, thereby enhancing our ability to deliver accurate and timely financial entity recognition services.

DVC (Data Version Control): DVC is crucial for data and model versioning in our project. It helps in tracking changes in datasets and machine learning models, enabling us to maintain a history of modifications and experimentations. This feature is particularly valuable for reproducing results and rolling back to earlier versions if needed. DVC's seamless integration with cloud storage solutions enhances our capability to handle large datasets and model files efficiently.

GCP: GCP provides the robust and scalable infrastructure necessary for hosting our datasets and machine learning models. It supports our project with extensive data storage options, powerful computing resources, and reliable hosting services, ensuring high availability and performance of our data pipeline and machine learning models.

Each of these tools is carefully selected and integrated to create a robust and efficient platform for financial data analysis. The project stands as a testament to the power of combining cutting-edge technology with best practices in software development and data science, aiming to set new standards in the field of financial analytics.




## Data Card

### Train Dataset (`train.csv`)
- **Size:** 605,040 rows × 3 columns

| Variable Name | Role      | Type   | Description                                           |
|:--------------|:----------|:-------|:------------------------------------------------------|
| id            | ID        | Integer | Unique identifier for each entry.                     |
| tokens        | Feature   | Object  | Tokenized text data, likely sentences or phrases.     |
| ner_tags      | Feature   | Object  | NER tags associated with each token in the `tokens`.  |

### Test Dataset (`test.csv`)
- **Size:** 151,261 rows × 3 columns

| Variable Name | Role      | Type   | Description                                           |
|:--------------|:----------|:-------|:------------------------------------------------------|
| id            | ID        | Integer | Unique identifier for each entry.                     |
| tokens        | Feature   | Object  | Tokenized text data, likely sentences or phrases.     |
| ner_tags      | Feature   | Object  | NER tags associated with each token in the `tokens`.  |

### Overview
The datasets are structured for NLP tasks, specifically for Named Entity Recognition (NER). 
The `tokens` column in both datasets contains strings of tokenized text, which are sentences 
or phrases split into individual words or tokens. The `ner_tags` column appears to have labels 
for each token, used in NER tasks to classify each token into predefined categories like person 
names, organizations, locations, etc. The large size of the training set indicates its potential 
to train robust NLP models, capturing a wide variety of language patterns and nuances related 
to named entities.






## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Docker](https://www.example.com)
- [Airflow](https://www.example.com)
- [ELK](https://www.example.com)
- [DVC](https://www.example.com)
- [GCP](https://www.example.com)

### Installing

A step by step series of examples that tell you how to get a development
environment running

**1. Clone the Repository:**

    git clone https://github.com/Harshan1823/FinancialNumericEntityRecognition.git

**2. Set Up a Virtual Environment (optional but recommended):**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\Activate`
    
**3. Install Dependencies**

    pip install -r requirements.txt
    
**4. Docker:**

    echo -e "AIRFLOW_UID=$(id -u)" > .env
    echo "AIRFLOW_HOME_DIR=$(pwd)" >> .env
    
    docker compose up airflow-init
    docker compose up

**5. DVC**
```
    dvc pull
```

## Data Pipeline Components

The data pipeline in the FinancialNumericEntityRecognition project consists of several interconnected modules, each dedicated to specific tasks within the data processing workflow. Utilizing Airflow and Docker, we orchestrate and containerize these modules, ensuring efficient and modular data processing.

### 1. Downloading Data:
- **download_data.py:** Responsible for downloading the financial dataset from specified sources.
- **unzip_data.py:** Extracts the content from the downloaded zip files for further processing.

### 2. Cleaning Data:
- **tfdata_cleaning.py:** Handles the initial cleaning and formatting of the financial data.
- **pre_process.py:** Further preprocesses the data, focusing on aspects crucial for NLP tasks such as tokenization and normalization.

### 3. Feature Engineering:
- **tokenise_data.py:** This module is crucial for breaking down text into tokens, a fundamental step in NLP.
- **custom_feature_engineering.py:** Tailored for extracting features specific to financial entities and numeric data, enhancing the input for machine learning models.

Each module reads data from an input path, processes it, and outputs the results for subsequent steps. Airflow ensures that these modules function cohesively, maintaining a smooth data processing flow.

## Machine Learning Modeling Pipeline

Our machine learning pipeline is hosted on Google Cloud Platform (GCP) and integrates various tools for robust and scalable model development.

### Pipeline Components:

1. **Trainer:**
   - **train.py:** A Python script that trains the NLP model, focusing on financial entity recognition.
   - **Dockerfile:** Used to containerize the training environment, ensuring consistency across different platforms.

2. **Serve:**
   - **predict.py:** A Flask application for making predictions using the trained model.
   - **Dockerfile:** Ensures that the Flask app is containerized for reliable deployment.

3. **Model Management:**
   - **build.py:** Manages the training and serving pipeline, deploying the model on Vertex AI.

4. **Inference:**
   - **inference.py:** Handles incoming data for model predictions, demonstrating the model's real-world applicability.

### Experimental Tracking with MLflow:

We use MLflow for tracking our experiments, focusing on metrics that are critical for evaluating NLP models in the context of financial data. MLflow's integration allows us to monitor, compare, and optimize model parameters effectively.

### Model Staging and Production:

The models go through stages of development, from initial training to staging and eventually production deployment. We manage these stages using MLflow and Vertex AI, ensuring that our models are robust, efficient, and scalable.
    
