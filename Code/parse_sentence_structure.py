import os
from string import punctuation
import re

def format_text(directory, file):
    
    word_list = ['START']     
    route = f'./{directory}/{file}'

    #string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    #punctuation = '\.\:\;\"\,\!' 
    #sentence_structure = re.sub('. ', 'START END')
    #LAUGHTER

    with open(route, "r") as file:
        for line in file:
            mod_line = re.sub('\.', " END START ", line)
            #print(mod_line)
            for word in mod_line.split():

                #strip the punctionation from both sides of the word & # edit- do not convert to lowercase
                word = word.lstrip(punctuation).rstrip(punctuation).strip('\n')
               
                if word not in "END START":
                    if word_list[-1] != "START":
                        word = word.lower()
                word_list.append(word)
    #print(word_list)
    return word_list

def compile_corpus(directory):

    corpus = []

    for file in os.listdir(directory):
        word_list = format_text(directory,file)

        for word in word_list:
            corpus.append(word)

    return corpus


#planet_earth = format_text('./corpus', 'life_that_glows.txt')
planet_earth = compile_corpus('./corpus')
#print(len(planet_earth))