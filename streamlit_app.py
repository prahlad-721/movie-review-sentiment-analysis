import streamlit as st
import requests

st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬"
)

st.title("🎬 Movie Review Sentiment Analysis")

st.write("Enter a movie review and click Predict.")

review = st.text_area(
    "Movie Review",
    height=200,
    placeholder="Example: This movie was amazing!"
)

if st.button("Predict"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "review": review
            }
        )

        if response.status_code == 200:

            result = response.json()

            sentiment = result["sentiment"]

            if sentiment.lower() == "positive":
                st.success("😊 Positive Review")

            else:
                st.error("😞 Negative Review")

        else:
            st.error("Prediction Failed")