import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 

df= pd.read_csv('clean_crime_by_district.csv')
df.head()

# Clean column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(r'[^\w\s]', '', regex=True)

# Convert year column to integer
df["year"] = pd.to_numeric(df["year"], errors='coerce')

# Streamlit Configuration
st.set_page_config(layout="wide")
st.title("Crime Data Dashboard")

# Sidebar Filters
st.sidebar.header("Crime Data Analysis Filters")
selected_state = st.sidebar.selectbox("Select a State", options=df["stateut"].unique())
year_range = st.sidebar.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (int(df["year"].min()), int(df["year"].max())))

# Filter Data
df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1]) & (df["stateut"] == selected_state)]

# Crime Trends Over the Years
st.subheader("Crime Trends Over the Years")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_filtered, x="year", y="murder", label="Murder", marker="o", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="assault on women", label="Assault on Women", marker="s", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="kidnapping and abduction", label="Kidnapping & Abduction", marker="^", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Cases")
ax.legend()
st.pyplot(fig)

# Top 5 States with the Most Murders
st.subheader("Top 5 States with Most Murders")
top_states = df.groupby("stateut")["murder"].sum().nlargest(5)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_states.index, y=top_states.values, palette="Reds", ax=ax)
ax.set_xlabel("State/UT")
ax.set_ylabel("Total Murders")
st.pyplot(fig)

# Distribution of Murders (Histogram)
st.subheader("Distribution of Murder Cases")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df["murder"], bins=20, kde=True, color="blue", ax=ax)
st.pyplot(fig)

# Correlation Heatmap
numeric_df = df.select_dtypes(include=['number'])

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Top 5 States with Most Assaults on Women (Pie Chart)
st.subheader("Top 5 States with Most Assaults on Women")
top_women_assault = df.groupby("stateut")["assault on women"].sum().nlargest(5)
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(top_women_assault, labels=top_women_assault.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
st.pyplot(fig)

# Scatter Plot for Hurt vs. Murder Cases
st.subheader("Hurt vs. Murder Cases Relationship")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="hurt", y="murder", hue="stateut", alpha=0.7, palette="tab10", ax=ax)
st.pyplot(fig)

# Box Plot for Outlier Detection in Robbery Cases
st.subheader("Outlier Detection in Robbery Cases")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(y=df["robbery"], color="orange", ax=ax)
st.pyplot(fig)

# Descriptive Statistics
st.subheader("Descriptive Statistics")
st.write("Summary of key statistics for crime data:")
st.write(df.describe())



