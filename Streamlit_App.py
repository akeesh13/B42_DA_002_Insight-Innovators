import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 


df= pd.read_csv('cleaned_rt.csv')
df.head()

# Clean column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(r'[^\w\s]', '', regex=True)

# Convert year column to integer
df["year"] = pd.to_numeric(df["year"], errors='coerce')

# Streamlit Configuration
st.set_page_config(layout="wide")
st.title("Crime Data Dashboard")

# on side bar add the logo of the project
st.sidebar.header('Insight Innovators')
st.sidebar.image("https://i.ibb.co/8n1GN9bt/Whats-App-Image-2025-02-05-at-12-08-21-724ffd42-2.jpg",width=160)
# Sidebar Filters
st.sidebar.header("Crime Data Analysis Filters")
selected_state = st.sidebar.selectbox("Select a State", options=df["stateut"].unique())
filtered_districts = df[df["stateut"] == selected_state]["district"].unique()
selected_district = st.sidebar.selectbox("Select a District", options=filtered_districts)
year_range = st.sidebar.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (int(df["year"].min()), int(df["year"].max())))

# Filter Data
df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1]) & (df["stateut"] == selected_state) & (df["district"] == selected_district)]

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
ax.set_position([0.05, 0.1, 0.75, 0.8])  # Adjust position to move left
sns.scatterplot(data=df, x="hurt", y="murder", hue="stateut", alpha=0.7, palette="tab10", ax=ax, edgecolor='black')
ax.set_xlabel("Hurt Cases")
ax.set_ylabel("Murder Cases")
ax.set_title("Scatter Plot of Hurt vs. Murder Cases")
ax.legend(loc='upper right', bbox_to_anchor=(-0.1, 1))  # Move legend outside to the left
st.pyplot(fig) 

# KPI Metrics
st.subheader("Key Performance Indicators (KPIs)")

# Top 5 Unsafe States
top_unsafe_states = df.groupby("stateut")["murder"].sum().nlargest(5)
st.write("### Top 5 Unsafe States")
st.write(top_unsafe_states)

# Top 5 Safest States
top_safest_states = df.groupby("stateut")["murder"].sum().nsmallest(5)
st.write("### Top 5 Safest States")
st.write(top_safest_states)

# Crime Trends Over the Year
st.write("### Crime Trends Over the Year")
st.line_chart(df.groupby("year")["murder"].sum())

# Top 5 Safest States for Women
top_safest_women_states = df.groupby("stateut")["assault on women"].sum().nsmallest(5)
st.write("### Top 5 Safest States for Women")
st.write(top_safest_women_states)

# Top 5 Unsafest States for Women
top_unsafest_women_states = df.groupby("stateut")["assault on women"].sum().nlargest(5)
st.write("### Top 5 Unsafest States for Women")
st.write(top_unsafest_women_states)

# Top States on Each Crime
top_states_per_crime = df.groupby("stateut").sum().idxmax()
st.write("### Top States on Each Crime")
st.write(top_states_per_crime)

# Percentage of Each Crime in Total Atrocities
total_crimes = df['total_atrocities'].sum()
crime_sums = df[['murder', 'assault on women', 'kidnapping and abduction', 
        'dacoity', 'robbery', 'arson', 'hurt', 'prevention of atrocities poa act', 'protection of civil rights pcr act', 'other crimes against scs']].sum()
crime_percentages = (crime_sums / total_crimes) * 100
st.write("### Percentage of Each Crime in Total Atrocities")
st.write(crime_percentages)


# Descriptive Statistics
st.subheader("Descriptive Statistics")
st.write("Summary of key statistics for crime data:")
st.write(df.describe())
    
