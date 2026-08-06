from fastapi import FastAPI
from app.schemas import ReviewRequest, PredictionResponse
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI(
    title="Movie Review Sentiment API",
    version="1.0"
)

model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Movie Review Sentiment API is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: ReviewRequest):

    review = clean_text(data.review)
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)[0]

    return PredictionResponse(sentiment=prediction)