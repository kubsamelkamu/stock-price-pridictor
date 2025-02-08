from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)


best_models = {
    'AAPL': 'AAPL_rf.pkl',
    'AMZN': 'AMZN_rf.pkl',
    'GOOGL': 'GOOGL_rf.pkl',
    'MSFT': 'MSFT_rf.pkl',
    'TSLA': 'TSLA_rf.pkl',
    
}

models = {}
for ticker, model_file in best_models.items():
    with open(f'../../models/trained_models/{model_file}', 'rb') as f:
        models[ticker] = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']
    model = models[ticker]
    
    # Get input features
    ma20 = float(request.form['ma20'])
    ma50 = float(request.form['ma50'])
    ma200 = float(request.form['ma200'])
    
    # Make prediction
    prediction = model.predict([[ma20, ma50, ma200]])[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)