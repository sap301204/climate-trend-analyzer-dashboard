import pandas as pd
from sklearn.linear_model import LinearRegression

def yearly_summary(df):
    yearly = df.groupby("year", as_index=False).agg({
        "avg_temp_c": "mean",
        "rainfall_mm": "mean",
        "co2_emissions": "mean",
        "sea_level_rise_mm": "mean",
        "population": "mean",
        "renewable_energy_pct": "mean",
        "extreme_weather_events": "mean",
        "forest_area_pct": "mean"
    })
    return yearly

def country_summary(df):
    country = df.groupby("country", as_index=False).agg({
        "avg_temp_c": "mean",
        "rainfall_mm": "mean",
        "co2_emissions": "mean",
        "sea_level_rise_mm": "mean"
    })
    return country

def compute_linear_trend(yearly_df, target_col):
    X = yearly_df[["year"]]
    y = yearly_df[target_col]

    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0]
    intercept = model.intercept_

    yearly_df = yearly_df.copy()
    yearly_df[f"{target_col}_trend"] = model.predict(X)

    return {
        "yearly_df": yearly_df,
        "slope": slope,
        "intercept": intercept,
        "model": model
    }

def correlation_summary(df):
    cols = [
        "avg_temp_c", "rainfall_mm", "co2_emissions",
        "sea_level_rise_mm", "population",
        "renewable_energy_pct", "extreme_weather_events", "forest_area_pct"
    ]
    return df[cols].corr()