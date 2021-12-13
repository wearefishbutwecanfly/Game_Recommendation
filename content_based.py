import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
# from training_data import df, tfidf

df = pd.read_csv("steam_api.csv")

print("Training tfidf")
tfidf_vectorizer = TfidfVectorizer(analyzer='word', strip_accents = 'unicode',stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(list(df['Game_description']))
print("Complete")

def content_based_recommend(game_index, max_number):
    # game_index = df [df ["Game_id"]==game_id].index[0]
    similarities = linear_kernel(tfidf[game_index],tfidf).flatten()
    related_docs_indices = (-similarities).argsort()[1:(max_number+1)]
    return related_docs_indices


