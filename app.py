from flask import Flask, request, render_template
import stochastic
import histogram
import time
app = Flask(__name__)

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
        return render_template('index.html', tweet=tweet, time=time.time)

@app.route('/favorites', methods=['GET', 'POST'])
def fav():
    return render_template('favorites.html', tweet="Placeholder")

if __name__ == "__main__":
    app.run()
