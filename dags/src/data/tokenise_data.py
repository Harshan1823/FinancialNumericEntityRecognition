
def tokenise_data(PROJECT_FOLDER, FILE, LOGGER):

    """
    Tokenise the data and save as a CSV file.

    This function reads data from a CSV file in the 'data/final' directory, tokenises the data, and saves the data as a CSV file in the 'data/final' directory.

    :param PROJECT_FOLDER: A Path object representing the project's root directory.
    :param FILE: A string representing the name of the CSV file to be processed.
    :param Logger: A logger object to log.
    """
    import ast
    import pickle
    import pandas as pd
    logger = LOGGER

    df = pd.read_csv(PROJECT_FOLDER/ 'data' / 'final' / f'{FILE}.csv')
    if(df is None):
        raise Exception("data is empty")
    
    logger.info('Starting tokenising data.')

    logger.info('Converting processed_data to a list.')
    df['processed_data'] = df['processed_data'].apply(ast.literal_eval)

    logger.info('Converting ner_tags to a list.')
    df['ner_tags'] = df['ner_tags'].apply(ast.literal_eval)

    
    PICKLE_PATH = PROJECT_FOLDER / 'model_store' / 'word_to_id.pkl'

    with open(PICKLE_PATH, 'rb') as file:
        token_id_mapping = pickle.load(file)
        
    df['tokenise_data'] = df['processed_data'].apply(lambda x: [token_id_mapping[word] if word in token_id_mapping else token_id_mapping['UNK'] for word in x])
    FILE_LOC = PROJECT_FOLDER/ 'data' / 'final' / f'{FILE}_encoded.json'
    df.to_json(FILE_LOC, orient='records', lines=True)
    
