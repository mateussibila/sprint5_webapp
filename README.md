# Sprint 05 - Vehicle Data Explorer

## 📌 Project Overview
This project is part of the TripleTen Data Analytics Post Graduation (Sprint 05).  
The goal was to develop an **interactive web application using Streamlit** to explore and analyze vehicle data.  
The app enables visualization, filtering, and interactive analysis of a dataset containing vehicle listings.

## 🎯 Objective
Build a **Streamlit application** that allows users to interactively explore vehicle data through tables and visualizations.

## 📂 Dataset
**File:** `/datasets/vehicles.csv` (single dataset)  

**Columns (examples):**  
- `model_year` – Year of the vehicle model.  
- `odometer` – Vehicle mileage (km or miles).  
- `price` – Listing price.  
- Other metadata (brand, model, etc.).

## 📝 Steps

1. **Streamlit Setup**  
   - Configured the Streamlit environment.  
   - Loaded dataset from CSV.  

2. **Data Viewer**  
   - Displayed the vehicle dataset in a clean table format.  
   - Added checkbox filter to show only models with more than 500 ads.  

3. **Histogram: Vehicle Model Year**  
   - Built an interactive histogram of `model_year`.  
   - Users generate the plot dynamically using a button.  

4. **Scatter Plot: Price vs. Odometer**  
   - Created scatter plot comparing price against odometer.  
   - Interactive button to generate visualization.  

5. **Deployment**  
   - Deployed live app on **Render**:  
     👉 [Vehicle Data Explorer](https://sprint5-webapp.onrender.com/)  

## 📊 Results
- Users can filter and analyze vehicle listings dynamically.  
- Histogram shows distribution of cars by model year.  
- Scatter plot highlights the relationship between **vehicle price and odometer**.  
- The app demonstrates practical use of **Streamlit for interactive analytics**.  

## 🏁 Conclusion
- Streamlit enables rapid development of interactive dashboards.  
- Vehicle dataset exploration helps identify trends in pricing and usage.  
- This sprint provided hands-on practice with **web app deployment for data analysis**.  

## 🛠 Tools & Technologies
- Python 3.x  
- Pandas  
- Streamlit  
- Matplotlib  

## 🗂 Repository Structure
sprint-05-vehicle-explorer/  
│  
├── README.md  
├── app.py  
└── vehicles.csv  

- `README.md` – Project documentation and overview  
- `app.py` – Streamlit application script  
- `vehicles.csv` – dataset used for analysis
