import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import os
import pickle

processed_data_path = '../data/processed_cleaned'
tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']

data = {
    ticker: pd.read_csv(
        f"{processed_data_path}/featured_engineered_{ticker}.csv",
        index_col='Date', parse_dates=True
    ) 
    for ticker in tickers
}

def train_and_save_models(ticker, X_train, y_train):
    models = {}

    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    models[f'{ticker}_lr'] = lr_model

    dt_model = DecisionTreeRegressor()
    dt_model.fit(X_train, y_train)
    models[f'{ticker}_dt'] = dt_model
    
    rf_model = RandomForestRegressor()
    rf_model.fit(X_train, y_train)
    models[f'{ticker}_rf'] = rf_model
    
    os.makedirs('trained_model', exist_ok=True)
    for model_name, model in models.items():
        with open(f'trained_model/{model_name}.pkl', 'wb') as f:
            pickle.dump(model, f)

for ticker in tickers:
    df = data[ticker]

    df = df.dropna()

    X = df[['MA20', 'MA50', 'MA200']]
    y = df['Close']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    train_and_save_models(ticker, X_train, y_train)
    print(f'Trained and saved models for {ticker}')
