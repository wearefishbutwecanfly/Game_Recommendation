import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity


df = pd.read_csv("steam_api.csv",encoding = 'utf-8')

print("Training tfidf")
tfidf_vectorizer = TfidfVectorizer(analyzer='word', strip_accents = 'unicode',stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(list(df['Game_description']))
print("Complete training tfidf")

def content_based_recommend(game_index, max_number):
    # game_index = df [df ["Game_id"]==game_id].index[0]
    similarities = linear_kernel(tfidf[game_index],tfidf).flatten()
    related_docs_indices = (-similarities).argsort()[1:(max_number+1)]
    print(type(similarities))
    return related_docs_indices


# predict = content_based_recommend(df[df['Game_id']==427520].index[0], 20)
# list_predict_game = df.iloc[predict]['Game_name']
# for i in list_predict_game:
#     print(i)