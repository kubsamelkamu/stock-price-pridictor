# Stock price pridictor
This project predicts stock prices using machine learning models. 

## setup
1.**clone the repository:
``` bash
    cd stock-price-predictor
```
2.**Create and Activate Virtual enviroment:
```bash
    python -m venv venv
    source venv/Scripts/activate  
```
3.**Install dependencies:
```bash
   pip install -r requirements.txt
```
4.**Download and preprocess Data:
```bash
   python src/data/download_data.py
   python src/features/feature_engineering.py
```
5.**Train Models:
```bash
   python models/train_model.py
```
6.Evaluate Models:
``` bash
    python models/evaluate_model.py
```
## Run Flask Application
1.**Navigate to the src/app directory:
```bash
    cd src/app
    python app.py
```
2.**Open the application in your browser:Go to http://127.0.0.1:500/





