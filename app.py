import streamlit as st
import pymongo
from pymongo import MongoClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if you haven't done so before
nltk.download('vader_lexicon')

# Set up a client to connect to your MongoDB Atlas cluster
client = MongoClient("mongodb+srv://gowtham07:gowtham07@awtcluster.aavwpkd.mongodb.net/socialchat")

# Access the "socialchat" database and "posts" collection
db = client["socialchat"]
posts_collection = db["posts"]

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define a function to analyze the sentiment of a given input text
def analyze_sentiment(text):
    # Use the VADER sentiment analyzer to get the sentiment scores
    scores = analyzer.polarity_scores(text)
    # Determine the sentiment label based on the compound score
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Find all posts and retrieve the "title" and "content" fields
posts = posts_collection.find({}, {"title": 1, "content": 1, "_id": 0})

# Create empty arrays to store the "title" and "content" fields
titles = []
contents = []

# Loop through each post and append its "title" and "content" fields to the arrays
for post in posts:
    titles.append(post["title"])
    contents.append(post["content"])

# Loop through each title in the titles array and analyze its sentiment
t_sentiments = []
for title in titles:
    sentiment = analyze_sentiment(title)
    t_sentiments.append(sentiment)

# Loop through each content in the contents array and analyze its sentiment
c_sentiments = []
for content in contents:
    sentiment = analyze_sentiment(content)
    c_sentiments.append(sentiment)

# Create a Streamlit app to display the sentiment analysis results
st.title("Sentiment Analysis Results")
st.write("Titles:")
for i in range(len(titles)):
    st.write(f"{titles[i]}: {t_sentiments[i]}")

st.write("Contents:")
for i in range(len(contents)):
    st.write(f"{contents[i]}: {c_sentiments[i]}")
