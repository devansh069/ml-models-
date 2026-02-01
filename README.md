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
