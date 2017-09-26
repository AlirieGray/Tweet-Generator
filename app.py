from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import stochastic
import histogram
import time
import json
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), unique=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Tweet %r>' % self.content


@app.route('/', methods=['GET', 'POST'])
def hello():
    num = request.args.get('num', default = 10, type = int)
    normalized_string = (histogram.normalize(histogram.read_in_file('blue.txt')))
    blue_words = histogram.create_dict(normalized_string)
    probs_list = stochastic.create_ranges_list(blue_words)
    return_list = []
    for i in range(num):
        return_list.append(stochastic.random_weighted(probs_list))
    tweet =  " ".join(return_list)
    if request.method == 'GET':
        return render_template('index.html', tweet=tweet, time=time.time)
    elif request.method == 'POST':
        print("Posting!")
        addFavoriteTweet(tweet)
        return render_template('index.html', tweet=tweet, time=time.time)

@app.route('/favorites', methods=['GET'])
def fav():
    # try to get content of tweets in db
    tweets_list = Tweet.query.all()
    tweet_strings = []
    print("Printing all content")
    for tweet in tweets_list:
        tweet_strings.append(tweet.content)
    return render_template('favorites.html', tweet=tweet_strings)

def addFavoriteTweet(tweet_content):
    tweet = Tweet(tweet_content)
    db.session.add(tweet)
    db.session.commit()
    print(Tweet.query.all())

if __name__ == "__main__":
    app.run()
