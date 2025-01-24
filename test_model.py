# test_model.py

import unittest
import pandas as pd
from model import train_model, predict
import joblib
import os

class TestModel(unittest.TestCase):
    def setUp(self):
        # Create dummy data for testing
        self.data = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [2, 4, 6],
            'target': [3, 6, 9]
        })
        self.data.to_csv("test_data.csv", index=False)

        # Train a model for testing predictions
        self.trained_model = train_model("test_data.csv")

    def test_train_model(self):
        model = train_model("test_data.csv")
        self.assertIsNotNone(model)

    def test_predict(self):
        # Use the trained model from setUp
        model = self.trained_model

        # Ensure the model is loaded (it should be already)
        self.assertIsNotNone(model)

        # Create test data
        test_data = [[4, 8], [5, 10]]

        # Get predictions
        predictions = predict(model, test_data)

        # Assertions to validate predictions (adjust as needed)
        self.assertEqual(len(predictions), 2)  # Check if we got 2 predictions
        self.assertGreater(predictions[0], 0) # Check if predictions are positive

    def tearDown(self):
        # Clean up the dummy data file
        if os.path.exists("test_data.csv"):
            os.remove("test_data.csv")
        if os.path.exists('model.joblib'):
            os.remove('model.joblib')

if __name__ == '__main__':
    unittest.main()
