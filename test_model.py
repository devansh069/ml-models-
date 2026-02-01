import pickle
from preprocess import Preprocess

def test_prediction():
    try:
        with open("models/logistic_regression_model.pkl", "rb") as f:
            # We now load a tuple: (vectorizer, model)
            vectorizer, model = pickle.load(f)
        print("✅ Model and Vectorizer loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    cleaner = Preprocess()
    test_reviews = ["This is great!", "It is okay.", "Very bad."]

    for review in test_reviews:
        # 1. Clean
        cleaned = " ".join(cleaner.lemmatize(review))
        # 2. Vectorize
        vectorized = vectorizer.transform([cleaned])
        # 3. Predict
        prediction = model.predict(vectorized)[0]
        print(f"Review: {review} -> Rating: {prediction}")

test_prediction()