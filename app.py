from flask import Flask, request, render_template
import stochastic
import histogram
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    '''
    num = request.args.get('num', default = 10, type = int)
    normalized_string = (histogram.normalize(histogram.read_in_file('blue.txt')))
    blue_words = histogram.create_dict(normalized_string)
    probs_list = stochastic.create_ranges_list(blue_words)
    return_list = []
    for i in range(num):
        return_list.append(stochastic.random_weighted(probs_list))
    return " ".join(return_list)
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
