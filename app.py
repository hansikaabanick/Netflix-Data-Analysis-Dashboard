import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Netflix Dashboard",
    layout="wide"
)

# ---------------- CUSTOM STYLING ---------------- #

st.markdown("""
<style>

.main {
    background-color: #141414;
    color: white;
}

h1, h2, h3 {
    color: #E50914;
}

.stMetric {
    background-color: #1f1f1f;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #

df = pd.read_csv("data/netflix_titles.csv")

# ---------------- HEADER ---------------- #

st.markdown(
    "<h1 style='text-align: center;'>NETFLIX DATA ANALYSIS DASHBOARD</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<center>Interactive analysis of Netflix movies and TV shows using Python and Streamlit</center>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🎬 Netflix Filters")

type_filter = st.sidebar.selectbox(
    "Select Content Type",
    df['type'].unique()
)

st.sidebar.info(
    "Use the filter above to analyze Movies or TV Shows separately."
)

# Filtered Data
filtered_df = df[df['type'] == type_filter]

# ---------------- KPI SECTION ---------------- #

total_titles = len(df)
total_movies = len(df[df['type'] == 'Movie'])
total_shows = len(df[df['type'] == 'TV Show'])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎞 Total Titles", total_titles)

with col2:
    st.metric("🎬 Movies", total_movies)

with col3:
    st.metric("📺 TV Shows", total_shows)

st.divider()

# ---------------- DATASET PREVIEW ---------------- #

st.subheader("📋 Dataset Preview")

st.dataframe(filtered_df.head(10))

st.divider()

# ---------------- MOVIES VS TV SHOWS ---------------- #

st.subheader("🎭 Movies vs TV Shows Distribution")

fig1, ax1 = plt.subplots(figsize=(6, 4))

sns.countplot(
    x='type',
    data=df,
    palette='Reds',
    ax=ax1
)

ax1.set_facecolor("#141414")
fig1.patch.set_facecolor("#141414")

ax1.tick_params(colors='white')

ax1.set_xlabel("Content Type", color='white')
ax1.set_ylabel("Count", color='white')

st.pyplot(fig1)

st.divider()

# ---------------- RELEASE TREND ---------------- #

st.subheader("📈 Netflix Content Growth Over Years")

release_year = df['release_year'].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(12, 6))

ax2.plot(
    release_year.index,
    release_year.values,
    color='red',
    linewidth=3
)

ax2.set_facecolor("#141414")
fig2.patch.set_facecolor("#141414")

ax2.tick_params(colors='white')

ax2.set_xlabel("Year", color='white')
ax2.set_ylabel("Number of Releases", color='white')

ax2.set_title(
    "Netflix Release Trend",
    color='white',
    fontsize=16
)

st.pyplot(fig2)

st.divider()

# ---------------- TOP COUNTRIES ---------------- #

st.subheader("🌍 Top Content Producing Countries")

top_countries = df['country'].value_counts().head(10)

fig3, ax3 = plt.subplots(figsize=(10, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    palette='Reds',
    ax=ax3
)

ax3.set_facecolor("#141414")
fig3.patch.set_facecolor("#141414")

ax3.tick_params(colors='white')

ax3.set_xlabel("Number of Titles", color='white')
ax3.set_ylabel("Country", color='white')

st.pyplot(fig3)

st.divider()

# ---------------- TOP GENRES ---------------- #

st.subheader("🎬 Most Popular Genres")

top_genres = df['listed_in'].value_counts().head(10)

fig4, ax4 = plt.subplots(figsize=(12, 6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    palette='Reds',
    ax=ax4
)

ax4.set_facecolor("#141414")
fig4.patch.set_facecolor("#141414")

ax4.tick_params(colors='white')

ax4.set_xlabel("Number of Titles", color='white')
ax4.set_ylabel("Genre", color='white')

st.pyplot(fig4)

st.divider()

# ---------------- FOOTER ---------------- #

st.markdown(
    "<center><h4 style='color:red;'>Created by Hansikaa 🚀</h4></center>",
    unsafe_allow_html=True
)