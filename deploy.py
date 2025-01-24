# deploy.py

import joblib
import os

def deploy_model():
    """Simulates deploying the trained model."""
    model_file = 'model.joblib'

    if os.path.exists(model_file):
        model = joblib.load(model_file)
        print("Model loaded successfully from:", model_file)

        # Simulate deployment actions
        print("Deploying model to a production environment...")
        print("Model deployment successful!")

        # Here, you can add more specific deployment logic
        # For example, updating a model registry, deploying to a cloud service, etc.

    else:
        print("Error: Model file not found. Please train the model first.")

if __name__ == "__main__":
    deploy_model()
