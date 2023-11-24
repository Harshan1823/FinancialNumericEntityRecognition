# Financial Numeric Entity Recognition

FiNER (Financial Numeric Entity Recognition) is a state-of-the-art solution designed to recognize and classify financial numerical entities in text, aiding in the efficient tagging of these entities with XBRL tags. This project aims to automate the tedious process of manual XBRL tagging, ensuring accuracy, consistency, and speed.

Features
1. Automated recognition of financial numerical entities in text.
2. Classification of recognized entities for accurate XBRL tagging.
3. Seamless integration with existing financial systems.
4. Built with the latest advancements in NLP and machine learning.

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

    
