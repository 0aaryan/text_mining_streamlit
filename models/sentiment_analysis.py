import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

# Method 1: Sentiment analysis using VADER
def vader_lexicon(text):
    nltk.download("vader_lexicon")
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores["compound"] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, sentiment_scores["compound"] * 100

# Method 2: Sentiment analysis using TextBlob
def textblob_analysis(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        percent = polarity * 100
    elif polarity < 0:
        sentiment = "Negative"
        percent = abs(polarity) * 100
    else:
        sentiment = "Neutral"
        percent = 100

    return sentiment, percent

# Method 3: Sentiment analysis using Transformers (BERT)
def bert_analysis(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = sentiment_analyzer(text)

    return results[0]["label"], results[0]["score"] * 100
