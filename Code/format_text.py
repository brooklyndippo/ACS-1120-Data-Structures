from string import punctuation
import os

def format_text(directory, file):
    
    word_list = []     
    route = f'./{directory}/{file}'

    with open(route, "r") as file:
        for line in file:
            for word in line.split():
                #strip the punctionation from both sides of the word & # edit- do not convert to lowercase
                word = word.lstrip(punctuation).rstrip(punctuation).strip('\n').lower()
                word_list.append(word)

    return word_list

def compile_corpus(directory):

    corpus = []

    for file in os.listdir(directory):
        word_list = format_text(directory,file)
        print(file)
        print(len(word_list))
        for word in word_list:
            corpus.append(word)

    return corpus


planet_earth = compile_corpus('./corpus')
print(len(planet_earth))
