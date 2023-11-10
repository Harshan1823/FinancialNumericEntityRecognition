import pandas as pd
import ast
import re
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

def conver_to_list(PROJECT_FOLDER, FILE, logger):
    
    """
    Convert string data in the 'tokens' column to lists of processed tokens and save as a CSV file.

    This function reads data from a CSV file in the 'data/inter' directory, converts the 'tokens' column from a
    string representation to a list, processes the tokens, and saves the data as a CSV file in the 'data/final' directory.

    :param PROJECT_FOLDER: A Path object representing the project's root directory.
    :param FILE: A string representing the name of the CSV file to be processed.
    """
    
    try:
        INTER_FOLDER = PROJECT_FOLDER / 'data' / 'inter'
        FINAL_FOLDER = PROJECT_FOLDER / 'data' / 'final'
        FINAL_FOLDER.mkdir(parents=True, exist_ok=True)
        PICKLE_FOLDER = PROJECT_FOLDER / 'model_store'
        PICKLE_FOLDER.mkdir(parents=True, exist_ok=True)
        PATH_FILE = FINAL_FOLDER/f'{FILE}.csv'
        if(PATH_FILE.exists()):
            print("Data already exists")
            logger.info("Data already exists")
            return None
        df = pd.read_csv(INTER_FOLDER / f'{FILE}.csv')
        if(df is None):
            raise Exception("data is empty")
        logger.info('Started converting columns data from string to list.')
        df['tokens'] = df['tokens'].apply(ast.literal_eval)
        logger.info('Completed tokens columns data from string to list.')

        logger.info('Starting tokens processing.')
        df['processed_data'] = df['tokens'].apply(process_list)
        print('Completed tokens processing.')

        if(FILE=='train'):
            word_counts = Counter(word for token_list in df['processed_data'] for word in token_list)
            word_to_id = {word: idx for idx, (word, count) in enumerate(word_counts.items(), start=3) if count >= 5}
            word_to_id['UNK'] = 1
            pickle_file_path = PICKLE_FOLDER / 'word_to_id.pkl'
            with open(pickle_file_path, 'wb') as f:
                pickle.dump(word_to_id, f)
            logger.info(f"Vocabulary saved to {pickle_file_path}")
        df.to_csv(PATH_FILE, index=False)
        logger.info(f"Data saved to {PATH_FILE}")
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except pd.errors.EmptyDataError:
        logger.warning("Input CSV file is empty.")
    except Exception as e:
        logger.error(f"Issues in converting columns data from string to list. Error: {e}")
        return None