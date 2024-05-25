Sure! Here is the updated `README.md` file with emojis added to the titles:

---

# 📊 Sentiment Analysis for Chatgram

This project implements a sentiment analysis tool for the social media app Chatgram, using Streamlit for the web interface, Vader Lexicon for sentiment analysis, MongoDB for data storage, and Python as the programming language.

## 📚 Table of Contents

- [📋 Introduction](#introduction)
- [✨ Features](#features)
- [🛠 Technologies Used](#technologies-used)
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [🤝 Contributing](#contributing)
- [📜 License](#license)

## 📋 Introduction

Chatgram is a social media application that allows users to post messages and interact with each other. This project aims to analyze the sentiment of the messages posted on Chatgram, categorizing them as happy 😊, sad 😢, or neutral 😐. The sentiment analysis is performed using the Vader Lexicon, and the results are displayed using a Streamlit web interface. The messages and their sentiment scores are stored in a MongoDB database.

## ✨ Features

- **Sentiment Analysis**: Analyzes messages and classifies them as happy 😊, sad 😢, or neutral 😐.
- **Streamlit Web Interface**: User-friendly web interface for displaying sentiment analysis results.
- **MongoDB Integration**: Stores messages and their sentiment scores in a MongoDB database.
- **Real-time Analysis**: Provides real-time sentiment analysis as new messages are posted on Chatgram.

## 🛠 Technologies Used

- **Python**: Programming language for implementing the sentiment analysis.
- **Streamlit**: Framework for building the web interface.
- **Vader Lexicon**: Tool for performing sentiment analysis.
- **MongoDB**: Database for storing messages and sentiment scores.

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/gowthameaswar/analysis-social-media.git
   cd analysis-social-media
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB**

   Make sure MongoDB is installed and running on your machine. You can use the default settings or customize the connection string in the `config.py` file.

5. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

## 🚀 Usage

1. **Open the Streamlit Web Interface**

   Once the app is running, open your web browser and go to `http://localhost:8501`.

2. **Analyze Messages**

   Use the web interface to enter new messages or analyze existing messages stored in the MongoDB database. The sentiment analysis results will be displayed in real-time, with messages categorized as happy 😊, sad 😢, or neutral 😐.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or enhancements.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
