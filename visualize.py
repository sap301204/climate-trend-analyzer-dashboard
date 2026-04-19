import os
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import CHARTS_DIR

def plot_temperature_trend(yearly_df):
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_df["year"], yearly_df["avg_temp_c"], marker="o")
    plt.title("Average Temperature Trend")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    path = os.path.join(CHARTS_DIR, "temperature_trend.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

def plot_rainfall_trend(yearly_df):
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_df["year"], yearly_df["rainfall_mm"], marker="o")
    plt.title("Rainfall Trend")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (mm)")
    plt.grid(True)
    path = os.path.join(CHARTS_DIR, "rainfall_trend.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

def plot_seasonal_pattern(df):
    # Since the dataset is annual country-level data, use country comparison instead of fake seasonality
    country_df = (
        df.groupby("country", as_index=False)["avg_temp_c"]
        .mean()
        .sort_values("avg_temp_c", ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(data=country_df, x="country", y="avg_temp_c")
    plt.title("Top 10 Countries by Average Temperature")
    plt.xlabel("Country")
    plt.ylabel("Average Temperature (°C)")
    plt.xticks(rotation=45)
    path = os.path.join(CHARTS_DIR, "seasonal_pattern.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

def plot_anomaly(df):
    plt.figure(figsize=(12, 6))
    plt.scatter(df["year"], df["avg_temp_c"], alpha=0.6, label="Normal")
    anomaly_df = df[df["is_anomaly"] == True]
    plt.scatter(anomaly_df["year"], anomaly_df["avg_temp_c"], label="Anomaly")
    plt.title("Temperature Anomaly Plot")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.legend()
    plt.grid(True)
    path = os.path.join(CHARTS_DIR, "anomaly_plot.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

def plot_forecast(forecast_df):
    plt.figure(figsize=(12, 6))

    hist = forecast_df[forecast_df["type"] == "historical"]
    future = forecast_df[forecast_df["type"] == "forecast"]

    plt.plot(hist["year"], hist["avg_temp_c"], marker="o", label="Historical")
    plt.plot(future["year"], future["avg_temp_c"], marker="o", linestyle="--", label="Forecast")

    plt.title("Temperature Forecast")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.legend()
    plt.grid(True)
    path = os.path.join(CHARTS_DIR, "forecast_plot.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

def plot_correlation_heatmap(df):
    cols = [
        "avg_temp_c", "rainfall_mm", "co2_emissions",
        "sea_level_rise_mm", "population",
        "renewable_energy_pct", "extreme_weather_events", "forest_area_pct"
    ]
    corr = df[cols].corr()

    plt.figure(figsize=(10, 7))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    path = os.path.join(CHARTS_DIR, "correlation_heatmap.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path