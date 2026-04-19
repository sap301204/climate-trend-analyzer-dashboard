import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_temperature(yearly_df, years_ahead=5):
    yearly_df = yearly_df.copy()

    X = yearly_df[["year"]]
    y = yearly_df["avg_temp_c"]

    model = LinearRegression()
    model.fit(X, y)

    last_year = yearly_df["year"].max()
    future_years = pd.DataFrame({
        "year": list(range(last_year + 1, last_year + years_ahead + 1))
    })

    future_years["avg_temp_c"] = model.predict(future_years[["year"]])

    hist = yearly_df[["year", "avg_temp_c"]].copy()
    hist["type"] = "historical"

    future_years["type"] = "forecast"

    forecast_df = pd.concat([hist, future_years], ignore_index=True)
    return forecast_df