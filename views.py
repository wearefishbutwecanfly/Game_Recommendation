from flask import Flask, Blueprint, redirect, url_for, render_template, request, redirect, session
import pandas as pd
from content_based import content_based_recommend
from SVD import SVD, hybrid
from models import User, Rating
from init import db
import random
import csv

views = Blueprint('views', __name__)

df = pd.read_csv("steam_api.csv")
df["Rating"] = ((df["Rating"].fillna(0)).astype(int)).astype(str)

# Home Page
@views.route("/", methods = ['GET','POST'])
def index():
    if session.get('logged_in'):
        with open(r'user_rating.csv','w') as f:
            header = ["ID", "User_ID","Game_id", "Game_name","Rating"]
            users = db.session.query(Rating.id, Rating.user_id, Rating.game_id,Rating.game_name,Rating.rating)
            csv_out = csv.writer(f)
            csv_out.writerow(header)
            for user in users:
                csv_out.writerow(user)

        user_name = session.get("username")
        top_Rating = df.sort_values(by = "Rating", ascending = False)[:100]
        top_forever = df.sort_values(by = "average_forever", ascending = False)[:100]
        top_positive = df.sort_values(by=['positive','negative'], ascending = False)[:100]
        user_recommend = df.iloc[SVD(session.get('user_id'),20, 100,top_Rating)['Game_index']]
        # list2 = random.sample(range(19233), 20)
        return render_template("home.html", top_Rating= top_Rating, user_recommend = user_recommend, top_forever=top_forever, top_positive= top_positive, user_name = user_name)
    else:
        return render_template("index.html")

#Register Page
@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('views.login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')

#Login Page
@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            session["user_id"] = data.id
            session["username"] = data.username
            return redirect(url_for('views.index'))
        return render_template('index.html', message="Incorrect Details")

#Logout 
@views.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('views.index'))


#Detail Page
@views.route("/detail/<game_id>",methods=['GET', 'POST'])
def detail(game_id):
    user_id = session.get('user_id')
    game_index = int(df[df["Game_id"]==int(game_id)].index[0])
    # list2 = random.sample(range(19233), 20)
    game_detail = df.loc[df["Game_id"]==int(game_id)].squeeze()
    game_name = str(game_detail["Game_name"])
    list_game_recommend = content_based_recommend(game_index, 20)
    list_game_hybrid = hybrid(user_id, game_index, game_name, 30, 20)['Game_index']

    if request.method == "POST":
        rating = request.form.get('rating')

        data = Rating.query.filter_by(user_id=user_id, game_id=game_id, game_name=game_name).first()
        if data is not None:
            data.rating = rating
            # Rating.query.filter_by(username='admin').update(dict(rating=rating))
            db.session.commit()
        else:
            db.session.add(Rating(user_id=user_id, game_id=game_id, game_name = game_name, rating = rating))
            db.session.commit()
        # print("Import done")

    return render_template("detail.html", game_detail=game_detail, df = df, list_game_recommend=list_game_recommend, list_game_hybrid=list_game_hybrid)