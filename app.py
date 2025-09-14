import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Beats by Dre Dashboard")

# Load Data
sentiment = pd.DataFrame({"Sentiment": ["Positive","Neutral","Negative"], "Percent":[55,25,20]})
keywords = pd.DataFrame({"Feature":["Sound","Battery","Price","Design"], "Mentions":[40,30,25,15]})
adoption = pd.DataFrame({"Year":[2022,2023,2024],"Adoption":[40,50,60]})

# Sentiment Pie
st.subheader("Consumer Sentiment")
fig1 = px.pie(sentiment, names="Sentiment", values="Percent")
st.plotly_chart(fig1)

# Keyword Bar
st.subheader("Top Consumer Priorities")
fig2 = px.bar(keywords, x="Feature", y="Mentions")
st.plotly_chart(fig2)

# Market Trend
st.subheader("Wireless Speaker Adoption Trend")
fig3 = px.line(adoption, x="Year", y="Adoption", markers=True)
st.plotly_chart(fig3)
