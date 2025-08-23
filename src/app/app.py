from flask import Flask, render_template, request
import os
import pickle
import sys

try:
    from waitress import serve
except ImportError:
    serve = None

app = Flask(__name__)


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(PROJECT_ROOT, "trained_model")


best_models = {
    'AAPL': 'AAPL_rf.pkl',
    'AMZN': 'AMZN_rf.pkl',
    'GOOGL': 'GOOGL_rf.pkl',
    'MSFT': 'MSFT_rf.pkl',
    'TSLA': 'TSLA_rf.pkl',
}

models = {}
for ticker, model_file in best_models.items():
    model_path = os.path.join(MODEL_DIR, model_file)
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            models[ticker] = pickle.load(f)
        print(f"✅ Loaded {model_file}")
    else:
        print(f"⚠️ Model file not found for {ticker}: {model_path}", file=sys.stderr)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        ticker = request.form['ticker'].upper()
        if ticker not in models:
            return render_template('index.html', prediction=f"Model for {ticker} not found!")

        model = models[ticker]

        # Get input features
        ma20 = float(request.form['ma20'])
        ma50 = float(request.form['ma50'])
        ma200 = float(request.form['ma200'])

        # Make prediction
        prediction = model.predict([[ma20, ma50, ma200]])[0]

        return render_template('index.html', prediction=round(prediction, 2))

    except ValueError:
        return render_template('index.html', prediction="Invalid input. Please enter numeric values.")
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    if serve:
        # Use Waitress for production
        print(f"⚡ Running on port {port} using Waitress")
        serve(app, host='0.0.0.0', port=port)
    else:
        # Fallback to Flask dev server
        print(f"⚡ Running on port {port} using Flask dev server")
        app.run(host='0.0.0.0', port=port, debug=True)
