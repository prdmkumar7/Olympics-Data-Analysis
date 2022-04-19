import pandas as pd

def preprocess(df,region_df):
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # remove the 1906 edition
    df = df[df['Year']!=1906]
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df