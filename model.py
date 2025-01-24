# model.py - Simple Linear Regression Model

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_model(data_path="data.csv"):
    """Trains a linear regression model."""
    print("Loading data...")
    data = pd.read_csv(data_path)

    print("Preparing data...")
    X = data[['feature1', 'feature2']]  # Example features
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    print("Saving model...")
    joblib.dump(model, 'model.joblib')

    return model

def predict(model, data):
    """Makes predictions with the trained model."""
    if isinstance(model, str):
        # Load the model if a path is provided
        model = joblib.load(model)

    data_df = pd.DataFrame(data, columns=['feature1', 'feature2'])
    predictions = model.predict(data_df)
    return predictions

if __name__ == "__main__":
    train_model()
