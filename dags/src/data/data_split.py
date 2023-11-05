
import pandas as pd
from sklearn.model_selection import train_test_split

def merge_data(PROJECT_FOLDER):
    try:
        RAW_DATA_FOLDER = PROJECT_FOLDER / 'data' / 'raw'
        train_csv = pd.read_csv(RAW_DATA_FOLDER / 'train.csv')
        test_csv = pd.read_csv(RAW_DATA_FOLDER / 'test.csv')
        valid_csv = pd.read_csv(RAW_DATA_FOLDER / 'validation.csv')
        df = pd.concat([train_csv, test_csv, valid_csv], ignore_index=True)
    except Exception as e:
        print(f"Issues in loading raw data files. Error: {e}")
        return None
    
    final_df = df.drop_duplicates(subset=['tokens'])
    print(final_df.head())
    return final_df

def split_data(PROJECT_FOLDER):
    INT_FOLDER = PROJECT_FOLDER / 'data' / 'inter'
    train_path = INT_FOLDER / 'train.csv'
    test_path = INT_FOLDER / 'test.csv'
    INT_FOLDER.mkdir(parents=True, exist_ok=True)
    # Check if the files exist
    if not train_path.exists() and not test_path.exists():
        print('started splitting data into train and test data.')
        df = merge_data(PROJECT_FOLDER)
        train_df, test_df = train_test_split(df, test_size=0.2)
        test_df.to_csv(test_path, index = False)
        train_df.to_csv(train_path, index = False)
    else:
        print("Train and test CSV files already exist. Skipping the processing.")


    
# def conver_to_list(PROJECT_FOLDER):
#     try:
#         df = merge_data(PROJECT_FOLDER)
#         if(df is None):
#             raise Exception("data is empty")
#         print('started coverting columns data from string to list.')
#         df['tokens'] = df['tokens'].apply(ast.literal_eval)
#         print('Completed tokens columns data from string to list.')
#         df['ner_tags'] = df['ner_tags'].apply(ast.literal_eval)
#         print('Completed ner_tags columns data from string to list.')
#         return df

#     except Exception as e:
#         print(f"Issues in coverting columns data from string to list. Error: {e}")
#         return None
    
# def split_data(PROJECT_FOLDER):
#     FINAL_FOLDER = PROJECT_FOLDER / 'data' / 'final'
#     train_path = FINAL_FOLDER / 'train.csv'
#     test_path = FINAL_FOLDER / 'test.csv'
#     FINAL_FOLDER.mkdir(parents=True, exist_ok=True)
#     # Check if the files exist
#     if not train_path.exists() and not test_path.exists():
#         print('started splitting data into train and test data.')
#         df = merge_data(PROJECT_FOLDER)
#         print('started converting columns data from string to list.')
#         list_df = conver_to_list(df)
#         print('completed converting columns data from string to list.')
#         train_df, test_df = train_test_split(list_df, test_size=0.2)
#         test_df.to_csv(test_path, index = False)
#         train_df.to_csv(train_path, index = False)
#     else:
#         print("Train and test CSV files already exist. Skipping the processing.")
 
# def parallel_process_tokens_column(df):
#     num_cores = cpu_count()  # Number of cores on your machine
    
#     # Split DataFrame into chunks based on the number of cores
#     df_chunks = np.array_split(df, num_cores)

#     # Using ProcessPoolExecutor to parallelize the processing
#     with ProcessPoolExecutor(max_workers=num_cores) as executor:
#         processed_chunks = list(executor.map(process_tokens_column_chunk, df_chunks))
        
#     return pd.concat(processed_chunks, ignore_index=True)

# def process_list(input_list):
#     return [process_string(s) for s in input_list]

# import pandas as pd
# from multiprocessing import Pool, cpu_count

# def process_tokens_column_chunk(df_chunk):
#     """Process a chunk of the DataFrame"""
#     df_chunk['tokens'] = df_chunk['tokens'].apply(process_list)
#     return df_chunk


# def process_string(s):
#     # Check if the string represents a number (integer or decimal)
#     if re.match(r'^\d+(\.\d+)?$', s):
#         return "[num]"
#     else:
#         return s.lower()

# def split_data(PROJECT_FOLDER):
#     FINAL_FOLDER = PROJECT_FOLDER / 'data' / 'final'
#     train_path = FINAL_FOLDER / 'train.csv'
#     test_path = FINAL_FOLDER / 'test.csv'
#     FINAL_FOLDER.mkdir(parents=True, exist_ok=True)
#     # Check if the files exist
#     if not train_path.exists() and not test_path.exists():
#         df = merge_data(PROJECT_FOLDER)
#         df = parallel_process_tokens_column(df)
#         print(df.head(10))
#         train_df, test_df = train_test_split(df, test_size=0.2)
#         test_df.to_csv(test_path, index = False)
#         train_df.to_csv(train_path, index = False)
#     else:
#         print("Train and test CSV files already exist. Skipping the processing.")