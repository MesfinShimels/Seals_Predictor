import pandas as pd
import numpy as np

def load_data(train_path, test_path, store_path):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    store = pd.read_csv(store_path)
    return train, test, store

def clean_data(train, test, store):
    train = train.merge(store, on='Store', how='left')
    test = test.merge(store, on='Store', how='left')
    train.fillna(0, inplace=True)
    test.fillna(0, inplace=True)
    train['Sales'] = np.log1p(train['Sales'])  # Apply log transformation
    return train, test

def save_cleaned_data(train, test):
    train.to_csv('Cleaned_Data/clean_train.csv', index=False)
    test.to_csv('Cleaned_Data/clean_test.csv', index=False)
