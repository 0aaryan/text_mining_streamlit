# sentiment_analysis_model.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def perform_sentiment_analysis(text):
    nltk.download("vader_lexicon")
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    # Determine sentiment label based on the compound score
    if sentiment_scores["compound"] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment

# Example usage
if __name__ == "__main__":
    text = "This is a very good example of sentiment analysis."
    sentiment = perform_sentiment_analysis(text)
    print("Sentiment:", sentiment)
