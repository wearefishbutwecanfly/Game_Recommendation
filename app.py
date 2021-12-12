from flask import Flask, redirect, url_for, render_template
import pandas as pd
from sort_value import df, top10_Rating, top10_forever, top10_positive
import random

app = Flask(__name__)
app.secret_key = "Game recommendation"


@app.route("/")
def home():
    return render_template("index.html",top10_Rating= top10_Rating, top10_forever=top10_forever, top10_positive= top10_positive)
    # return render_template("index.html", df = df)

@app.route("/detail/<game_id>",methods=['GET', 'POST'])
def detail(game_id):
    list1 = random.sample(range(20000), 5)
    list2 = random.sample(range(20000), 5)
    game_detail = df.loc[df["Game_id"]==int(game_id)].squeeze()
    return render_template("detail.html", game_detail=game_detail, df = df, list1=list1, list2=list2)
    

if __name__ == "__main__":
    app.run(debug=True, port=2300)