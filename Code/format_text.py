from string import punctuation

def format_text(file):
    
    word_list = []      

    with open(file, "r") as file:
        for line in file:
            for word in line.split():
                #strip the punctionation from both sides of the word & # edit- do not convert to lowercase
                word = word.lstrip(punctuation).rstrip(punctuation).strip('\n').lower()
                word_list.append(word)

    return word_list