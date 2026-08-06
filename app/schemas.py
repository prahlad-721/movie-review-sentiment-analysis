from pydantic import BaseModel

class ReviewRequest(BaseModel):
    review: str

class PredictionResponse(BaseModel):
    sentiment: str