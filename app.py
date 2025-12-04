"""
app.py
Streamlit interface for AI-powered email automation
"""

import streamlit as st
from email_processor import load_emails, predict_email, train_email_classifiers

st.set_page_config(page_title="AI Email Automation", layout="wide")

st.title("AI-Powered Email Automation System")

# Load emails
df = load_emails()
st.subheader("Sample Emails")
st.dataframe(df.head())

# Train models button
if st.button("Train Models"):
    train_email_classifiers(df)
    st.success("Models trained successfully!")

# Input for new email
st.subheader("Test Email")
email_text = st.text_area("Paste email content here:")

if st.button("Analyze Email"):
    if email_text.strip() == "":
        st.warning("Please enter email content")
    else:
        category, priority = predict_email(email_text)
        st.write(f"**Predicted Category:** {category}")
        st.write(f"**Predicted Priority:** {'High' if priority==1 else 'Low'}")
        reply = suggest_reply(email_text, category)
        st.write(f"**Suggested Reply:** {reply}")
