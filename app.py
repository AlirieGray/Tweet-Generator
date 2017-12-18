#!python3.6
import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from dictogram import Dictogram
import time
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

mx = Dictogram('corpus.txt')

# database model for Tweet
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), unique=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Tweet %r>' % self.content

# home route
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        tweet = mx.generate_sentence()
        # keep track of the current tweet in case a user favorites it
        global current_tweet
        current_tweet = tweet
        return render_template('index.html', tweet=tweet, time=time.time())
    elif request.method == 'POST':
        addFavoriteTweet(current_tweet)
        return render_template('index.html', tweet=current_tweet, time=time.time())

# display favorites
@app.route('/favorites', methods=['GET'])
def fav():
    # try to get content of tweets in db
    tweets_list = Tweet.query.all()
    tweet_strings = []
    for tweet in tweets_list:
        tweet_strings.append(tweet.content)
    return render_template('favorites.html', tweets=tweet_strings, time=time.time())

# add favorited tweet to the database
def addFavoriteTweet(tweet_content):
    tweet = Tweet(tweet_content)
    db.session.add(tweet)
    db.session.commit()
    print(Tweet.query.all())

# empty the database
def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print ('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()

if __name__ == "__main__":
    app.run()
