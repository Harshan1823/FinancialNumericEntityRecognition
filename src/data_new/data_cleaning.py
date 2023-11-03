import pandas as pd
import sys
import re
from pathlib import Path
from sklearn.model_selection import train_test_split
import ast
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from src.data import DATA_FOLDER, DESTINATION_FOLDER

FINAL_FOLDER = DATA_FOLDER / 'final'

FINAL_FOLDER.mkdir(parents=True, exist_ok=True)

def merge_data():
    try:
        train_csv = pd.read_csv(DESTINATION_FOLDER / 'train.csv')
        test_csv = pd.read_csv(DESTINATION_FOLDER / 'test.csv')
        valid_csv = pd.read_csv(DESTINATION_FOLDER / 'validation.csv')
        df = pd.concat([train_csv, test_csv, valid_csv], ignore_index=True)
    except Exception as e:
        print(f"Issues in loading raw data files. Error: {e}")
        return None
    
    final_df = df.drop_duplicates(subset=['tokens'])
    print(final_df.head())
    return final_df
    
def preprocess_data():
    try:
        df = merge_data()
        df['tokens'] = df['tokens'].apply(ast.literal_eval)
        df['ner_tags'] = df['ner_tags'].apply(ast.literal_eval)
        return df

    except Exception as e:
        print(f"Issues in coverting columns data from string to list. Error: {e}")
        return None

def process_tokens_column(df):
    df['tokens'] = df['tokens'].apply(process_list)
    return df

def process_list(input_list):
    return [process_string(s) for s in input_list]

def process_string(s):
    # Check if the string represents a number (integer or decimal)
    if re.match(r'^\d+(\.\d+)?$', s):
        return "[num]"
    else:
        return s.lower()

def split_data():
    train_path = FINAL_FOLDER / 'train.csv'
    test_path = FINAL_FOLDER / 'test.csv'

    # Check if the files exist
    if not train_path.exists() and not test_path.exists():
        df = process_tokens_column(preprocess_data())
        train_df, test_df = train_test_split(df, test_size=0.2)
        test_df.to_csv(test_path, index = False)
        train_df.to_csv(train_path, index = False)
    else:
        print("Train and test CSV files already exist. Skipping the processing.")

split_data()