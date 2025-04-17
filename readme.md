# Sentiment Review Response Generator

This project is a web application that takes user reviews as input, analyzes their sentiment (Positive, Negative, or Neutral), and generates a context-aware response using the DistilGPT-2 model.

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4. Open the app in your browser and enter a review to see the sentiment and response.

## Technologies Used:
- Python
- Streamlit
- Hugging Face Transformers (DistilBERT for sentiment analysis, DistilGPT-2 for response generation)
- PyTorch
