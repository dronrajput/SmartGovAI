from transformers import pipeline

# Load Hugging Face NLP pipelines
sentiment_pipeline = pipeline("sentiment-analysis")
category_pipeline = pipeline("zero-shot-classification")

def analyze_feedback(text):
    # Sentiment
    sentiment = sentiment_pipeline(text)[0]['label']

    # Topic
    candidate_labels = ["Water Supply", "Traffic", "Electricity", "Waste Management", "Public Safety"]
    category_result = category_pipeline(text, candidate_labels)
    category = category_result['labels'][0]

    # Urgency level
    urgency = "Low"
    urgent_words = ["immediately", "urgent", "emergency", "now", "danger", "critical"]
    if any(word in text.lower() for word in urgent_words):
        urgency = "High"
    elif sentiment == "NEGATIVE":
        urgency = "Medium"

    return sentiment, category, urgency
