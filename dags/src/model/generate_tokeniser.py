from pathlib import Path
def genereate_tokenizer(PROJECT_FOLDER, logger):
    import pandas as pd
    import tensorflow as tf
    import pickle
    from tensorflow.keras.preprocessing.text import Tokenizer

    MODEL_STORE = PROJECT_FOLDER / 'model_store'
    FILE_NAME = 'tokenizerV1.pkl'

    MODEL_STORE.mkdir(parents=True, exist_ok=True)
    if((MODEL_STORE / FILE_NAME).exists()):
        logger.info("Pickle file already exists")
        return None

    DATA_STORE = PROJECT_FOLDER / 'data' / 'final' / 'train_pre_process.json'
    train = pd.read_json(DATA_STORE, lines = True)
    vocab = list(set(train["tokens"].explode()))
    n_vocab = len(vocab)
    sent = train['tokens']
    tokenizer = Tokenizer(num_words=n_vocab, oov_token="<OOV>", lower=True)
    tokenizer.fit_on_texts(sent)
    logger.info(f'Writing pickle file to {MODEL_STORE} / {FILE_NAME}')
    with open(MODEL_STORE / FILE_NAME, "wb") as file:
        pickle.dump(tokenizer, file)
    logger.info(f'Pickle file to {MODEL_STORE} / {FILE_NAME}')