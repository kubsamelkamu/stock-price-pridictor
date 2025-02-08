import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

MODEL_PATH = 'models/trained_models'
tickers = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']
models = {}


for ticker in tickers:
    for model_type in ['lr', 'dt', 'rf']:
        model_filename = f'{MODEL_PATH}/{ticker}_{model_type}.pkl'
        if os.path.exists(model_filename):
            with open(model_filename, 'rb') as f:
                models[f'{ticker}_{model_type}'] = pickle.load(f)

# Load datasets and plot actual vs predicted values
processed_data_path = "./data/processed_cleaned"
for ticker in tickers:
    df = pd.read_csv(f'{processed_data_path}/featured_engineered_{ticker}.csv', index_col='Date', parse_dates=True)
    X = df[['MA20', 'MA50', 'MA200']]
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    
    plt.figure(figsize=(12, 8))
    for i, model_type in enumerate(['lr', 'dt', 'rf']):
        model_key = f'{ticker}_{model_type}'
        if model_key in models:
            model = models[model_key]
            y_pred = model.predict(X_test)
            
            plt.subplot(3, 1, i + 1)
            plt.plot(y_test.values, label='Actual Prices', color='blue', linestyle='dashed')
            plt.plot(y_pred, label='Predicted Prices', color='red')
            plt.title(f'{ticker} - {model_type.upper()}')
            plt.xlabel('Time')
            plt.ylabel('Stock Price')

    plt.tight_layout()
    plt.show()
