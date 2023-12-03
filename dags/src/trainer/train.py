# import pandas as pd
# import tensorflow as tf
# import mlflow
# import mlflow.tensor
# import mlflow.keras
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.layers import Embedding, Dense, Input, MultiHeadAttention, Dropout, GlobalAveragePooling1D, LayerNormalization
# from tensorflow.keras.models import Model
# from pathlib import Path
# import pandas as pd
# import os
# ROOT_DIR  = Path('__file__').resolve().parent.parent.parent.parent
# DATA_DIR = ROOT_DIR / 'data' / 'inter'
# FINAL_DATA_DIR = ROOT_DIR / 'data' / 'final'
# print(ROOT_DIR, DATA_DIR, FINAL_DATA_DIR)

# df = pd.read_json(FINAL_DATA_DIR/ 'final' / 'test_pre_process.json', lines = True)

# print(df.shape)

# print(os.listdir())

# train = pd.read_json(FINAL_DATA_DIR/ 'train_pre_process.json', lines = True)
# test = test = pd.read_json(FINAL_DATA_DIR/ 'test_pre_process.json', lines = True)

