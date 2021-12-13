from flask import Flask, redirect, url_for, render_template
import pandas as pd
from content_based import content_based_recommend
import random

app = Flask(__name__)
app.secret_key = "Game recommendation"

df = pd.read_csv("steam_api.csv")
df["Rating"] = ((df["Rating"].fillna(0)).astype(int)).astype(str)

@app.route("/")
def home():
    top_Rating = df.sort_values(by = "Rating", ascending = False)[:100]
    top_forever = df.sort_values(by = "average_forever", ascending = False)[:100]
    top_positive = df.sort_values(by=['positive','negative'], ascending = False)[:100]
    return render_template("index.html",top_Rating= top_Rating, top_forever=top_forever, top_positive= top_positive)
    # return render_template("index.html", df = df)

@app.route("/detail/<game_id>",methods=['GET', 'POST'])
def detail(game_id):
    game_index = df[df["Game_id"]==int(game_id)].index[0]
    list2 = random.sample(range(19233), 20)
    game_detail = df.loc[df["Game_id"]==int(game_id)].squeeze()
    list_game_recommend = content_based_recommend(game_index, 20)

    return render_template("detail.html", game_detail=game_detail, df = df, list_game_recommend=list_game_recommend, list2=list2)
    

if __name__ == "__main__":
    app.run(debug=True, port=2300)