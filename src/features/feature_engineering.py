import pandas as pd
import os

def create_features(df):
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    return df

raw_data_path = 'data/raw'
processed_data_path = "../data/processed_cleaned"
os.makedirs(processed_data_path, exist_ok=True)

for file in os.listdir(raw_data_path):
    if file.endswith('.csv'):
        df = pd.read_csv(f'{raw_data_path}/{file}')
        
        print(f'Columns in {file}: {df.columns.tolist()}')

        if 'Date' in df.columns:
            df = pd.read_csv(f'{raw_data_path}/{file}', index_col='Date', parse_dates=True)
            df = create_features(df)
            df.to_csv(f'{processed_data_path}/{'featured_engineered_'+file}')
            print(f'Processed data for {file}')
        else:
            print(f'Error: "Date" column not found in {file}')