import pandas as pd
import os

def create_features(df):
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    return df

raw_data_path = 'data/raw'
processed_data_path = "data/processed"
os.makedirs(processed_data_path, exist_ok=True)

for file in os.listdir(raw_data_path):
    if file.endswith('.csv'):
        df = pd.read_csv(f'{raw_data_path}/{file}', parse_dates=['Date'])
        df.set_index('Date', inplace=True)

        print(f'Columns in {file}: {df.columns.tolist()}')
        print(df.dtypes) 

        if 'Close' in df.columns:
            df = create_features(df)
            df.to_csv(f"{processed_data_path}/featured_engineered_{file}")
            print(f'Processed data for {file}')
            print(f"{processed_data_path}/featured_engineered_{file}")
        else:
            print(f'Error: "Close" column not found in {file}')
