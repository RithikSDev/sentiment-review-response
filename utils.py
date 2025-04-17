from transformers import pipeline
import random
import csv
import os
from datetime import datetime

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Predefined template responses
RESPONSES = {
    "POSITIVE": [
        "Thank you so much for your kind words! We're thrilled to hear you had a great experience.",
        "We truly appreciate your positive feedback. It means a lot to our team!",
        "Glad to know everything went well. Thanks for being an awesome customer!"
    ],
    "NEGATIVE": [
        "We're really sorry to hear about your experience. We're looking into this and will make it right.",
        "Thank you for your honest feedback. We'll use this to improve our services.",
        "We apologize for the inconvenience. Please allow us the chance to fix this for you."
    ],
    "NEUTRAL": [
        "Thanks for your feedback! If there's anything we can do better, feel free to let us know.",
        "We appreciate you taking the time to share your thoughts.",
        "Your feedback helps us grow. Thank you!"
    ]
}

LOG_FILE_PATH = "logs/review_logs.csv"

def respond_to_review(review_text: str):
    try:
        result = sentiment_pipeline(review_text)[0]
        label = result["label"].upper()

        if "NEGATIVE" in label:
            sentiment = "Negative"
            response = random.choice(RESPONSES["NEGATIVE"])
        elif "POSITIVE" in label:
            sentiment = "Positive"
            response = random.choice(RESPONSES["POSITIVE"])
        else:
            sentiment = "Neutral"
            response = random.choice(RESPONSES["NEUTRAL"])

    except Exception as e:
        sentiment = "Unknown"
        response = "Sorry, we couldn't process the review. Please try again later."

    # Save to CSV
    log_review(review_text, sentiment, response)

    return response, sentiment

def log_review(review, sentiment, response):
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    write_header = not os.path.exists(LOG_FILE_PATH)

    with open(LOG_FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Timestamp", "Review", "Sentiment", "Response"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), review, sentiment, response])
