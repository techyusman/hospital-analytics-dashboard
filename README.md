# hospital-analytics-dashboard
A professional Streamlit-based hospital analytics platform for visualizing patient demographics, billing data, and medical outcomes using Python and Plotly.

# Hospital Analytics Enterprise Dashboard

A professional-grade analytics platform designed to provide hospital administrators and healthcare providers with actionable insights into patient data, medical conditions, and financial performance.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Data Analysis Logic](#data-analysis-logic)
- [Dataset Description](#dataset-description)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## 🔍 Project Overview
The **Hospital Analytics Enterprise Dashboard** is a data science project that transforms raw healthcare records into interactive visualizations. It enables users to analyze patient demographics, track common medical conditions (like Cancer and Obesity), and monitor billing amounts across different insurance providers.

## ✨ Key Features
- **Dynamic Demographics:** Interactive analysis of patient Age and Gender distributions.
- **Medical Condition Insights:** Visual tracking of common diagnoses and treatment outcomes.
- **Financial Analytics:** Comprehensive review of billing amounts categorized by insurance providers (e.g., Medicare, Aetna, Cigna).
- **Operational Monitoring:** Real-time data on admission types (Urgent, Emergency, Elective) and hospital room occupancy.

## 📊 Data Analysis Logic
The project script (`health_dashboard.py`) follows a professional hospital management workflow:
1. **Data Ingestion:** Loads patient records from `healthcare_dataset.csv`.
2. **Patient Tracking:** Monitors dates of admission and discharge to calculate hospital throughput.
3. **Medical Outcome Analysis:** Evaluates test results (Normal, Abnormal, Inconclusive) against specific medical conditions.
4. **Billing Audits:** Summarizes financial data to identify billing trends across various healthcare facilities.

## 📂 Dataset Description
The system utilizes a structured CSV dataset containing:
- **Patient Identifiers:** Name, Age, Gender, and Blood Type.
- **Clinical Data:** Medical Condition, Doctor, Medication, and Test Results.
- **Administrative Data:** Hospital name, Admission Type, and Room Number.
- **Financial Data:** Insurance Provider and Billing Amount.

## 🚀 Installation & Setup
