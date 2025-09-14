import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(page_title="Beats by Dre Dashboard", layout="wide")
st.title("Beats by Dre: Consumer Insights & Market Analysis")

# ------------------------------
# 1. Consumer Insights
# ------------------------------
st.header("Consumer Insights")
st.markdown("""
- Consumers highly value **sound quality** and **battery life**.  
- Common complaints: **price** and limited wireless options.  
- Positive reactions: stylish design, brand loyalty, durability.  
""")

# ------------------------------
# 2. Sentiment Analysis
# ------------------------------
st.header("Sentiment Analysis")
sentiment = pd.DataFrame({
    "Sentiment": ["Positive", "Neutral", "Negative"],
    "Percent": [55, 25, 20]
})
fig_sentiment = px.pie(sentiment, names="Sentiment", values="Percent",
                       title="Customer Sentiment Distribution",
                       color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig_sentiment, use_container_width=True)

# ------------------------------
# 3. Feature Priorities
# ------------------------------
st.header("Top Consumer Priorities")
keywords = pd.DataFrame({
    "Feature": ["Sound Quality", "Battery Life", "Price", "Design"],
    "Mentions": [40, 30, 25, 15]
})
fig_keywords = px.bar(keywords, x="Feature", y="Mentions",
                      title="Features Consumers Care About Most",
                      color="Mentions", color_continuous_scale="Viridis")
st.plotly_chart(fig_keywords, use_container_width=True)

# ------------------------------
# 4. Market Trends
# ------------------------------
st.header("Market Trends")
adoption = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "Adoption %": [40, 50, 60]
})
fig_adoption = px.line(adoption, x="Year", y="Adoption %", markers=True,
                       title="Wireless Speaker Adoption Trend")
st.plotly_chart(fig_adoption, use_container_width=True)

# ------------------------------
# 5. Competitor Comparison
# ------------------------------
st.header("Competitor Comparison")
competitors = pd.DataFrame({
    "Brand": ["JBL", "Sony", "Beats"],
    "Price ($)": [60, 80, 100],
    "Battery Life (hrs)": [10, 12, 12],
    "Sound Quality": ["Good", "Excellent", "Excellent"],
    "Popularity": ["High", "Medium", "Medium"]
})
st.dataframe(competitors)

# ------------------------------
# 6. User Age Distribution
# ------------------------------
st.header("User Age Distribution")
age_data = pd.DataFrame({
    "Age Group": ["16-20", "21-25", "26-30", "31-35", "36-40", "41+"],
    "Users": [120, 250, 180, 90, 60, 40]
})
fig_age = px.bar(age_data, x="Age Group", y="Users",
                 title="Beats Users by Age Group",
                 color="Users", color_continuous_scale="Blues")
st.plotly_chart(fig_age, use_container_width=True)

st.markdown("""
**Insight:** Most Beats users are **21–25 years old**, indicating strong adoption among Gen Z. 
Companies should target this group with social media campaigns and product designs that appeal to younger consumers.
""")

# ------------------------------
# 7. Consumer Comments Word Cloud
# ------------------------------
st.header("Consumer Comments Word Cloud")
# Sample comments
comments = [
    "Love the sound quality", "Battery lasts long", "Too expensive",
    "Stylish design", "Amazing bass", "Not worth the price", "Very comfortable",
    "Great for workouts", "Battery drains quickly", "Sound is clear and crisp"
]

# Combine all comments into a single string
text = " ".join(comments)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Display word cloud using matplotlib
fig_wc, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig_wc)

# ------------------------------
# 8. Key Recommendations
# ------------------------------
st.header("Key Recommendations")
st.markdown("""
1. Launch a **mid-priced ($50–$100) high-fidelity wireless speaker**.  
2. Market via **social media campaigns** emphasizing sound quality and portability.  
3. Distribute through **Amazon and Beats website**.  
4. Collect feedback continuously for **product improvement**.  
""")
