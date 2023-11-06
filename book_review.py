import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Create a list to store the reviewText and sentiment scores
review_data = []

# Read data from the "all_books_review.csv" CSV file
with open('all_books_review.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        review_text = row['reviewText']
        
        # Analyze the sentiment of the reviewText
        sentiment = sia.polarity_scores(review_text)
        
        # Determine sentiment category based on the compound score
        if sentiment['compound'] >= 0.05:
            sentiment_category = "Positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_category = "Negative"
        else:
            sentiment_category = "Neutral"
        
        # Store reviewText, sentiment scores, and sentiment category in the list
        review_data.append({
            'ReviewText': review_text,
            'Sentiment Score': sentiment['compound'],
            'Sentiment Category': sentiment_category
        })

# Perform sentiment analysis on each reviewText
for data in review_data:
    print(f"Review Text: {data['ReviewText']}")
    print(f"Sentiment Score: {data['Sentiment Score']:.2f}")
    print(f"Sentiment Category: {data['Sentiment Category']}")
    print()
