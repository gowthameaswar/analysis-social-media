import pymongo
from pymongo import MongoClient
import streamlit as st
import nltk
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Download the VADER lexicon if you haven't done so before
#nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
st.title('Sentiment Analysis for Chatgram')
st.write("Negative-1")
st.write("Neutral-2")
st.write("Positive-3")

# Define a function to analyze the sentiment of a given input text
def analyze_sentiment(text):
    # Use the VADER sentiment analyzer to get the sentiment scores
    scores = analyzer.polarity_scores(text)
    # Determine the sentiment label based on the compound score
    if scores['compound'] >= 0.05:
        return 3
    elif scores['compound'] <= -0.05:
        return 1
    else:
        return 2

# Set up a client to connect to your MongoDB Atlas cluster
client = MongoClient("mongodb+srv://gowtham07:gowtham07@awtcluster.aavwpkd.mongodb.net/socialchat")

# Access the "socialchat" database and "posts" collection
db = client["socialchat"]
posts_collection = db["posts"]

# Find all posts and retrieve the "title" and "content" fields
posts = posts_collection.find({}, {"title": 1, "content": 1, "_id": 0})

# Create empty arrays to store the "title" and "content" fields
titles = []
contents = []

# Loop through each post and append its "title" and "content" fields to the arrays
for post in posts:
    titles.append(post["title"])
    contents.append(post["content"])

# Create empty arrays to store the sentiment labels
t_sentiments = []
c_sentiments = []

# Loop through each title in the titles array and analyze its sentiment
for title in titles:
    sentiment = analyze_sentiment(title)
    t_sentiments.append(sentiment)

# Loop through each content in the contents array and analyze its sentiment
for content in contents:
    sentiment = analyze_sentiment(content)
    c_sentiments.append(sentiment)

# Display the title sentiments as a table
st.write("Title Sentiments:")
title_table = list(zip(titles, t_sentiments))
st.table(title_table)

# Display the content sentiments as a table
st.write("Content Sentiments:")
content_table = list(zip(contents, c_sentiments))
st.table(content_table)



plt.figure(figsize=(8, 5))
plt.hist(t_sentiments, bins=[1, 2, 3, 4], align='left')
plt.xticks([1, 2, 3], ['Negative', 'Neutral', 'Positive'])
plt.xlabel('Sentiment')
plt.ylabel('Number of Titles')
plt.title('Sentiment Analysis of Titles')
st.pyplot(plt)

# Plot the sentiment values for contents
plt.figure(figsize=(8, 5))
plt.hist(c_sentiments, bins=[1, 2, 3, 4], align='left')
plt.xticks([1, 2, 3], ['Negative', 'Neutral', 'Positive'])
plt.xlabel('Sentiment')
plt.ylabel('Number of Contents')
plt.title('Sentiment Analysis of Contents')
st.pyplot(plt)

df = pd.DataFrame({'Title Sentiments': t_sentiments, 'Content Sentiments': c_sentiments})

# Create a line graph for Title Sentiments
st.write('## Title Sentiments')
fig1 = px.line(df, x=df.index, y='Title Sentiments')
st.plotly_chart(fig1)

# Create a line graph for Content Sentiments
st.write('## Content Sentiments')
fig2 = px.line(df, x=df.index, y='Content Sentiments')
st.plotly_chart(fig2)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].scatter(range(len(t_sentiments)), t_sentiments)
axs[0].set_title('Title Sentiments')
axs[0].set_xlabel('Post Index')
axs[0].set_ylabel('Sentiment Value')
axs[1].scatter(range(len(c_sentiments)), c_sentiments)
axs[1].set_title('Content Sentiments')
axs[1].set_xlabel('Post Index')
axs[1].set_ylabel('Sentiment Value')
st.pyplot(fig)
