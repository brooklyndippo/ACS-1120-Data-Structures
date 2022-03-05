from flask import Flask, request, render_template, redirect
from markov_chain_nth_sentences import Markov_Chain
from parse_sentence_structure import planet_earth
import twitter


app = Flask(__name__)
markov_chain = Markov_Chain(planet_earth, 2)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.

@app.route('/')
def home():
    sentence = markov_chain.walk_markov_chain()
    return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    print(status)
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
