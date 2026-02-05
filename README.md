# Professional Hospital Analytics Dashboard

This enterprise-grade analytics platform is designed for healthcare administrators and clinical researchers to visualize complex patient data, monitor financial trends, and evaluate medical outcomes.

## 🚀 Project Overview
The dashboard processes a comprehensive healthcare dataset to provide interactive visualizations. It enables stakeholders to track hospital performance, patient demographics, and the effectiveness of medical treatments across various conditions.

## ✨ Key Features
- **Patient Demographics:** Granular analysis of Age, Gender, and Blood Type distributions.
- **Clinical Performance:** Visualization of test results (Normal, Abnormal, Inconclusive) and medical conditions like Cancer, Obesity, and Diabetes.
- **Financial Auditing:** Tracking of billing amounts and insurance provider performance (Medicare, Aetna, Cigna, etc.).
- **Operational Insights:** Monitoring of admission types (Urgent, Emergency, Elective) and room occupancy rates.
- **Medical Treatment Analysis:** Analysis of medication usage (e.g., Paracetamol, Ibuprofen, Aspirin) relative to discharge timelines.

## 🛠 Tech Stack
- **Dashboarding:** [Streamlit](https://streamlit.io/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **Visualizations:** [Plotly](https://plotly.com/) / Matplotlib
- **Programming:** Python 3.x

## 📂 Dataset Architecture
The system utilizes a structured `healthcare_dataset.csv` containing the following dimensions:
| Column | Description |
| :--- | :--- |
| `Name`, `Age`, `Gender` | Patient Identifiers |
| `Medical Condition` | Diagnoses (e.g., Asthma, Hypertension) |
| `Doctor`, `Hospital` | Provider Information |
| `Insurance Provider` | Financial Payers |
| `Billing Amount` | Transactional data |
| `Admission Type` | Priority (Urgent, Emergency, Elective) |
| `Test Results` | Clinical outcomes |

## ⚙️ Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone: https://github.com/techyusman/healthcare-analytics-dashboard.git

   Install Dependencies: pip install -r requirements.txt
   Launch the Dashboard: streamlit run health_dashboard.py


   Developer Name: Muhammad Usman Software Engineer
