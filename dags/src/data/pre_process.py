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
    try:
        INTER_FOLDER = PROJECT_FOLDER / 'data' / 'inter'
        FINAL_FOLDER = PROJECT_FOLDER / 'data' / 'final'
        FINAL_FOLDER.mkdir(parents=True, exist_ok=True)
        path_file = FINAL_FOLDER/f'{FILE}.csv'
        print(path_file)
        if(path_file.exists()):
            print("Data already exists")
            return None
        df = pd.read_csv(INTER_FOLDER / f'{FILE}.csv')
        if(df is None):
            raise Exception("data is empty")
        print('started coverting columns data from string to list.')
        df['tokens'] = df['tokens'].apply(ast.literal_eval)
        print('Completed tokens columns data from string to list.')
        print('Starting tokens num.')
        df['processed_data'] = df['tokens'].apply(process_list)
        print('Completed tokens num.')
        df.to_csv(FINAL_FOLDER / f'{FILE}.csv', index = False)
    except Exception as e:
        print(f"Issues in coverting columns data from string to list. Error: {e}")
        return None
