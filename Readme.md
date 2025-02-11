# Stock price pridictor
This project predicts stock prices using machine learning models. The application is built with Flask and uses historical stock data for training. The UI is designed to be user-friendly and interactive, providing insights into the input features used for predictions.

## setup
1.clone the repository:
``` bash
    cd stock-price-predictor
```
2.Create and Activate Virtual enviroment:
```bash
    python -m venv venv
    venv\Scripts\activate
```
3.Install dependencies:
```bash
   pip install -r requirements.txt
```
4.Download and preprocess Data:
```bash
   python src/data/download_data.py
   python src/features/feature_engineering.py
```
5.Train Models:
```bash
   python models/train_model.py
```
6.Evaluate Models:
``` bash
    python models/evaluate_model.py
```
## Run Flask Application
1.Navigate to the src/app directory:
```bash
    cd src/app
    python app.py
```
2.Open the application in your browser:Go to http://127.0.0.1:500/


## Using The application
### 1.Select Stock Ticker:
  Choose a stock ticker (e.g., Apple (AAPL), Microsoft (MSFT)) from the dropdown menu.
### 2.Enter Moving Average Values:
  Enter the values for MA20, MA50, and MA200. These are the 20-day, 50-day, and 200-day moving averages of the stock's closing price.
### 3.Get Pridiction:
  Click the "Predict" button to get the predicted stock price based on the input values.

## Explanation of Input features
### MA20 (20-day Moving Average):

The average closing price of the stock over the past 20 trading days. This helps to smooth out short-term fluctuations and highlight longer-term trends
### MA50 (50-day Moving Average):

The average closing price of the stock over the past 50 trading days. It is often used to identify medium-term trends in the stock's price
### MA200 (200-day Moving Average):

The average closing price of the stock over the past 200 trading days. It is used to identify long-term trends and is a strong indicator of the overall market direction for the stock



