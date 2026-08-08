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
        with st.spinner("Analyzing... (first request may take up to a minute if the server was idle)"):
            try:
                response = requests.post(
                    "https://movie-review-sentiment-analysis-w2eo.onrender.com/predict",
                    json={"review": review},
                    timeout=90
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

            except requests.exceptions.RequestException:
                st.error("Could not reach the prediction server. Please try again.")