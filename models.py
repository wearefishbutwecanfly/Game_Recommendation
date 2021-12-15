from init import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    ratings = db.relationship('Rating')

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    game_id = db.Column(db.Integer, unique=True)
    game_name = db.Column(db.String, unique=True)
    rating = db.Column(db.Integer)
