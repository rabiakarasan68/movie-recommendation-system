import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset yükleme
df = pd.read_csv("movies.csv")

# Eksik değerleri temizleme
df["genres"] = df["genres"].fillna("")

# TF-IDF
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["genres"])

# Cosine similarity
similarity = cosine_similarity(tfidf_matrix)
