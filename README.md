# Airbnb Listings Dashboard (Python | Streamlit)

This project is an **interactive Airbnb Listings Dashboard** built using **Python and Streamlit**.  
It analyzes Airbnb listings data to uncover insights related to **pricing, room types, reviews, and geographic distribution**.

The project demonstrates an end-to-end workflow:
- Data cleaning and exploratory analysis in Jupyter Notebook
- Reuse of cleaned data in an interactive Streamlit dashboard

---

## 📌 Project Objectives

- Clean and preprocess Airbnb listings data
- Perform exploratory data analysis (EDA)
- Analyze pricing and review patterns
- Build an interactive dashboard for data exploration

---

## 🛠️ Tools & Technologies

- **Python**
- Pandas, NumPy
- Streamlit
- Plotly
- Matplotlib, Seaborn
- Jupyter Notebook

---

## 📂 Project Files

| File | Description |
|-----|-------------|
|[ `🏠 Airbnb Listings Dashboard.py`](https://github.com/shivakumarmurarishetti/airbnb-listings-python-dashboard/blob/main/%F0%9F%8F%A0%20Airbnb%20Listings%20Dashboard.py) | Streamlit application for the interactive dashboard |
|[`eda_cleaning.ipynb`](https://github.com/shivakumarmurarishetti/airbnb-listings-python-dashboard/blob/main/eda_cleaning.ipynb) | Data cleaning and exploratory data analysis |
| [`cleaned_listings.csv`](https://github.com/shivakumarmurarishetti/airbnb-listings-python-dashboard/blob/main/cleaned_listings.csv) | Cleaned Airbnb listings dataset |
| [`requirements.txt`](https://github.com/shivakumarmurarishetti/airbnb-listings-python-dashboard/blob/main/requirements.txt) | Python dependencies |
| [`README.md`]() | Project documentation |

---

## 📊 Dashboard Features

### 🎛️ Interactive Filters
- Neighbourhood group selection
- Room type selection
- Price range slider
- Text search by listing name, neighbourhood, or room type

### 📈 Visualizations
- Room type distribution
- Price vs number of reviews
- Interactive geographic map of listings
- Price distribution histogram

### 📋 Data Exploration
- Summary metrics (total listings, average price, most frequent room type)
- Top 5 most expensive listings
- Filtered listings table with CSV download option
- Optional descriptive statistics

---

## 🧹 Data Processing Workflow

1. Raw Airbnb data cleaned and prepared in Jupyter Notebook
2. Missing values handled and key columns selected
3. Cleaned dataset exported as `cleaned_listings.csv`
4. Dataset reused in the Streamlit dashboard for visualization

---

## ▶️ How to Run the Project

1. Download the repository from GitHub  
   - Click **Code → Download ZIP**
   - Extract the ZIP file
2. Open a terminal/command prompt inside the project folder
3. Install dependencies:
   ```bash
   pip install -r requirements.txt(https://github.com/shivakumarmurarishetti/airbnb-listings-python-dashboard/blob/main/requirements.txt)
4. Run the Streamlit dashboard:
    ```bash
    streamlit run "🏠 Airbnb Listings Dashboard.py"
The dashboard will open automatically in your browser
(usually at http://localhost:8501).

## 🖼️ Dashboard Preview
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/89efb282-0b30-4e4e-baea-879d478b46d2" />
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/20f3ee0d-4ae8-4030-9f04-6bbcbd20b010" />
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/41c234bc-ded2-4223-8688-83619ec60aa2" />
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/6ad6ad8e-7ed8-448d-ae74-52d58ded162b" />
<img width="2560" height="1504" alt="image" src="https://github.com/user-attachments/assets/c4c25d43-26f6-4987-a54e-90dd1b2e8a7f" />



