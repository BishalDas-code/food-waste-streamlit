import streamlit as st
import pandas as pd
import pickle

# ===== Load the Model and Columns =====
with open("food_waste_model.pkl", "rb") as file:
    model, model_columns = pickle.load(file)


st.title("🍽️ Food Waste Prediction App")
st.write("Predict leftover food and get suggestions to reduce waste.")

# ===== Input Fields =====
food_items = ['Pizza', 'Burger', 'Pasta', 'Noodles', 'Salad', 'Soup', 
              'Fried Rice', 'Thali', 'Biryani', 'Dosa', 'Sandwich', 'Ice Cream']

food = st.selectbox("Select Food Item", food_items)
plate_size = st.selectbox("Plate Size", [1, 2, 3])
serving_weight = st.number_input("Serving Food Weight (grams)", min_value=100, max_value=600, value=250, step=50)
price = st.number_input("Price (₹)", min_value=50, max_value=1000, value=250, step=10)

# ===== Prepare Input =====
example = pd.DataFrame({
    'Plate_Size': [plate_size],
    'Serving_Food_Weight_g': [serving_weight],
    'Price_Rs': [price]
})

# One-hot encode food names for all items
for item in food_items:
    example[f'Food_Name_{item}'] = 1 if food == item else 0

# Reindex to match training columns
example = example.reindex(columns=model_columns, fill_value=0)

# ===== Prediction =====
predicted_leftover = model.predict(example)[0]

# ===== Suggestion Logic =====
def get_suggestion(leftover):
    if leftover < 50:
        return "✅ Keep as is / promote"
    elif leftover < 100:
        return "⚠️ Monitor portion sizes"
    elif leftover < 150:
        return "📉 Reduce portion or adjust price"
    else:
        return "🚨 High waste! Rethink serving size or menu item"

suggestion = get_suggestion(predicted_leftover)

# ===== Output =====
st.subheader("Prediction Result")
st.write(f"**Predicted Leftover:** {predicted_leftover:.2f} grams")
st.write(f"**Suggestion:** {suggestion}")
