import pandas as pd
from src.config import PROCESSED_DATA_PATH


def clean_climate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize the raw climate dataset for downstream analysis
    and dashboard usage.
    """
    df = df.copy()

    # -----------------------------------------
    # Rename columns to code-friendly names
    # -----------------------------------------
    df = df.rename(columns={
        "Year": "year",
        "Country": "country",
        "Avg Temperature (°C)": "avg_temp_c",
        "CO2 Emissions (Tons/Capita)": "co2_emissions",
        "Sea Level Rise (mm)": "sea_level_rise_mm",
        "Rainfall (mm)": "rainfall_mm",
        "Population": "population",
        "Renewable Energy (%)": "renewable_energy_pct",
        "Extreme Weather Events": "extreme_weather_events",
        "Forest Area (%)": "forest_area_pct"
    })

    # -----------------------------------------
    # Standardize country names
    # -----------------------------------------
    df["country"] = df["country"].astype(str).str.strip()

    country_fix = {
        "USA": "United States",
        "US": "United States",
        "U.S.A.": "United States",
        "UK": "United Kingdom",
        "U.K.": "United Kingdom",
        "UAE": "United Arab Emirates",
        "Korea, South": "South Korea",
        "Republic of Korea": "South Korea",
        "Russian Federation": "Russia"
    }
    df["country"] = df["country"].replace(country_fix)

    # -----------------------------------------
    # Convert numeric columns safely
    # -----------------------------------------
    numeric_cols = [
        "year",
        "avg_temp_c",
        "co2_emissions",
        "sea_level_rise_mm",
        "rainfall_mm",
        "population",
        "renewable_energy_pct",
        "extreme_weather_events",
        "forest_area_pct"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # -----------------------------------------
    # Remove duplicates
    # -----------------------------------------
    df = df.drop_duplicates()

    # -----------------------------------------
    # Drop rows missing critical fields
    # -----------------------------------------
    df = df.dropna(subset=["year", "country", "avg_temp_c", "rainfall_mm"])

    # -----------------------------------------
    # Fill remaining missing numeric values
    # -----------------------------------------
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # -----------------------------------------
    # Basic validity rules / clipping
    # -----------------------------------------
    df["avg_temp_c"] = df["avg_temp_c"].clip(-50, 60)
    df["rainfall_mm"] = df["rainfall_mm"].clip(lower=0)
    df["co2_emissions"] = df["co2_emissions"].clip(lower=0)
    df["sea_level_rise_mm"] = df["sea_level_rise_mm"].clip(lower=0)
    df["population"] = df["population"].clip(lower=0)
    df["renewable_energy_pct"] = df["renewable_energy_pct"].clip(0, 100)
    df["forest_area_pct"] = df["forest_area_pct"].clip(0, 100)
    df["extreme_weather_events"] = df["extreme_weather_events"].clip(lower=0)

    # -----------------------------------------
    # Final type cleanup
    # -----------------------------------------
    df["year"] = df["year"].astype(int)
    df["extreme_weather_events"] = df["extreme_weather_events"].round().astype(int)

    # -----------------------------------------
    # Sort for clean downstream visuals
    # -----------------------------------------
    df = df.sort_values(["country", "year"]).reset_index(drop=True)

    return df


def save_cleaned_data(df: pd.DataFrame, path: str = PROCESSED_DATA_PATH) -> None:
    """
    Save cleaned climate data to processed folder.
    """
    df.to_csv(path, index=False)