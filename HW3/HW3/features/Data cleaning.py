#%%
import pandas as pd
import numpy as np

#%%
# Single function for cleaning and encoding
def process_data(df, columns_drop, columns_fill, columns_hot, columns_binary):
    df_clean = df.dropna(subset=columns_drop)
    df_clean[columns_fill] = df_clean[columns_fill].apply(lambda col: col.fillna(col.mean()))
    df_clean['Binary'] = df_clean[columns_binary].apply(lambda x: 1 if x == 'M' else 0)
    dummy = pd.get_dummies(df_clean[columns_hot])
    encoded_df = pd.concat([df_clean, dummy], axis=1)
    
    return encoded_df
#%%
# Function to clean data (drop and fill with the mean)
def clean_na(df, columns_drop, columns_fill):
    df_clean = df.dropna(subset=columns_drop)
    df_clean[columns_fill] = df_clean[columns_fill].apply(lambda col: col.fillna(col.mean()))
    return df_clean

#%%
# Function to encode data (create dummies and binary variable)
def encode_data(df, columns_drop, columns_fill, columns_hot, columns_binary):
    df_clean['Binary'] = df_clean[columns_binary].apply(lambda x: 1 if x == 'M' else 0)
    dummy = pd.get_dummies(df_clean[columns_hot])
    encoded_df = pd.concat([df_clean, dummy], axis=1)
    return encoded_df
#%%
# Function to drop NaNs
def drop_na(df, columns):
    df_drop = df.dropna(subset=columns)
    return df_drop

#%%
# Function to fill NaNs with the mean
def fill_na(df, columns):
    df[columns] = df[columns].apply(lambda col: col.fillna(col.mean()))
    return df

#%%
# Function to create dummies
def one_hot(df, columns):
    dummy = pd.get_dummies(df[columns])
    encoded_df = pd.concat([df, dummy], axis=1)
    return encoded_df

#%%
# Function to create binary variable
def binary(df, columns):
    df['Binary'] = df[columns].apply(lambda x: 1 if x == 'M' else 0)
    return df

# %%
