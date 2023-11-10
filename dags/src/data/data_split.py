
import pandas as pd
from sklearn.model_selection import train_test_split

def merge_data(PROJECT_FOLDER):
    
    """
    Merges and de-duplicates data from raw CSV files.

    This function reads three CSV files (train, test, and validation) located in the 'data/raw' directory 
    specified by PROJECT_FOLDER. It then concatenates these files and removes duplicate rows based on the 'tokens' column.

    :param PROJECT_FOLDER: A Path object representing the project's root directory.
    :return: A DataFrame containing the merged and de-duplicated data.
    """
    
    try:
        RAW_DATA_FOLDER = PROJECT_FOLDER / 'data' / 'raw'
        train_csv = pd.read_csv(RAW_DATA_FOLDER / 'train.csv')
        test_csv = pd.read_csv(RAW_DATA_FOLDER / 'test.csv')
        valid_csv = pd.read_csv(RAW_DATA_FOLDER / 'validation.csv')
        df = pd.concat([train_csv, test_csv, valid_csv], ignore_index=True)
    except Exception as e:
        print(f"Issues in loading raw data files. Error: {e}")
        return None
    
    final_df = df.drop_duplicates(subset=['tokens']) # Remove duplicate rows based on the 'tokens' column
    return final_df

def split_data(PROJECT_FOLDER, logger):
    
    """
    Splits the merged data into training and testing sets and saves them as CSV files.

    This function checks if the training and testing CSV files already exist in the 'data/inter' directory 
    specified by PROJECT_FOLDER. If they do not exist, it calls the merge_data function to merge the raw data 
    and then splits it into training and testing sets. The resulting sets are saved as CSV files in the 
    'data/inter' directory.

    :param PROJECT_FOLDER: A Path object representing the project's root directory.
    """
    
    INT_FOLDER = PROJECT_FOLDER / 'data' / 'inter'
    train_path = INT_FOLDER / 'train.csv'
    test_path = INT_FOLDER / 'test.csv'
    INT_FOLDER.mkdir(parents=True, exist_ok=True) # Create the 'data/inter' directory if it doesn't exist
    
    # Check if the files exist
    if not train_path.exists() and not test_path.exists():
        logger.info('Started splitting data into train and test data.')
        df = merge_data(PROJECT_FOLDER) # Calls merge_data function to get the merged data
        if df is not None:
            train_df, test_df = train_test_split(df, test_size=0.2)  # Splits data into train and test sets
            test_df.to_csv(test_path, index=False)  # Save the test set as a CSV file
            train_df.to_csv(train_path, index=False)  # Save the train set as a CSV file
            logger.info("Train and test data split and saved successfully.")
        else:
            print("Train and test CSV files already exist. Skipping the processing.")
            logger.warning("Skipping data splitting due to issues in merging data.")
    else:
        logger.info("Train and test CSV files already exist. Skipping the processing.")


    
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