from flask import Flask
from Code.format_text import format_text
from format_text import format_text
from markov_chain import Markov_Chain, random_words


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.



@app.route("/")
def home():
    planet_earth = format_text('./planet_earth.txt')
    chain = Markov_Chain(planet_earth)
    sentence = chain.walk_markov_chain()
    return sentence


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
