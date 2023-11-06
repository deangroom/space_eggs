import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    sentiment = sentiment_scores['compound']

    if sentiment >= 0.05:
        return "Positive"
    elif sentiment <= -0.05:
        return "Negative"
    else:
        return "Neutral"

text=input("Enter the text: ")
print("The sentiment of the text is: ", perform_sentiment_analysis(text))