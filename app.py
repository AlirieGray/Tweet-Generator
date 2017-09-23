from flask import Flask
import stochastic
import histogram
app = Flask(__name__)

@app.route('/')
def hello():
    normalized_string = (histogram.normalize(histogram.read_in_file('blue.txt')))
    blue_words = histogram.create_dict(normalized_string)
    blue_probs = stochastic.probability_dictionary(blue_words)
    probs_list = stochastic.create_probs_list(blue_probs)
    return_list = []
    for i in range(10):
        return_list.append(stochastic.random_weighted(probs_list))
    return " ".join(return_list)

if __name__ == "__main__":
    app.run()
