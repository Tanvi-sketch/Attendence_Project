import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load dataset
import os

file_path = os.path.join(os.path.dirname(__file__), "attendance.csv")
data = pd.read_csv(file_path)

X = data[['total', 'attended']]
y = data['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

def predict_status(total, attended):
    return model.predict([[total, attended]])[0]