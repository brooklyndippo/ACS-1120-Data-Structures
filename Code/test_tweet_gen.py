from markov_chain_nth import Markov_Chain
from format_text import planet_earth


chain = Markov_Chain(planet_earth, 3)
chain.walk_markov_chain()