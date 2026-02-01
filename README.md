# 🚀 FoundU ML Service: AI-Powered Credibility Badge System

This service is the Machine Learning microservice for the **FoundU** platform. It uses a Natural Language Processing (NLP) model to analyze user reviews and star ratings to dynamically calculate a **Credibility Badge** for cofounders and freelancers.

---

## 🛠️ 1. Prerequisites
Before running this project, ensure you have the following installed:
* **Python 3.9 or higher**
* **pip** (Python package manager)
* **Git**

---

## ⚡ 2. Step-by-Step Installation

### 1️⃣ Clone and Navigate
```bash
git clone <your-repository-url>
cd ml_service
2️⃣ Set Up Virtual Environment (Recommended)
Isolating your dependencies prevents conflicts with other Python projects.
# Windows
python -m venv venv
.\venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Initialize NLTK Data
This service requires specific NLP datasets for text preprocessing.
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
🚀 3. Running the Service
Start the FastAPI server using Uvicorn. By default, this runs on port 8000 to match the Node.js backend configuration.
uvicorn main:app --reload --port 8000
Status: Once you see INFO: Uvicorn running on http://127.0.0.1:8000, the AI is ready!

# macOS/Linux
python3 -m venv venv
source venv/bin/activate




📬 Postman Testing Guide
You can test the API endpoints using Postman. Follow the steps below for each service.

1️⃣ Test Node.js Backend (Full Integration)
This endpoint saves a review to the database and automatically triggers the AI credibility check.

Method: POST

URL: http://localhost:4000/api/reviews

Body (raw JSON):
{
    "user_id": 1,
    "reviewer_id": 3,
    "review_text": "Working with Devansh was a great experience. He is highly technical and reliable.",
    "stars": 5
}
Note: Ensure user_id and reviewer_id exist in your local MySQL users table before testing.


2️⃣ Test Python ML Service (AI Prediction Only)
Use this to verify the AI model's logic independently of the database.

Method: POST

URL: http://localhost:8000/predict-score

Body (raw JSON):
{
    "user_id": "1",
    "user_name": "devansh",
    "stars": 5,
    "text_review": "Exceptional work! Highly recommended for any technical project."
}


3️⃣ Automated Response Verification
To ensure everything is working correctly, you can paste this into the Tests tab in Postman to automatically validate the response:
// Check for successful status
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Verify JSON structure
pm.test("Response has success flag", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.success).to.eql(true);
});
