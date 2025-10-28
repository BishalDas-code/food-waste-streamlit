import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load your dataset
data = pd.read_csv("Food_waste-dataset.csv")

# Prepare features
X = pd.get_dummies(data[['Food_Name','Plate_Size','Serving_Food_Weight_g','Price_Rs']], drop_first=False)
y = data['Leftover_Food_Weight_g']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model AND the column names together
model_columns = X.columns
with open("food_waste_model.pkl", "wb") as f:
    pickle.dump((model, model_columns), f)

print("✅ Model saved with columns as 'food_waste_model.pkl'")
