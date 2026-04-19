🌍 Climate Trend Analyzer Dashboard

A Power BI–style climate analytics dashboard built using Python, Streamlit, and Plotly to analyze long-term environmental trends across countries.

This project transforms raw climate data into executive-level insights, helping understand patterns in temperature, rainfall, CO₂ emissions, renewable energy, and extreme weather events.

🚀 Project Overview

Climate change is one of the most critical global challenges. This project simulates a real-world climate analytics system used by:

Governments 🌐
Environmental agencies 🌱
Policy makers 📊
Climate-tech companies ⚡

The dashboard enables:

📈 Trend analysis over time
🌍 Geographic comparison
🏆 Country benchmarking
📊 Multi-metric analysis
🧠 Insight generation for decision-making
🧠 Key Features
🔹 Executive Dashboard
KPI cards (Temperature, Rainfall, CO₂, Events)
Trend direction (Upward / Downward / Stable)
Peak year detection
Top & lowest performing countries
🔹 Trend Analytics
Time-series visualization
Long-term trendline
Pattern identification
🔹 Geographic Intelligence
Interactive world map (choropleth)
Country-level climate comparison
🔹 Country Contribution
Donut chart showing distribution across countries
🔹 Country Benchmark
Top countries ranking (bar chart)
🔹 Multi-Metric Comparison
Normalized comparison of:
Temperature
Rainfall
CO₂ emissions
Renewable energy
Forest area
🔹 Summary Statistics
Max / Avg / Min metrics
🔹 Indicator Highlights
Hottest country
Coolest country
Wettest country
Highest renewable energy country
🔹 Underlying Data
Full filtered dataset view
CSV download option
🏗️ Tech Stack
Category	Tools
Language	Python
Data Processing	Pandas, NumPy
Visualization	Plotly
Dashboard	Streamlit
Modeling	Scikit-learn (basic trend)
Time Analysis	NumPy / Polynomial Fit
📁 Project Structure
Climate-Trend-Analyzer/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── climate_cleaned.csv
│
├── src/
│   ├── preprocess.py
│   └── analysis.py
│
├── app/
│   └── streamlit_app.py
│
├── outputs/
│   ├── charts/
│   ├── tables/
│   └── reports/
│
├── notebooks/
│
├── README.md
├── requirements.txt
└── main.py
⚙️ Installation
1. Clone repository
git clone https://github.com/yourusername/climate-trend-analyzer-dashboard.git
cd climate-trend-analyzer-dashboard
2. Create virtual environment

Windows

python -m venv venv
venv\Scripts\activate

Mac/Linux

python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
▶️ Run the Project
Step 1: Process data
python main.py
Step 2: Launch dashboard
streamlit run app/streamlit_app.py

Open in browser:

http://localhost:8501
📊 Sample Outputs
📈 Trend Analysis
Year-wise temperature changes
Trendline showing long-term direction
🌍 Map View
Country-level climate metric visualization
🧠 Insights
Top performing country
Peak climate year
Trend direction
📸 Screenshots
/images/
   dashboard_overview.png
   trend_chart.png
   map_view.png
   benchmark.png

![Dashboard](images/dashboard_overview.png)
