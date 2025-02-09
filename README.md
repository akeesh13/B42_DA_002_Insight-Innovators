# **📊 Caste-Based Crime Dashboard**  

## **🔍 Introduction**  
This project provides an **interactive dashboard** to analyze **caste-based crimes in India** from **2001 to 2013**. It helps users explore crime trends using **data visualizations, filters, and sliders**.  

📌 **Key Objectives:**  
- Perform **Exploratory Data Analysis (EDA)** on caste-based crimes.  
- Create **visualizations** to uncover trends over the years.  
- Build an **interactive Streamlit dashboard** for real-time insights.  

---

## **📂 Project Type**  
✅ **Backend:** Data Processing & EDA (Python, Pandas)  
✅ **Frontend:** Streamlit Dashboard  

---

## **🚀 Deployed App**  
🌐 **Streamlit Dashboard:** [Live Dashboard](https://b42da002insight-innovators-j8xxixczy6up8gkueqtj5q.streamlit.app/)  

---

## **📂 Directory Structure**  
```
caste-crime-dashboard/
├─ backend/               # Data Processing & EDA
│  ├─ data_cleaning.py    # Data cleaning scripts
│  ├─ analysis.py         # Exploratory Data Analysis (EDA)
├─ frontend/              # Streamlit Dashboard
│  ├─ Streamlit_App.py    # Main Streamlit app
│  ├─ components/         # UI Components
│  ├─ assets/             # Images & static files
├─ dataset/               # Crime dataset
│  ├─ cleaned_rt.csv      # Cleaned data
├─ README.md              # Documentation
├─ requirements.txt       # Dependencies
```

## **⚡ Features**  
✔ **Interactive Filters & Sliders** to explore crime data  
✔ **Year-wise Analysis (2001-2013)** 📆  
✔ **Dynamic Charts (Line plots, Bar charts, Heatmaps, etc.)** 📊  
✔ **State & District-Level Crime Trends** 🗺️  
✔ **Deployed on Streamlit Cloud** 🌐  

---

## **📌 Design Decisions & Assumptions**  
1️⃣ **Data Aggregation:** Grouped data at the **state level** to provide an overview.  
2️⃣ **Filtering Mechanism:** Users can **filter by state, district, and year**.  
3️⃣ **Visualization Types:** Line plots for **trends**, bar charts for **comparisons**, heatmaps for **correlation analysis**.  

---

## **⚙️ Installation & Getting Started**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/caste-crime-dashboard.git
cd caste-crime-dashboard
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit Application**  
```bash
streamlit run Streamlit.py
```
💡 **Once running, open the displayed URL in your browser (e.g., `http://localhost:8501/`).**  

---

## **📌 Usage**  
To explore the crime data:  
1️⃣ **Select a state** from the dropdown filter.  
2️⃣ **Choose a district** (if needed).  
3️⃣ **Adjust the slider** to filter by year.  
4️⃣ **Analyze trends** using the interactive charts.  

### **📸 Screenshots**  
**Crime Trend Visualization 📊**  
![Crime Trend Screenshot](https://your-image-link.com](https://github.com/akeesh13/B42_DA_002_Insight-Innovators/blob/1071a5095f2e58c39365ece7f93352a0c5f23b3c/year%20trend.png))  

**State-Level Crime Analysis 🗺️**  
![State Crime Screenshot](https://your-image-link.com](https://github.com/akeesh13/B42_DA_002_Insight-Innovators/blob/0b879c3c7c6d04bab7671bf566b0fc93db4cec75/Screenshot%202025-02-10%20023333.png))  

---

## **🛠 Technology Stack**  
🚀 **Languages & Frameworks:**  
- **Python** (Data Processing & EDA)  
- **Streamlit** (Interactive Dashboard)  

📊 **Data & Visualization:**  
- **Pandas** (Data Manipulation)  
- **Seaborn & Matplotlib** (Visualizations)  

🔧 **Other Tools:**  
- **Jupyter Notebook** (EDA)  
- **GitHub** (Version Control)  
