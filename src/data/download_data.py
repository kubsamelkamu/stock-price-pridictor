import yfinance as yf
import os

tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']

os.makedirs('data/raw', exist_ok=True)

for ticker in tickers:
    data = yf.download(ticker, start='2015-01-01', end='2025-01-01')
    data.reset_index(inplace=True)  
    data.to_csv(f'data/raw/{ticker}.csv', index=False)
    print(f'Downloaded data for {ticker}')