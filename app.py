from flask import Flask
import stochastic
import histogram
app = Flask(__name__)

@app.route('/')
def hello():
    normalized_string = (histogram.normalize(histogram.read_in_file('fish.txt')))
    fish_words = histogram.create_dict(normalized_string)
    fish_probs = stochastic.probability_dictionary(fish_words)
    probs_list = stochastic.create_probs_list(fish_probs)
    return stochastic.random_weighted(probs_list)

if __name__ == "__main__":
    app.run()
