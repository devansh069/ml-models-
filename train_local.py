import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import Preprocess

# 1. Load your local CSV
print("Reading local data...")
df = pd.read_csv("data/train.csv")

# Using the exact column names we just found
X_raw = df['Review'].fillna('') 
y = df['Rating']

# 2. Clean the text
print("Cleaning text (this may take a minute)...")
cleaner = Preprocess()
# This turns the list of lemmas back into a string for the vectorizer
X_cleaned = [" ".join(cleaner.lemmatize(text)) for text in X_raw]

# 3. Vectorize (Turn text into numbers)
print("Training model...")
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X_cleaned)

# 4. Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_vectorized, y)

# 5. Save the Vectorizer and Model together
with open("models/logistic_regression_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Success! Your model is saved in models/logistic_regression_model.pkl")