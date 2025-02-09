import streamlit as st
import pandas as pd
import numpy as np
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
#st.title("Crime Data Dashboard")
st.markdown("""
    <h2 style="font-weight: bold; text-decoration: underline; 
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 4.25em;">
       Crime Data Dashboard
    </h3>
""", unsafe_allow_html=True)

##############################################################################################################################################

st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-weight: 900; font-size: 32px; color: #FFF; font-family: 'Arial', sans-serif; 
                   text-decoration: underline wavy red 3px;  /* Custom underline */
                   text-underline-offset: 5px;"> 
            Insight Innovators
        </h1>
    </div>
""", unsafe_allow_html=True)

import streamlit as st

try:
    st.sidebar.markdown(
        """
        <div style="display: flex; justify-content: center;">  <img src="https://i.ibb.co/8n1GN9bt/Whats-App-Image-2025-02-05-at-12-08-21-724ffd42-2.jpg" width="160">
        </div>
        """,
        unsafe_allow_html=True,
    )
except Exception as e:
    st.sidebar.markdown(
        """
        <div style="display: flex; justify-content: center;">  <span>Project Logo (Error loading image)</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    print(f"Error loading image: {e}")

st.sidebar.markdown("<h3 style='font-weight: bold; font-size: 20px;'>Data Filters</h3>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .streamlit-expanderHeader { /* Style the expander header (if used) */
        font-weight: bold !important; /* Make it bold */
    }
    label { /* Target all labels in the sidebar */
        font-weight: bold;
        text-decoration: underline;
        font-size: 16px; /* Adjust size as needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

state_options = sorted(df["stateut"].unique())
selected_state = st.sidebar.selectbox("Select a State", options=state_options)

filtered_districts = sorted(df[df["stateut"] == selected_state]["district"].unique()) # Sort districts
selected_district = st.sidebar.selectbox("Select a District", options=filtered_districts)

min_year = int(df["year"].min()) if not pd.isna(df["year"].min()) else 2001 #handle NaN min year
max_year = int(df["year"].max()) if not pd.isna(df["year"].max()) else 2022 #handle NaN max year
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

df_filtered = df[
    (df["year"] >= year_range[0]) &
    (df["year"] <= year_range[1]) &
    (df["stateut"] == selected_state) &
    (df["district"] == selected_district)
]

if df_filtered.empty:
    st.warning("No data available for the selected filters. Please adjust your selections.")
    st.stop() 
    
###############################################################################################################################################
st.markdown("""
    <h2 style="font-weight: bold; 
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
       Crime Trends Over the Years of each Crimes
    </h2>
""", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 5)) 


sns.lineplot(data=df_filtered, x="year", y="murder", label="Murder", marker="o", ax=ax) 
sns.lineplot(data=df_filtered, x="year", y="assault on women", label="Assault on Women", marker="s", ax=ax) 
sns.lineplot(data=df_filtered, x="year", y="kidnapping and abduction", label="Kidnapping & Abduction", marker="^", ax=ax) 
sns.lineplot(data=df_filtered, x="year", y="dacoity", label="Dacoity", marker="D", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="robbery", label="Robbery", marker="P", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="arson", label="Arson", marker="X", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="hurt", label="Hurt", marker="*", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="prevention of atrocities poa act", label="POA Act", marker="v", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="protection of civil rights pcr act", label="PCR Act", marker=">", ax=ax)
sns.lineplot(data=df_filtered, x="year", y="other crimes against scs", label="Other Crimes", marker="<", ax=ax)

ax.set_xlabel("Year", fontsize=12, color="#444")  
ax.set_ylabel("Number of Cases", fontsize=12, color="#444")
ax.set_title("Crime Trends Over the Years of each Crimes", fontsize=16, fontweight="bold", color="#222") 

ax.tick_params(axis='both', labelsize=10, color="#666") 
ax.legend(fontsize=10, loc="upper left", frameon=False)  
ax.grid(True, linestyle="--", alpha=0.5, color="#ddd")  
ax.set_facecolor("#f8f8f8") 

# Improved Spines (More Subtle):
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#ccc') 
ax.spines['left'].set_color('#ccc') 
st.pyplot(fig)



################################################################################################################################################

st.markdown("""
    <h2 style="font-weight: bold;  
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
       Top 5 States with Most Murders
    </h2>
""", unsafe_allow_html=True)

top_states = df.groupby("stateut")["murder"].sum().nlargest(5)

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_states.index, y=top_states.values, palette="Reds_r", ax=ax, edgecolor='black', linewidth=1.5)

ax.set_xlabel("State/UT", fontsize=14, color="#333")
ax.set_ylabel("Total Murders", fontsize=14, color="#333")
ax.set_title("Top 5 States with Most Murders", fontsize=16, fontweight="bold", color="#111")
ax.tick_params(axis='x', rotation=45, labelsize=12, color="#555")  
ax.set_xticklabels(ax.get_xticklabels(), ha='right')  

ax.tick_params(axis='y', labelsize=12, color="#555")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#888')
ax.spines['bottom'].set_color('#888')

ax.grid(axis='y', linestyle='--', alpha=0.7, color="#ddd")
ax.set_facecolor("#f9f9f9")
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

st.pyplot(fig)


#########################################################################################################################################################
numeric_df = df.select_dtypes(include=['number']).drop(columns='year', errors='ignore')
st.markdown("""
    <h2 style="font-weight: bold;  
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
       Correlation Heatmap
    </h2>
""", unsafe_allow_html=True)


fig, ax = plt.subplots(figsize=(14, 8)) 
corr_matrix = numeric_df.corr()
mask = np.triu(corr_matrix)  
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", mask=mask, 
            linewidths=.5, 
            cbar_kws={'label': 'Correlation'}, 
            ax=ax)
ax.set_title("Correlation Heatmap", fontsize=16, fontweight="bold", color="#111")
ax.tick_params(axis='both', labelsize=10, color="#555")  
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

####################################################################################################################################################

# Top 5 States with Most Assaults on Women (Pie Chart)

st.markdown("""
    <h2 style="font-weight: bold; 
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
        Top 5 States with Most Assaults on Women
    </h2>
""", unsafe_allow_html=True)

top_women_assault = df.groupby("stateut")["assault on women"].sum().nlargest(5)

fig, ax = plt.subplots(figsize=(6, 6))  
colors = sns.color_palette("Set3", n_colors=len(top_women_assault))  
explode = [0] * len(top_women_assault)
largest_slice_index = top_women_assault.idxmax()
if largest_slice_index in top_women_assault.index:
    explode[top_women_assault.index.get_loc(largest_slice_index)] = 0.1  
wedges, texts, autotexts = ax.pie(top_women_assault, 
                                 labels=top_women_assault.index, 
                                 autopct="%1.1f%%", 
                                 colors=colors, 
                                 explode=explode,  
                                 startangle=90,  
                                 textprops={'fontsize': 12, 'color': 'black'},
                                 wedgeprops={"linewidth": 1, "edgecolor": "white"}) 

ax.set_title("Top 5 States with Most Assaults on Women", fontsize=16, fontweight="bold", color="#333")
ax.axis("equal")  
ax.legend(wedges, top_women_assault.index,  
          title="States", 
          loc="center left",   
          bbox_to_anchor=(1, 0, 0.5, 1)) 
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


st.pyplot(fig)

#####################################################################################################################################
import plotly.express as px
st.markdown("""
    <h2 style="font-weight: bold; 
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
        Scatter Plot for Hurt vs. Murder Cases
    </h2>
""", unsafe_allow_html=True)

fig = px.scatter(df, x="hurt", y="murder", color="stateut", hover_name="stateut") 
st.plotly_chart(fig)


############################################################################################################################


st.markdown("""
    <h2 style="font-weight: bold; text-decoration: underline; 
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
        Key Performance Indicators (KPIs)
    </h2>
""", unsafe_allow_html=True)

####################################################################################################################################
col1, col2 = st.columns(2)  # Create 3 columns

with col1:
    top_unsafe_states = df.groupby("stateut")["murder"].sum().nlargest(5)
    st.markdown("### Top 5 Unsafe States")  # Use markdown for smaller heading
    st.write(top_unsafe_states)

with col2:
    top_safest_states = df.groupby("stateut")["murder"].sum().nsmallest(5)
    st.markdown("### Top 5 Safest States")  # Use markdown for smaller heading
    st.write(top_safest_states)
st.markdown(
    """
    <style>
    .st-expander { /* Target the expander elements */
        height: 200px; /* Adjust height as needed */
        overflow-y: auto; /* Add scroll if content overflows */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


#####################################################################################################################################
st.write("### Crime Trends Over the Year")
st.line_chart(df.groupby("year")["total_atrocities"].sum())


##################################################################################################################################

col1, col2 = st.columns(2) 

with col1:
    top_safest_women_states = df.groupby("stateut")["assault on women"].sum().nsmallest(5)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True) # Center the content
    st.markdown("### Top 5 Safest States for Women", unsafe_allow_html=True)
    st.write(top_safest_women_states)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    top_unsafest_women_states = df.groupby("stateut")["assault on women"].sum().nlargest(5)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True) # Center the content
    st.markdown("### Top 5 Unsafest States for Women", unsafe_allow_html=True)
    st.write(top_unsafest_women_states)
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .st-column { /* Add some spacing between columns */
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

######################################################################################################################################

col1, col2 = st.columns(2)  

with col1:
    top_states_per_crime = df.groupby("stateut").sum().idxmax()
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True) 
    st.markdown("### Top States on Each Crime", unsafe_allow_html=True)
    st.write(top_states_per_crime)  
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    total_crimes = df['total_atrocities'].sum()
    crime_sums = df[['murder', 'assault on women', 'kidnapping and abduction',
                    'dacoity', 'robbery', 'arson', 'hurt', 'prevention of atrocities poa act',
                    'protection of civil rights pcr act', 'other crimes against scs']].sum()
    crime_percentages = (crime_sums / total_crimes) * 100
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)  # Center
    st.markdown("### Percentage of Each Crime in Total Atrocities", unsafe_allow_html=True)
    st.write(crime_percentages) 
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .st-column {
        padding: 20px; /* Adjust as needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#####################################################################################################################################
st.markdown("""
    <h2 style="font-weight: bold; text-decoration: underline; 
                font-family: 'Verdana', 'Geneva', 'Tahoma', sans-serif; /* Web-safe font stack */
                font-size: 1.25em;">
        Descriptive Statistics
    </h2>
""", unsafe_allow_html=True)

st.write("Summary of key statistics for crime data:")
st.write(df.describe())
