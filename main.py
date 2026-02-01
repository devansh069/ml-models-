from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
from preprocess import Preprocess

app = FastAPI()

# 1. Load the "Brain" (Vectorizer + Model)
try:
    with open("models/logistic_regression_model.pkl", "rb") as f:
        vectorizer, nlp_model = pickle.load(f)
    print("✅ ML Model and Vectorizer loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")

cleaner = Preprocess()

# 2. Define the Request Schema (Matches your API data)
class ReviewRequest(BaseModel):
    user_id: str
    user_name: str
    stars: float        # Rating from your Star Model/Input (1-5)
    text_review: str    # Text from the user review

@app.post("/predict-score")
async def get_combined_score(request: ReviewRequest):
    # A. NLP Prediction Logic
    # 1. Clean the incoming text
    cleaned_text = " ".join(cleaner.lemmatize(request.text_review))
    # 2. Vectorize using the saved translator
    vectorized_text = vectorizer.transform([cleaned_text])
    # 3. Predict the rating (1-5)
    predicted_text_rating = nlp_model.predict(vectorized_text)[0]

    # B. Calculate Weighted Score (1-100 Scale)
    # Formula: Average the 1-5 scales and multiply by 20 to get a % score
    # (Example: 4.5 average = 90%)
    average_rating = (0.5 * request.stars) + (0.5 * float(predicted_text_rating))
    final_score = average_rating * 20 

    # C. Categorize into your 4 Categories
    category = ""
    if final_score >= 90 and final_score <= 95:
        category = "95-90"
    elif final_score >= 85 and final_score < 90:
        category = "90-85"
    elif final_score >= 80 and final_score < 85:
        category = "85-80"
    else:
        category = "Below 80"

    return {
        "user_id": request.user_id,
        "user_name": request.user_name,
        "final_score": round(final_score, 2),
        "category": category,
        "details": {
            "input_stars": request.stars,
            "ai_predicted_rating": int(predicted_text_rating)
        }
    }