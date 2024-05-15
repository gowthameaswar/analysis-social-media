import streamlit as st
import pymongo
from pymongo import MongoClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd

nltk.download('vader_lexicon')
st.set_page_config(page_title="Sentiment Analysis for Chatgram",  page_icon="📊")

client = MongoClient("mongodb+srv://gowtham07:gowtham07@awtcluster.aavwpkd.mongodb.net/socialchat")

db = client["socialchat"]
posts_collection = db["posts"]

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return '😊 Positive'
    elif scores['compound'] <= -0.05:
        return '😔 Negative'
    else:
        return '😐 Neutral'

posts = posts_collection.find({}, {"title": 1, "content": 1, "_id": 0})

data = []

for post in posts:
    title = post["title"]
    content = post["content"]
    title_sentiment = analyze_sentiment(title)
    content_sentiment = analyze_sentiment(content)
    data.append((title, title_sentiment, content, content_sentiment))

# Create a DataFrame to store sentiments data
df = pd.DataFrame(data, columns=["Title", "Title Sentiment", "Content", "Content Sentiment"])

st.title("Sentiment Analysis Results for Chatgram📊")
st.markdown("[Chatgram Link](https://github.com/gowthameaswar/chatgram)", unsafe_allow_html=True)

st.write("Sentiment Analysis Results:")

# Displaying the Table
st.subheader("Sentiment Analysis Data:")
st.table(df)

# Plotting for Title Sentiments
st.subheader("Title Sentiments Distribution")
fig, ax = plt.subplots()
title_sentiments_plot = df["Title Sentiment"].value_counts().plot(kind="bar", color=["green", "red", "blue"], ax=ax)
title_sentiments_plot.set_xlabel("Sentiment")
title_sentiments_plot.set_ylabel("Count")
st.pyplot(fig)

# Plotting for Content Sentiments
st.subheader("Content Sentiments Distribution")
fig, ax = plt.subplots()
content_sentiments_plot = df["Content Sentiment"].value_counts().plot(kind="bar", color=["green", "red", "blue"], ax=ax)
content_sentiments_plot.set_xlabel("Sentiment")
content_sentiments_plot.set_ylabel("Count")
st.pyplot(fig)
