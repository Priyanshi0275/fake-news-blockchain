import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
fake = pd.read_csv("dataset/Fake.csv")
real = pd.read_csv("dataset/True.csv")

fake["label"] = 1
real["label"] = 0

data = pd.concat([fake, real])
data = data.sample(frac=1)

X = data["text"]
y = data["label"]

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

X_vec = vectorizer.fit_transform(X)

# Train classifier
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)


def predict_news(news_text):

    vec = vectorizer.transform([news_text])

    prob = model.predict_proba(vec)[0][1]

    return float(prob)