import streamlit as st
import pandas as pd
import pickle

# ===== Load the model =====
with open("food_waste_model.pkl", "rb") as file:
    model, model_columns = pickle.load(file)

# ===== App Title =====
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

# One-hot encode food item
for item in food_items:
    col_name = f'Food_Name_{item}'
    example[col_name] = 1 if food == item else 0

# Align input columns with model columns
example = example.reindex(columns=model_columns, fill_value=0)

# ===== Make Prediction =====
predicted_leftover = model.predict(example)[0]

# ===== Suggestion Logic =====
if predicted_leftover < 50:
    suggestion = "✅ Keep as is / promote"
elif predicted_leftover < 100:
    suggestion = "⚠️ Monitor portion sizes"
elif predicted_leftover < 150:
    suggestion = "📉 Reduce portion or adjust price"
else:
    suggestion = "🚨 High waste! Rethink serving size or menu item"

# ===== Output =====
st.subheader("Prediction Result")
st.write(f"**Predicted Leftover:** {predicted_leftover:.2f} grams")
st.write(f"**Suggestion:** {suggestion}")

# ===== Optional: Add info / instructions =====
st.markdown("""
---
**How to use:**  
1. Select the food item.  
2. Choose plate size, serving weight, and price.  
3. The app, predicts leftover food and gives a suggestion to reduce waste.  
""")
