# ---------------------------------------------------------
# File: health_dashboard_enterprise.py
# Professional Hospital Analytics Dashboard
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

# -------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Enterprise Healthcare Dashboard",
    layout="wide",
    page_icon="🏥"
)

# -------------- CUSTOM UI THEME --------------
st.markdown("""
<style>
/* General Layout */
.main { padding: 0rem 2rem; }

/* Header Banner */
header { visibility: hidden; }
#root > div:nth-child(1) > div > div > div > div {
    background: linear-gradient(90deg, #0059b3, #00a6ff);
    padding: 20px 20px !important;
    border-radius: 0 0 25px 25px;
}
h1 {
    color: white !important;
    font-weight: 700;
    letter-spacing: 0.4px;
    text-align: center;
}

/* Tabs Styling */
.stTabs [data-baseweb="tab"] {
    font-size: 17px;
    font-weight: 650;
    border-radius: 12px;
    background-color: #f2f8ff;
    color: #004c99;
    padding: 10px 20px;
}
.stTabs [data-baseweb="tab"]:hover {
    background-color: #cfe7ff;
    color: #0066cc;
}

/* Metric Cards */
.metric-card {
    background: linear-gradient(135deg, #e8f2ff, #d6eaff);
    padding: 18px 20px;
    border-radius: 18px;
    text-align: center;
    font-weight: 600;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}
.metric-card h3 { color:#003d80; font-size:20px; }
.metric-card h2 { color:#001a33; font-size:28px; font-weight:700; }

/* Sidebar Branding */
.sidebar-card {
    background: linear-gradient(180deg, #0076e6, #00c6ff);
    padding:18px 15px;
    border-radius:14px;
    text-align:center;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# -------- TITLE ----------
st.title("🏥 Enterprise Healthcare Analytics Dashboard")

# --------- SIDEBAR FILTERS ----------
st.sidebar.markdown("""
<div class="sidebar-card">
<h2>🏥 Health Analytics</h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.header("Filters")

DATA_PATH = "C:/Users/Usman/Desktop/Data Science project/healthcare_dataset.csv"
df = pd.read_csv(DATA_PATH)

df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Month'] = df['Date of Admission'].dt.month
df['Year'] = df['Date of Admission'].dt.year

selected_year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))
filtered_df = df[df['Year'] == selected_year]

hospitals = ['All'] + list(df['Hospital'].unique())
selected_hospital = st.sidebar.selectbox("Select Hospital", hospitals)
if selected_hospital != 'All':
    filtered_df = filtered_df[df['Hospital'] == selected_hospital]

diseases = ['All'] + list(df['Medical Condition'].unique())
selected_disease = st.sidebar.selectbox("Select Disease", diseases)
if selected_disease != 'All':
    filtered_df = filtered_df[df['Medical Condition'] == selected_disease]

# ----------- TABS -----------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Key Metrics",
    "📈 Trends",
    "👥 Gender Analysis",
    "🏥 Hospital Summary",
    "🔮 Seasonality & Forecast"
])

# -------- TAB 1: KEY METRICS ----------
with tab1:
    st.markdown("### 📌 Executive Overview")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <h3>🧑‍⚕️ Total Patients</h3>
        <h2>{len(filtered_df)}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
        <h3>🦠 Diseases Tracked</h3>
        <h2>{filtered_df['Medical Condition'].nunique()}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
        <h3>🏥 Hospitals Covered</h3>
        <h2>{filtered_df['Hospital'].nunique()}</h2>
        </div>
        """, unsafe_allow_html=True)


# -------- TAB 2: MONTHLY TREND ----------
with tab2:
    st.markdown("### 📈 Monthly Patient Trend")
    monthly_count = filtered_df.groupby('Month').size().reset_index(name='Patients')
    fig = px.line(monthly_count, x='Month', y='Patients', markers=True,
                  title="Trend of Patients")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📌 Disease-wise Peak Month")
    disease_monthly = filtered_df.groupby(['Medical Condition', 'Month']).size().reset_index(name='Patients')
    peak_months = disease_monthly.loc[disease_monthly.groupby('Medical Condition')['Patients'].idxmax()]
    st.dataframe(peak_months)


# -------- TAB 3: GENDER ANALYSIS ----------
with tab3:
    st.markdown("### 👥 Gender Wise Month Distribution")
    gender_month = filtered_df.groupby(['Month', 'Gender']).size().reset_index(name='Patients')
    fig2 = px.bar(gender_month, x='Month', y='Patients', color='Gender', barmode='group')
    st.plotly_chart(fig2, use_container_width=True)


# -------- TAB 4: HOSPITAL SUMMARY ----------
with tab4:
    st.markdown("### 🏥 Hospital Patient Load")
    hospital_count = filtered_df.groupby('Hospital').size().reset_index(name='Patients').sort_values(by='Patients', ascending=False)
    fig3 = px.bar(hospital_count, x='Hospital', y='Patients', text='Patients')
    st.plotly_chart(fig3, use_container_width=True)
    st.dataframe(hospital_count)


# -------- TAB 5: SEASONALITY + FORECAST ----------
with tab5:
    st.markdown("### 🔮 Seasonality & Future Forecasting")

    if selected_disease != 'All':
        disease_df = df[df['Medical Condition'] == selected_disease]
        ts = disease_df.groupby('Date of Admission').size().reset_index(name='Patients')
        ts.rename(columns={'Date of Admission': 'ds', 'Patients': 'y'}, inplace=True)

        if len(ts) > 20:
            # Seasonality
            ts['Month'] = ts['ds'].dt.month
            seasonality = ts.groupby('Month')['y'].sum().reset_index()
            fig4 = px.bar(seasonality, x='Month', y='y', title=f"Seasonality - High Risk Months")
            st.plotly_chart(fig4, use_container_width=True)

            # Forecast
            model = Prophet(yearly_seasonality=True)
            model.fit(ts)
            future = model.make_future_dataframe(periods=180)
            forecast = model.predict(future)

            st.markdown("### 📊 6 Month Forecast")
           # st.pyplot(model.plot(forecast))
        else:
            st.warning("Not enough past records to forecast.")
    else:
        st.info("Select a specific disease for forecasting view.")


# -------- FOOTER ----------
st.markdown("---")
st.markdown("✔ Designed by Usman, Rizwan, Azra soomro and Mahnoor Memon")

