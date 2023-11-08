import pandas as pd
import ast
import re
from collections import Counter
import pickle
from collections import Counter
import pickle
def process_string(s):
    # Check if the string represents a number (integer or decimal)
    if re.match(r'^\d+(\.\d+)?$', s):
        return "[num]"
    else:
        return s.lower()

def process_list(input_list):
    return [process_string(s) for s in input_list]

def conver_to_list(PROJECT_FOLDER, FILE):
    try:
        INTER_FOLDER = PROJECT_FOLDER / 'data' / 'inter'
        FINAL_FOLDER = PROJECT_FOLDER / 'data' / 'final'
        FINAL_FOLDER.mkdir(parents=True, exist_ok=True)
        PICKLE_FOLDER = PROJECT_FOLDER / 'model_store'
        PICKLE_FOLDER.mkdir(parents=True, exist_ok=True)
        PATH_FILE = FINAL_FOLDER/f'{FILE}.csv'
        print(PATH_FILE)
        if(PATH_FILE.exists()):
        FINAL_FOLDER.mkdir(parents=True, exist_ok=True)
        PICKLE_FOLDER = PROJECT_FOLDER / 'model_store'
        PICKLE_FOLDER.mkdir(parents=True, exist_ok=True)
        PATH_FILE = FINAL_FOLDER/f'{FILE}.csv'
        print(PATH_FILE)
        if(PATH_FILE.exists()):
            print("Data already exists")
            return None
        df = pd.read_csv(INTER_FOLDER / f'{FILE}.csv')
        df = pd.read_csv(INTER_FOLDER / f'{FILE}.csv')
        if(df is None):
            raise Exception("data is empty")
        print('started coverting columns data from string to list.')
        df['tokens'] = df['tokens'].apply(ast.literal_eval)
        word_counts = Counter(word for token_list in df['tokens'] for word in token_list)
        df['tokens'] = df['tokens'].apply(ast.literal_eval)
        word_counts = Counter(word for token_list in df['tokens'] for word in token_list)
        print('Completed tokens columns data from string to list.')
        print('Starting tokens num.')
        df['processed_data'] = df['tokens'].apply(process_list)
        df['processed_data'] = df['tokens'].apply(process_list)
        print('Completed tokens num.')
        word_counts = Counter(word for token_list in df['processed_data'] for word in token_list)
        word_to_id = {word: idx for idx, (word, count) in enumerate(word_counts.items(), start=1) if count >= 5}
        if(FILE=='train'):
            pickle_file_path = PICKLE_FOLDER / 'word_to_id.pkl'
            with open(pickle_file_path, 'wb') as f:
                pickle.dump(word_to_id, f)
            print(f"Vocabulary saved to {pickle_file_path}")
        df.to_csv(PATH_FILE, index=False)
        word_counts = Counter(word for token_list in df['processed_data'] for word in token_list)
        word_to_id = {word: idx for idx, (word, count) in enumerate(word_counts.items(), start=1) if count >= 5}
        if(FILE=='train'):
            pickle_file_path = PICKLE_FOLDER / 'word_to_id.pkl'
            with open(pickle_file_path, 'wb') as f:
                pickle.dump(word_to_id, f)
            print(f"Vocabulary saved to {pickle_file_path}")
        df.to_csv(PATH_FILE, index=False)
    except Exception as e:
        print(f"Issues in coverting columns data from string to list. Error: {e}")
        return None
    

    

