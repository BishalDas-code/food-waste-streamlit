# 🍽️ Food Waste Prediction App

**A Streamlit app to predict leftover food in restaurants and provide actionable suggestions to reduce waste.**



## 🔹 Project Overview

Food waste is a major challenge for restaurants. This app uses **machine learning (Linear Regression)** to predict the amount of food that will be left uneaten based on:

* Food item
* Plate size
* Serving weight
* Price

It provides **suggestions** to reduce waste and optimize menu performance.

---

## 🔹 Features

1. **Predict leftover food** for any menu item.
2. **Dynamic suggestions** to reduce waste:

   * ✅ Keep as is / promote
   * ⚠️ Monitor portion sizes
   * 📉 Reduce portion or adjust price
   * 🚨 High waste – rethink serving size or menu item
3. **Interactive inputs**: select food item, plate size, weight, and price.
4. **Future enhancements possible**: multi-item prediction, CSV upload, visual charts.
5. Built using **Python, Pandas, scikit-learn, and Streamlit**.

---

## 🔹 Dataset

* Simulated restaurant dataset:

  * 12 food items
  * Columns: `Customer_Name`, `Food_Name`, `Plate_Size`, `Serving_Food_Weight_g`, `Leftover_Food_Weight_g`, `Price_Rs`
* Target: `Leftover_Food_Weight_g`

---

## 🔹 Machine Learning Model

* **Model type**: Linear Regression
* **Training process**:

  1. One-hot encode categorical features (`Food_Name`)
  2. Train on `Serving_Food_Weight_g`, `Plate_Size`, `Price_Rs`, and one-hot encoded food items
* **Saved model**: `food_waste_model.pkl` (includes trained model + column names)

---

## 🔹 Installation & Setup

1. Clone the repo:

```bash
git clone https://github.com/yourusername/food-waste-app.git
cd food-waste-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
streamlit run app.py
```

---

## 🔹 Usage

1. Select the **Food Item** from the dropdown.
2. Choose **Plate Size** (1–3).
3. Enter **Serving Weight** in grams.
4. Enter **Price** in ₹.
5. The app predicts **leftover food** and provides **suggestions** to reduce waste.

---

## 🔹 Folder Structure

```
food-waste-app/
│
├─ app.py                  # Streamlit app
├─ food_waste_model.pkl    # Trained ML model + columns
├─ Food_waste-dataset.csv  # Dataset used for training (optional)
├─ requirements.txt        # Python dependencies
└─ README.md
```

---

## 🔹 Future Improvements

* Multi-food item predictions
* Upload CSV for bulk predictions
* Interactive charts for leftover trends
* Menu optimization suggestions
* Integration with inventory management

---

## 🔹 Tech Stack

* Python
* Pandas
* scikit-learn
* Streamlit

---

## 🔹 License

This project is for **educational and hackathon purposes**.


