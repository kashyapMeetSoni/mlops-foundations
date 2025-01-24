# model.py - A very simple model for demonstration

def train_model():
  """Simulates training a model."""
  print("Model training started...")
  print("Model training complete!")
  return "Trained Model"

def predict(model, data):
  """Simulates making a prediction."""
  print(f"Predicting with {model} on data: {data}")
  return "Prediction Result"

# Example usage (you can comment these out later if needed)
trained_model = train_model()
prediction = predict(trained_model, [1, 2, 3])
print(prediction)
