import random
from format_text import format_text
from dictogram import Dictogram

planet_earth = format_text('./corpus', 'life_that_glows.txt')
random_words = ["peanut", "butter", "jelly", "butter", "peanut", "butter","jelly", "butter","peanut", "jelly", "butter", "toast", "time"]

class Markov_Chain(Dictogram):
    """Markov Chain is a complex histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None, n=5):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov_Chain, self).__init__()
        self.word_list = word_list
        self.n = n
        self.types = 0
        self.tokens = 0
        if word_list is not None and len(word_list) > (self.n + 1):
            self.build_chain()

    
    def build_chain(self):
        index = self.n #start the index at our n value, this is actually the END of our key
        while index < (len(self.word_list)):
            #assign the words & put into a tuple
            counter = self.n #set a second counter 5
            tuple_words = []

            while counter > 0:
                word = self.word_list[index-counter]
                tuple_words.append(word)
                counter -= 1
            tuple_key = tuple(tuple_words)


            #store the next value
            next_word = self.word_list[index]

            #if tuple is not in our dictionary, then add it with a value of a dictionary
            if tuple_key not in self:
                self[tuple_key] = Dictogram() 
            
            #add the next word into the sub-dictionary for the tuple
            self[tuple_key].add_count(next_word)
        
            index += 1
    
        #print(self)
        return self

    def walk_markov_chain(self):
        
        sentence_length = random.randint(15,20)
        text_length = (len(self.word_list)-self.n)
        start = random.randint(0, text_length)
        sentence = []
        
        counter = 0
        tuple_words = []
        while counter < self.n:
            word = self.word_list[start+counter]
            tuple_words.append(word)
            sentence.append(word)
            counter += 1
       

        current_tuple = tuple(tuple_words)
        
        next_word = self[current_tuple].sample()
        sentence.append(next_word)
    

        
        while len(sentence) < sentence_length:


            tuple_slice = current_tuple[1:self.n]
            next_tuple_list = list(tuple_slice)
            next_tuple_list.append(next_word)
            
            current_tuple = tuple(next_tuple_list)
            
            if current_tuple in self:
                next_word = self[current_tuple].sample()
                sentence.append(next_word)
            else:
                break
        
        sentence = ' '.join(sentence)
        print(sentence)
        return sentence




if __name__ == '__main__':
    planet_earth = format_text('./planet_earth.txt')
    chain = Markov_Chain(planet_earth, 3)
    chain.walk_markov_chain()
