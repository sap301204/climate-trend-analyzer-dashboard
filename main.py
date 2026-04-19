import os
from src.data_loader import load_climate_data
from src.preprocess import clean_climate_data, save_cleaned_data
from src.trend_analysis import yearly_summary, compute_linear_trend
from src.anomaly_detection import detect_temperature_anomalies, detect_rainfall_anomalies, combine_anomalies
from src.forecasting import forecast_temperature
from src.visualize import (
    plot_temperature_trend,
    plot_rainfall_trend,
    plot_seasonal_pattern,
    plot_anomaly,
    plot_forecast,
    plot_correlation_heatmap
)
from src.report import generate_summary_report
from src.config import TABLES_DIR

def main():
    print("Loading raw climate data...")
    df = load_climate_data()

    print("Cleaning and standardizing dataset...")
    clean_df = clean_climate_data(df)
    save_cleaned_data(clean_df)

    print("Generating yearly summary...")
    yearly_df = yearly_summary(clean_df)
    yearly_df.to_csv(os.path.join(TABLES_DIR, "yearly_summary.csv"), index=False)

    print("Computing long-term trends...")
    temp_trend_result = compute_linear_trend(yearly_df, "avg_temp_c")
    rain_trend_result = compute_linear_trend(yearly_df, "rainfall_mm")

    print("Detecting anomalies...")
    anomaly_df = detect_temperature_anomalies(clean_df)
    anomaly_df = detect_rainfall_anomalies(anomaly_df)
    anomaly_df = combine_anomalies(anomaly_df)

    anomalies_only = anomaly_df[anomaly_df["is_anomaly"] == True]
    anomalies_only.to_csv(os.path.join(TABLES_DIR, "anomalies.csv"), index=False)

    print("Forecasting future temperature trend...")
    forecast_df = forecast_temperature(yearly_df, years_ahead=5)

    print("Generating charts...")
    plot_temperature_trend(yearly_df)
    plot_rainfall_trend(yearly_df)
    plot_seasonal_pattern(clean_df)
    plot_anomaly(anomaly_df)
    plot_forecast(forecast_df)
    plot_correlation_heatmap(clean_df)

    print("Generating summary report...")
    generate_summary_report(
        temp_slope=temp_trend_result["slope"],
        rain_slope=rain_trend_result["slope"],
        anomaly_count=len(anomalies_only)
    )

    print("\nClimate Trend Analyzer pipeline completed successfully.")
    print("Generated files:")
    print("- data/processed/climate_cleaned.csv")
    print("- outputs/charts/temperature_trend.png")
    print("- outputs/charts/rainfall_trend.png")
    print("- outputs/charts/seasonal_pattern.png")
    print("- outputs/charts/anomaly_plot.png")
    print("- outputs/charts/forecast_plot.png")
    print("- outputs/charts/correlation_heatmap.png")
    print("- outputs/reports/summary_report.txt")
    print("- outputs/tables/yearly_summary.csv")
    print("- outputs/tables/anomalies.csv")

if __name__ == "__main__":
    main()