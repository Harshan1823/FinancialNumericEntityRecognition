import pandas as pd
import ast
import re
def process_string(s):
    # Check if the string represents a number (integer or decimal)
    if re.match(r'^\d+(\.\d+)?$', s):
        return "[num]"
    else:
        return s.lower()

def process_list(input_list):
    return [process_string(s) for s in input_list]

def conver_to_list(PROJECT_FOLDER, FILE):
    
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
        FINAL_FOLDER.mkdir(parents=True, exist_ok=True) # Create the 'data/final' directory if it doesn't exist
        path_file = FINAL_FOLDER/f'{FILE}.csv'
        print(path_file)
        if(path_file.exists()):
            print("Data already exists")
            return None
        df = pd.read_csv(INTER_FOLDER / f'{FILE}.csv') # Read data from the 'data/inter' directory
        if(df is None):
            raise Exception("data is empty")
        print('started coverting columns data from string to list.')
        df['tokens'] = df['tokens'].apply(ast.literal_eval) # Convert string representation of lists to actual lists
        print('Completed tokens columns data from string to list.')
        print('Starting tokens num.')
        df['processed_data'] = df['tokens'].apply(process_list) # Process tokens using the process_string function
        print('Completed tokens num.')
        df.to_csv(FINAL_FOLDER / f'{FILE}.csv', index = False) # Save the processed data as a CSV file
    except Exception as e:
        print(f"Issues in coverting columns data from string to list. Error: {e}")
        return None
