"""
email_processor.py
Core AI/NLP logic for email automation:
- Categorization (work, personal, spam, etc.)
- Priority detection
- Automated response suggestions
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

# Path to dataset
DATA_DIR = "./data/enron_mail_20150507/maildir/"

# Placeholder function: Load emails (simplified for demo)
def load_emails():
    # For demonstration, we will assume a CSV exists. Real case: parse Enron folders.
    csv_path = os.path.join(DATA_DIR, "emails.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        # Dummy DataFrame
        df = pd.DataFrame({
            "content": ["Please review the report", "Free lottery winner!", "Meeting at 3PM"],
            "category": ["work", "spam", "work"],
            "priority": [1, 0, 1]
        })
    return df

# Train a simple classifier (category + priority)
def train_email_classifiers(df):
    X = df["content"]
    y_category = df["category"]
    y_priority = df["priority"]

    # Category classifier
    category_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', MultinomialNB())
    ])
    category_pipeline.fit(X, y_category)
    
    # Priority classifier
    priority_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', MultinomialNB())
    ])
    priority_pipeline.fit(X, y_priority)

    # Save models
    os.makedirs("models", exist_ok=True)
    pickle.dump(category_pipeline, open("models/category_model.pkl", "wb"))
    pickle.dump(priority_pipeline, open("models/priority_model.pkl", "wb"))

    print("Models trained and saved in /models")

# Predict category and priority for new emails
def predict_email(email_text):
    category_model = pickle.load(open("models/category_model.pkl", "rb"))
    priority_model = pickle.load(open("models/priority_model.pkl", "rb"))

    category = category_model.predict([email_text])[0]
    priority = priority_model.predict([email_text])[0]

    return category, priority

# Suggest a basic response
def suggest_reply(email_text, category):
    if category == "work":
        return "Thank you for your email. I will review it and get back to you shortly."
    elif category == "personal":
        return "Got it! Will respond soon."
    elif category == "spam":
        return "No reply necessary."
    else:
        return "Thank you for your email."
