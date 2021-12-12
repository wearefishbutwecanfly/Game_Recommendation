import pandas as pd
df = pd.read_csv("full_steam_api.csv")
df["Rating"] = ((df["Rating"].fillna(0)*100).astype(int)).astype(str)

top10_Rating = df.sort_values(by = "Rating", ascending = False)[:100]
top10_forever = df.sort_values(by = "average_forever", ascending = False)[:100]
top10_positive = df.sort_values(by=['positive','negative'], ascending = False)[:100]


