from flask import Flask
from markov_chain_nth import Markov_Chain
from format_text import planet_earth


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.



@app.route("/")
def home():
    chain = Markov_Chain(planet_earth, 3)
    sentence = chain.walk_markov_chain()
    return sentence


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
