import random
from format_text import format_text
from dictogram import Dictogram

random_words = ["peanut", "butter", "jelly", "butter", "jelly", "peanut", "jelly", "butter", "toast", "time"]

class Markov_Chain(Dictogram):
    """Markov Chain is a complex histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None, n=2):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov_Chain, self).__init__()
        self.word_list = word_list
        self.n = n
        self.types = 0
        self.tokens = 0
        if word_list is not None and len(word_list) > (self.n + 1):
            self.build_chain()

    
    def build_chain(self):
        index = 0
        while index < (len(self.word_list) - (self.n)):
            #assign the words & put into a tuple
            word_1 = self.word_list[index]
            word_2 = self.word_list[index + 1]
            tuple = (word_1, word_2)

            #store the next value
            next_word = self.word_list[index + 2]

            #if tuple is not in our dictionary, then add it with a value of a dictionary
            if tuple not in self:
                self[tuple] = Dictogram() 
            
            #add the next word into the sub-dictionary for the tuple
            self[tuple].add_count(next_word)
        
            index += 1
    
        #print(self)

        return self

    def walk_markov_chain(self):
        
        sentence_length = random.randint(15, 20)
        text_length = len(self.word_list)
        start = random.randint(0, text_length)
        word_1 = self.word_list[start]
        word_2 = self.word_list[start+1]
    
        sentence = []


        current_tuple = (word_1, word_2)
        sentence.append(word_1)
        sentence.append(word_2)
        next_word = self[current_tuple].sample()
        index = 1


        while index < sentence_length:
            current_tuple = (current_tuple[1], next_word)
            sentence.append(current_tuple[1])
            if current_tuple in self:
                next_word = self[current_tuple].sample()
                print(next_word)
                index += 1
            else:
                index = sentence_length

        #sentence = sentence.join(' ')
        sentence = ' '.join(sentence)
        print(sentence)
        return sentence




if __name__ == '__main__':
    planet_earth = format_text('./planet_earth.txt')
    chain = Markov_Chain(planet_earth)
    chain.walk_markov_chain()


# def markov_chain:
# - modify current histogram code
# - instead of getting count for each word, we can get the next word and store it in that key’s value (another dictionary) following our classic histogram
# expected output: {“like”: {dogs: 2, cats: 1}, “dogs”: {and: 1, *END*: 1} .. }
# def higher_order_markov_chain:
# - loop through text
# - generate tuple of two word pairs to store as key
# - store the next word histogram-style in the value (which is also a dictionary)
# expected output: {(I, like) : {dogs: 1, cats: 1}, (dogs, and) : {you: 1} ….. }

# def create_markov(word_list):
#     take in a word list
#     iterate every two words (if they exist)
#     [i]
#     [i + 1]
#     put both words in a tuple
#     Check if this tuple was in a dictionary,
#         if it was, increment the count for the next word (+1)
#         else: make a new entry with the value being the next word initialized to 1
#     return markov chain
# markov_chain = create_markov(word_list)
# example = {
#     (cats, I) : {
#         like: 1
#     },
#     (I, like): {
#         dogs: 1,
#         cats: 1
#     },
#     (like, dogs): {
#         and: 1,
#     },
# }
# seed the first word to be the first word of the word list (“I”)
# sentence = wordlist[0]
# “I like dogs”
# loop for until we hit our sentence length limit:
#     check if sentence[-1] is in any of the tuples[1] keys in our markov_chain,
#     and then use sample() function to choose the next word from that histogram,
#     append that word to the sentence
# return sentence

