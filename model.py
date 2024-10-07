import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle as pkl

# Load the dataset
movies = pd.read_csv("dataset.csv")

# Select relevant columns
movies = movies[["id", "title", "overview", "genre"]]

# Create tags by combining 'overview' and 'genre'
movies["tags"] = movies["overview"] + movies["genre"]

# Drop unnecessary columns
new_data = movies.drop(columns=["overview", "genre"])

# Vectorize the 'tags' column
cv = CountVectorizer(max_features=10000, stop_words="english")
vector = cv.fit_transform(new_data["tags"].values.astype("U")).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vector)

# Save the 'new_data' and 'similarity' models
with open("movies_list.pkl", "wb") as file:
    pkl.dump(new_data, file)

with open("similarity.pkl", "wb") as file:
    pkl.dump(similarity, file)

print("Models saved successfully.")