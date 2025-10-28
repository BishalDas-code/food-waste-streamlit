import streamlit as st
import pandas as pd
import pickle

# ===== Load the model =====
with open("food_waste_model.pkl", "rb") as file:
    model, model_columns = pickle.load(file)

# ===== Page Config =====
st.set_page_config(
    page_title="🍽️ Food Waste Predictor",
    page_icon="🍕",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===== Landing Page Header =====
st.markdown("""
<div style="text-align:center; padding:20px; background-color:#f0f8ff; border-radius:10px;">
<h1 style="color:#FF6F61;">🍽️ Food Waste Prediction App</h1>
<p style="font-size:18px;">Predict leftover food, see the waste category, and get actionable suggestions!</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ===== Input Fields =====
col1, col2 = st.columns(2)

food_items = ['Pizza', 'Burger', 'Pasta', 'Noodles', 'Salad', 'Soup', 
              'Fried Rice', 'Thali', 'Biryani', 'Dosa', 'Sandwich', 'Ice Cream']

with col1:
    food = st.selectbox("🍔 Select Food Item", food_items)
    plate_size = st.selectbox("🍽️ Plate Size", [1, 2, 3])

with col2:
    serving_weight = st.number_input("⚖️ Serving Food Weight (grams)", min_value=100, max_value=600, value=250, step=50)
    price = st.number_input("💰 Price (₹)", min_value=50, max_value=1000, value=250, step=10)

st.write("---")

# ===== Prepare Input =====
example = pd.DataFrame({
    'Plate_Size': [plate_size],
    'Serving_Food_Weight_g': [serving_weight],
    'Price_Rs': [price]
})

# One-hot encode food items
for item in food_items:
    col_name = f'Food_Name_{item}'
    example[col_name] = 1 if food == item else 0

# Align columns with model
example = example.reindex(columns=model_columns, fill_value=0)

# ===== Prediction =====
predicted_leftover = model.predict(example)[0]

# ===== Waste Category =====
waste_percent = (predicted_leftover / serving_weight) * 100
if waste_percent <= 10:
    waste_category = "Low"
    color = "#28a745"  # green
elif waste_percent <= 25:
    waste_category = "Medium"
    color = "#ffc107"  # yellow
elif waste_percent <= 50:
    waste_category = "High"
    color = "#fd7e14"  # orange
else:
    waste_category = "Very High"
    color = "#dc3545"  # red

# ===== Suggestion Logic =====
if waste_category == "Low":
    suggestion = "✅ Keep as is / promote"
elif waste_category == "Medium":
    suggestion = "⚠️ Monitor portion sizes"
elif waste_category == "High":
    suggestion = "📉 Reduce portion or adjust price"
else:
    suggestion = "🚨 High waste! Rethink serving size or menu item"

# ===== Output =====
st.subheader("📊 Prediction Result")
st.markdown(f"<h3 style='color:{color}'>{waste_category} Waste</h3>", unsafe_allow_html=True)
st.metric(label="Predicted Leftover (grams)", value=f"{predicted_leftover:.2f} g")
st.markdown(f"**Suggestion:** {suggestion}")

# Progress bar visualization
percent_leftover = min(predicted_leftover / serving_weight, 1.0)
st.progress(percent_leftover)

# ===== Optional Info Box =====
st.info("""
**Instructions:**  
- Select the food item and plate size.  
- Input the serving weight and price.  
- Click predict to see leftover estimation, waste category, and recommendations.  
- Use this info to optimize menu, portion sizes, or pricing!
""")

# ===== Footer =====
st.markdown("<p style='text-align:center; color:gray;'>Created for Hackathon Demo | Made with ❤️ in Streamlit</p>", unsafe_allow_html=True)
