# AI-Powered Email Automation System

## Overview
This project provides an AI-based system to intelligently manage a user's email inbox. Features include:
- Automatic email categorization (work, personal, spam, etc.)
- Priority detection (high vs. low)
- Suggested automated replies
- Integration with Streamlit for interactive usage

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download dataset: `python data_loader.py`
4. Run app: `streamlit run app.py`

## Folder Structure
- `app.py` : Main Streamlit app
- `data_loader.py` : Downloads Enron dataset
- `email_processor.py` : Core AI/NLP email processing
- `models/` : Saved models
- `data/` : Downloaded datasets
