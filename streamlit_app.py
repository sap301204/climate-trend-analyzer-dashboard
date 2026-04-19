import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "climate_cleaned.csv")

st.set_page_config(
    page_title="Climate Trend Analyzer",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# Futuristic Dashboard CSS
# ---------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(circle at 20% 20%, rgba(59,130,246,0.18), transparent 22%),
            radial-gradient(circle at 80% 15%, rgba(139,92,246,0.14), transparent 25%),
            radial-gradient(circle at 60% 75%, rgba(34,211,238,0.08), transparent 18%),
            linear-gradient(135deg, #060b1f 0%, #0b1026 50%, #0f1535 100%);
        color: #f8fafc;
    }

    .block-container {
        padding-top: 0.7rem;
        padding-bottom: 1.2rem;
        padding-left: 1.1rem;
        padding-right: 1.1rem;
        max-width: 100%;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1028 0%, #111a3d 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
        min-width: 300px !important;
        max-width: 300px !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 0.8rem;
        padding-left: 0.85rem;
        padding-right: 0.85rem;
        padding-bottom: 0.8rem;
    }

    .brand-card {
        background: linear-gradient(135deg, rgba(20,31,72,0.95), rgba(14,22,55,0.95));
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 15px 14px;
        margin-bottom: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.22);
    }

    .brand-title {
        font-size: 1rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.25rem;
    }

    .brand-subtitle {
        font-size: 0.82rem;
        color: #a5b4fc;
        line-height: 1.5;
    }

    .side-card {
        background: linear-gradient(135deg, rgba(18,28,66,0.95), rgba(12,20,52,0.95));
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 13px 12px;
        margin-bottom: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    }

    .side-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.2rem;
    }

    .side-text {
        font-size: 0.8rem;
        color: #94a3b8;
        line-height: 1.45;
    }

    .hero-shell {
        background:
            radial-gradient(circle at 70% 50%, rgba(59,130,246,0.20), transparent 22%),
            linear-gradient(135deg, rgba(18,28,66,0.95), rgba(11,17,40,0.94));
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 20px;
        padding: 18px 18px;
        margin-bottom: 14px;
        box-shadow: 0 14px 38px rgba(0,0,0,0.22);
    }

    .hero-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.3rem;
    }

    .hero-subtitle {
        font-size: 0.9rem;
        color: #cbd5e1;
        line-height: 1.6;
    }

    .panel-card {
        background: linear-gradient(135deg, rgba(14,22,55,0.96), rgba(10,16,40,0.96));
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 18px;
        padding: 14px 14px 10px 14px;
        margin-bottom: 14px;
        box-shadow: 0 10px 26px rgba(0,0,0,0.18);
    }

    .panel-title {
        font-size: 1rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.15rem;
    }

    .panel-subtitle {
        font-size: 0.82rem;
        color: #94a3b8;
        margin-bottom: 0.7rem;
    }

    .kpi-card {
        background:
            linear-gradient(135deg, rgba(20,31,72,0.96), rgba(13,21,52,0.96));
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 15px 15px;
        min-height: 100px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.16);
    }

    .kpi-label {
        font-size: 0.78rem;
        color: #93c5fd;
        margin-bottom: 0.35rem;
    }

    .kpi-value {
        font-size: 1.75rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.15;
    }

    .kpi-note {
        font-size: 0.75rem;
        color: #94a3b8;
        margin-top: 0.35rem;
    }

    .insight-card {
        background: linear-gradient(135deg, rgba(19,29,69,0.95), rgba(12,20,52,0.95));
        border-left: 4px solid #38bdf8;
        border-radius: 14px;
        padding: 12px 12px;
        min-height: 90px;
    }

    .insight-heading {
        font-size: 0.72rem;
        color: #67e8f9;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .insight-value {
        font-size: 1rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.2rem;
    }

    .insight-text {
        font-size: 0.79rem;
        color: #a5b4fc;
        line-height: 1.4;
    }

    .footer-strip {
        margin-top: 8px;
        padding: 12px 14px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(18,28,66,0.95), rgba(11,17,40,0.95));
        border: 1px solid rgba(255,255,255,0.05);
        color: #94a3b8;
        font-size: 0.83rem;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    div[data-baseweb="select"] > div {
        background-color: #0b1432 !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
    }

    div[data-baseweb="tag"] {
        background-color: #2563eb !important;
        border-radius: 8px !important;
    }

    .stDownloadButton button {
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.55rem 0.95rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Metadata
# ---------------------------------------------------
metric_labels = {
    "avg_temp_c": "Average Temperature (°C)",
    "rainfall_mm": "Average Rainfall (mm)",
    "co2_emissions": "Carbon Emissions Intensity",
    "sea_level_rise_mm": "Sea Level Rise (mm)",
    "renewable_energy_pct": "Renewable Energy Share (%)",
    "extreme_weather_events": "Extreme Weather Event Count",
    "forest_area_pct": "Forest Coverage (%)"
}

metric_units = {
    "avg_temp_c": "°C",
    "rainfall_mm": "mm",
    "co2_emissions": "",
    "sea_level_rise_mm": "mm",
    "renewable_energy_pct": "%",
    "extreme_weather_events": "",
    "forest_area_pct": "%"
}

metric_colors = {
    "avg_temp_c": "#f59e0b",
    "rainfall_mm": "#38bdf8",
    "co2_emissions": "#ef4444",
    "sea_level_rise_mm": "#06b6d4",
    "renewable_energy_pct": "#22c55e",
    "extreme_weather_events": "#f97316",
    "forest_area_pct": "#84cc16"
}

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

# ---------------------------------------------------
# Helpers
# ---------------------------------------------------
def styled_kpi(label, value, note):
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-note">{note}</div>
    </div>
    """

def format_value(value, metric):
    unit = metric_units.get(metric, "")
    if metric == "extreme_weather_events":
        return f"{int(round(value))}{unit}"
    elif metric == "rainfall_mm":
        return f"{value:.1f} {unit}".strip()
    else:
        return f"{value:.2f}{unit}"

def trend_direction(years, values):
    if len(years) < 2:
        return "Stable", 0.0
    slope = np.polyfit(years, values, 1)[0]
    if slope > 0.01:
        return "Upward", slope
    elif slope < -0.01:
        return "Downward", slope
    return "Stable", slope

def top_country(df, metric, ascending=False):
    temp = df.groupby("country", as_index=False)[metric].mean().sort_values(metric, ascending=ascending)
    return temp.iloc[0]["country"], temp.iloc[0][metric]

def top_year(df, metric, ascending=False):
    temp = df.groupby("year", as_index=False)[metric].mean().sort_values(metric, ascending=ascending)
    return int(temp.iloc[0]["year"]), temp.iloc[0][metric]

def page_header(title, subtitle):
    st.markdown(f"""
    <div class="hero-shell">
        <div class="hero-title">{title}</div>
        <div class="hero-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def section_header(title, subtitle):
    st.markdown(f"""
    <div class="panel-card">
        <div class="panel-title">{title}</div>
        <div class="panel-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
if not os.path.exists(CLEANED_DATA_PATH):
    st.warning("Processed data not found. Please run main.py first.")
    st.stop()

df = pd.read_csv(CLEANED_DATA_PATH)
df["country"] = df["country"].astype(str).str.strip().replace(country_fix)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.markdown("""
<div class="brand-card">
    <div class="brand-title">🌍 Climate Vision UI</div>
    <div class="brand-subtitle">
        Advanced climate intelligence dashboard inspired by modern analytics product design.
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="side-card">
    <div class="side-title">Filters</div>
    <div class="side-text">
        Apply country, year, and metric filters to update every panel in the dashboard.
    </div>
</div>
""", unsafe_allow_html=True)

countries = sorted(df["country"].dropna().unique().tolist())
selected_countries = st.sidebar.multiselect(
    "Select Country/Countries",
    options=countries,
    default=countries[:6] if len(countries) >= 6 else countries
)

min_year = int(df["year"].min())
max_year = int(df["year"].max())

selected_year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

metric = st.sidebar.selectbox(
    "Select Climate Metric",
    list(metric_labels.keys()),
    format_func=lambda x: metric_labels[x]
)

st.sidebar.markdown("""
<div class="side-card">
    <div class="side-title">Navigation</div>
    <div class="side-text">
        Switch across major dashboard modules like a modern analytics app.
    </div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Go to Section",
    [
        "Overview",
        "Trend Analytics",
        "Geographic Intelligence",
        "Country Contribution",
        "Country Benchmark",
        "Multi-Metric Comparison",
        "Summary Statistics",
        "Indicator Highlights",
        "Underlying Records"
    ]
)

# ---------------------------------------------------
# Filter
# ---------------------------------------------------
filtered_df = df[
    (df["year"] >= selected_year_range[0]) &
    (df["year"] <= selected_year_range[1])
]

if selected_countries:
    filtered_df = filtered_df[filtered_df["country"].isin(selected_countries)]

if filtered_df.empty:
    st.error("No data available for the selected filters.")
    st.stop()

yearly_df = filtered_df.groupby("year", as_index=False)[metric].mean()
direction, slope = trend_direction(yearly_df["year"].values, yearly_df[metric].values)

metric_avg = filtered_df[metric].mean()
metric_max_country, metric_max_value = top_country(filtered_df, metric, ascending=False)
metric_min_country, metric_min_value = top_country(filtered_df, metric, ascending=True)
metric_peak_year, metric_peak_value = top_year(filtered_df, metric, ascending=False)

coverage_text = f"{filtered_df['country'].nunique()} countries | {filtered_df['year'].min()}–{filtered_df['year'].max()} | {len(filtered_df)} records"

if direction == "Upward":
    executive_note = f"{metric_labels[metric]} is trending upward across the selected scope."
elif direction == "Downward":
    executive_note = f"{metric_labels[metric]} is trending downward across the selected scope."
else:
    executive_note = f"{metric_labels[metric]} remains relatively stable across the selected scope."

# ---------------------------------------------------
# OVERVIEW
# ---------------------------------------------------
if page == "Overview":
    page_header(
        "Climate Trend Analyzer Dashboard",
        f"Executive view: {executive_note} Current average is {format_value(metric_avg, metric)}. "
        f"Top country is {metric_max_country}, peak year is {metric_peak_year}. Scope: {coverage_text}."
    )

    avg_temp = filtered_df["avg_temp_c"].mean()
    avg_rain = filtered_df["rainfall_mm"].mean()
    avg_co2 = filtered_df["co2_emissions"].mean()
    extreme_events = filtered_df["extreme_weather_events"].sum()

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(styled_kpi("Average Temperature", f"{avg_temp:.2f}°C", "Mean temperature across filtered records"), unsafe_allow_html=True)
    with k2:
        st.markdown(styled_kpi("Average Rainfall", f"{avg_rain:.1f} mm", "Average rainfall across filtered records"), unsafe_allow_html=True)
    with k3:
        st.markdown(styled_kpi("Average Carbon Emissions", f"{avg_co2:.2f}", "Mean emissions intensity across filtered records"), unsafe_allow_html=True)
    with k4:
        st.markdown(styled_kpi("Extreme Weather Events", f"{int(extreme_events)}", "Total event count across filtered records"), unsafe_allow_html=True)

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    i1, i2, i3, i4 = st.columns(4)
    with i1:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-heading">Top Country</div>
            <div class="insight-value">{metric_max_country}</div>
            <div class="insight-text">Highest value at {format_value(metric_max_value, metric)}.</div>
        </div>
        """, unsafe_allow_html=True)
    with i2:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-heading">Lowest Country</div>
            <div class="insight-value">{metric_min_country}</div>
            <div class="insight-text">Lowest value at {format_value(metric_min_value, metric)}.</div>
        </div>
        """, unsafe_allow_html=True)
    with i3:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-heading">Peak Year</div>
            <div class="insight-value">{metric_peak_year}</div>
            <div class="insight-text">Peak annual average reached {format_value(metric_peak_value, metric)}.</div>
        </div>
        """, unsafe_allow_html=True)
    with i4:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-heading">Trend Direction</div>
            <div class="insight-value">{direction}</div>
            <div class="insight-text">{executive_note}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3.1, 1.5], gap="large")

    with col1:
        section_header(
            "Trend Overview",
            f"Annual movement of {metric_labels[metric]} across selected countries and years."
        )

        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=yearly_df["year"],
            y=yearly_df[metric],
            mode="lines+markers",
            name=metric_labels[metric],
            line=dict(color=metric_colors[metric], width=3),
            marker=dict(size=7, color=metric_colors[metric]),
            fill="tozeroy",
            fillcolor="rgba(59,130,246,0.08)"
        ))

        if len(yearly_df) >= 3:
            z = np.polyfit(yearly_df["year"], yearly_df[metric], 1)
            trendline = np.poly1d(z)(yearly_df["year"])
            fig_trend.add_trace(go.Scatter(
                x=yearly_df["year"],
                y=trendline,
                mode="lines",
                name="Long-Term Trend",
                line=dict(color="#cbd5e1", width=2, dash="dash")
            ))

        fig_trend.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0d1536",
            plot_bgcolor="#0d1536",
            margin=dict(l=20, r=20, t=10, b=20),
            height=420,
            xaxis_title="Year",
            yaxis_title=metric_labels[metric],
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0)
        )
        st.plotly_chart(fig_trend, use_container_width=True)

    with col2:
        section_header(
            "Country Contribution",
            f"Relative contribution of {metric_labels[metric]} among leading countries."
        )

        country_metric = (
            filtered_df.groupby("country", as_index=False)[metric]
            .mean()
            .sort_values(metric, ascending=False)
        )

        donut_df = country_metric.head(5).copy()
        if len(country_metric) > 5:
            others_val = country_metric.iloc[5:][metric].sum()
            donut_df = pd.concat([
                donut_df,
                pd.DataFrame({"country": ["Others"], metric: [others_val]})
            ], ignore_index=True)

        fig_donut = px.pie(
            donut_df,
            names="country",
            values=metric,
            hole=0.72,
            color_discrete_sequence=["#3b82f6", "#06b6d4", "#8b5cf6", "#22c55e", "#f59e0b", "#64748b"]
        )

        fig_donut.update_traces(
            textinfo="percent",
            marker=dict(line=dict(color="#0d1536", width=2))
        )

        fig_donut.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0d1536",
            plot_bgcolor="#0d1536",
            height=420,
            margin=dict(l=10, r=10, t=10, b=10),
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, x=0)
        )
        st.plotly_chart(fig_donut, use_container_width=True)

# ---------------------------------------------------
# TREND ANALYTICS
# ---------------------------------------------------
elif page == "Trend Analytics":
    page_header(
        "Trend Analytics",
        f"Investigate the historical behavior and long-term direction of {metric_labels[metric]}."
    )

    section_header(
        "Historical Trend Analysis",
        f"Time-series view of {metric_labels[metric]} from {filtered_df['year'].min()} to {filtered_df['year'].max()}."
    )

    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=yearly_df["year"],
        y=yearly_df[metric],
        mode="lines+markers",
        name=metric_labels[metric],
        line=dict(color=metric_colors[metric], width=3),
        marker=dict(size=7, color=metric_colors[metric]),
        fill="tozeroy",
        fillcolor="rgba(59,130,246,0.08)"
    ))

    if len(yearly_df) >= 3:
        z = np.polyfit(yearly_df["year"], yearly_df[metric], 1)
        trendline = np.poly1d(z)(yearly_df["year"])
        fig_trend.add_trace(go.Scatter(
            x=yearly_df["year"],
            y=trendline,
            mode="lines",
            name="Long-Term Trend",
            line=dict(color="#cbd5e1", width=2, dash="dash")
        ))

    fig_trend.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1536",
        plot_bgcolor="#0d1536",
        margin=dict(l=20, r=20, t=10, b=20),
        height=540,
        xaxis_title="Year",
        yaxis_title=metric_labels[metric],
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0)
    )
    st.plotly_chart(fig_trend, use_container_width=True)

# ---------------------------------------------------
# GEOGRAPHIC INTELLIGENCE
# ---------------------------------------------------
elif page == "Geographic Intelligence":
    page_header(
        "Geographic Intelligence",
        f"Spatial distribution of {metric_labels[metric]} across countries in the selected scope."
    )

    section_header(
        "Geographic Distribution Map",
        "Country-level choropleth visualization."
    )

    map_df = filtered_df.groupby("country", as_index=False)[metric].mean()

    fig_map = px.choropleth(
        map_df,
        locations="country",
        locationmode="country names",
        color=metric,
        hover_name="country",
        color_continuous_scale="Blues",
        projection="natural earth"
    )

    fig_map.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1536",
        geo=dict(
            bgcolor="#0d1536",
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#64748b",
            showland=True,
            landcolor="#101a40"
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=580,
        coloraxis_colorbar=dict(title=metric_labels[metric])
    )

    st.plotly_chart(fig_map, use_container_width=True)

# ---------------------------------------------------
# COUNTRY CONTRIBUTION
# ---------------------------------------------------
elif page == "Country Contribution":
    page_header(
        "Country Contribution",
        f"See how the selected {metric_labels[metric].lower()} is distributed among leading countries."
    )

    section_header(
        "Contribution Breakdown",
        "Relative distribution among top contributing countries."
    )

    country_metric = (
        filtered_df.groupby("country", as_index=False)[metric]
        .mean()
        .sort_values(metric, ascending=False)
    )

    donut_df = country_metric.head(6).copy()

    fig_donut = px.pie(
        donut_df,
        names="country",
        values=metric,
        hole=0.72,
        color_discrete_sequence=["#3b82f6", "#06b6d4", "#8b5cf6", "#22c55e", "#f59e0b", "#64748b"]
    )

    fig_donut.update_traces(
        textinfo="percent+label",
        marker=dict(line=dict(color="#0d1536", width=2))
    )

    fig_donut.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1536",
        plot_bgcolor="#0d1536",
        height=560,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=-0.12, x=0)
    )
    st.plotly_chart(fig_donut, use_container_width=True)

# ---------------------------------------------------
# COUNTRY BENCHMARK
# ---------------------------------------------------
elif page == "Country Benchmark":
    page_header(
        "Country Benchmark",
        f"Benchmark the strongest countries for {metric_labels[metric]}."
    )

    section_header(
        "Top Country Ranking",
        "Top 10 country comparison based on filtered average values."
    )

    top_country_df = (
        filtered_df.groupby("country", as_index=False)[metric]
        .mean()
        .sort_values(metric, ascending=False)
        .head(10)
    )

    fig_bar = px.bar(
        top_country_df,
        x=metric,
        y="country",
        orientation="h",
        color=metric,
        color_continuous_scale="Blues"
    )

    fig_bar.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1536",
        plot_bgcolor="#0d1536",
        margin=dict(l=20, r=20, t=10, b=20),
        height=560,
        xaxis_title=metric_labels[metric],
        yaxis_title="Country",
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------------------------------------
# MULTI-METRIC COMPARISON
# ---------------------------------------------------
elif page == "Multi-Metric Comparison":
    page_header(
        "Multi-Metric Comparison",
        "Compare major environmental indicators on a normalized scale."
    )

    section_header(
        "Normalized Environmental Benchmark",
        "Cross-metric benchmarking for the currently filtered selection."
    )

    benchmark_df = pd.DataFrame({
        "Metric": [
            "Average Temperature",
            "Average Rainfall",
            "Carbon Emissions",
            "Renewable Energy Share",
            "Forest Coverage"
        ],
        "Value": [
            filtered_df["avg_temp_c"].mean(),
            filtered_df["rainfall_mm"].mean(),
            filtered_df["co2_emissions"].mean(),
            filtered_df["renewable_energy_pct"].mean(),
            filtered_df["forest_area_pct"].mean()
        ]
    })

    benchmark_df["Normalized Score"] = benchmark_df["Value"] / benchmark_df["Value"].max() * 100

    fig_benchmark = px.bar(
        benchmark_df,
        x="Normalized Score",
        y="Metric",
        orientation="h",
        color="Normalized Score",
        color_continuous_scale="Tealgrn"
    )

    fig_benchmark.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1536",
        plot_bgcolor="#0d1536",
        margin=dict(l=20, r=20, t=10, b=20),
        height=560,
        xaxis_title="Normalized Score",
        yaxis_title="Metric",
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_benchmark, use_container_width=True)

# ---------------------------------------------------
# SUMMARY STATISTICS
# ---------------------------------------------------
elif page == "Summary Statistics":
    page_header(
        "Summary Statistics",
        "Maximum, average, and minimum values across the filtered dataset."
    )

    section_header(
        "Statistical Summary",
        "High-level aggregated metric view."
    )

    summary_table = pd.DataFrame({
        "Metric": [
            "Average Temperature (°C)",
            "Average Rainfall (mm)",
            "Carbon Emissions Intensity",
            "Renewable Energy Share (%)",
            "Extreme Weather Event Count"
        ],
        "Maximum": [
            round(filtered_df["avg_temp_c"].max(), 2),
            round(filtered_df["rainfall_mm"].max(), 2),
            round(filtered_df["co2_emissions"].max(), 2),
            round(filtered_df["renewable_energy_pct"].max(), 2),
            int(filtered_df["extreme_weather_events"].max())
        ],
        "Average": [
            round(filtered_df["avg_temp_c"].mean(), 2),
            round(filtered_df["rainfall_mm"].mean(), 2),
            round(filtered_df["co2_emissions"].mean(), 2),
            round(filtered_df["renewable_energy_pct"].mean(), 2),
            round(filtered_df["extreme_weather_events"].mean(), 2)
        ],
        "Minimum": [
            round(filtered_df["avg_temp_c"].min(), 2),
            round(filtered_df["rainfall_mm"].min(), 2),
            round(filtered_df["co2_emissions"].min(), 2),
            round(filtered_df["renewable_energy_pct"].min(), 2),
            int(filtered_df["extreme_weather_events"].min())
        ]
    })

    st.dataframe(summary_table, use_container_width=True, height=560)

# ---------------------------------------------------
# INDICATOR HIGHLIGHTS
# ---------------------------------------------------
elif page == "Indicator Highlights":
    page_header(
        "Indicator Highlights",
        "Country-level climate highlights derived from the filtered scope."
    )

    hottest_country, hottest_val = top_country(filtered_df, "avg_temp_c", ascending=False)
    coolest_country, coolest_val = top_country(filtered_df, "avg_temp_c", ascending=True)
    wettest_country, wettest_val = top_country(filtered_df, "rainfall_mm", ascending=False)
    greenest_country, greenest_val = top_country(filtered_df, "renewable_energy_pct", ascending=False)

    climate_info = pd.DataFrame({
        "Indicator": [
            "Hottest Country",
            "Coolest Country",
            "Wettest Country",
            "Highest Renewable Share Country"
        ],
        "Current Selection": [
            hottest_country,
            coolest_country,
            wettest_country,
            greenest_country
        ],
        "Metric Value": [
            f"{hottest_val:.2f}",
            f"{coolest_val:.2f}",
            f"{wettest_val:.2f}",
            f"{greenest_val:.2f}"
        ]
    })

    section_header(
        "Climate Highlights",
        "High-level country highlights across selected indicators."
    )

    st.dataframe(climate_info, use_container_width=True, height=560)

# ---------------------------------------------------
# UNDERLYING RECORDS
# ---------------------------------------------------
elif page == "Underlying Records":
    page_header(
        "Underlying Records",
        "Filtered dataset rows currently driving all dashboard visuals and summaries."
    )

    preview_cols = [
        "year", "country", "avg_temp_c", "rainfall_mm",
        "co2_emissions", "sea_level_rise_mm",
        "renewable_energy_pct", "extreme_weather_events", "forest_area_pct"
    ]

    section_header(
        "Filtered Data Preview",
        "Detailed record-level view of the current filtered dataset."
    )

    st.dataframe(filtered_df[preview_cols], use_container_width=True, height=560)

    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_climate_data.csv",
        mime="text/csv"
    )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("""
<div class="footer-strip">
Built with Streamlit, Plotly, and Python using your uploaded climate dataset. Styled as a futuristic analytics dashboard with modular navigation and executive-level presentation.
</div>
""", unsafe_allow_html=True)