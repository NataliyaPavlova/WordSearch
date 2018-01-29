import codecs
import sys
import re

def make_dict(filepath):  #make a dictionary of words; group words by their lengths
    with codecs.open(filepath, encoding = "utf8") as f:
        data_list=list(f)

    data_list = list(map(lambda x: x.lower(), data_list)) #all words to lower register
    data_list = list(map(lambda x: re.split('[^a-z]', x), data_list)) #delete all punctuation 

    dict = {}  
    for line in data_list:
        for word in line:
            word_length = len(word)
            if word_length in dict.keys(): 
                dict[word_length].append(word)
            else:
                dict[word_length] = [word]
    dict.pop(0)  #delete all empty words
    return dict

def fit_parameters(search_parameters, word):  #check if the word fits given conditions
    fit = True
    for condition in search_parameters:
        letter = condition[0]
        place_ind = int(condition[3])-1
        if not word[place_ind]==letter: 
            fit = False
            break
    return fit

def search_word(search_parameters, dict):  #look through the words with given length  
    search_parameters = search_parameters.split(r"{'")
    answer_len = int((re.findall('(\d+)', search_parameters[0]))[0])
    answers_list = dict[answer_len]
    answer = 'There is no such word...'
    for word in answers_list:
        if fit_parameters(search_parameters[1:],word): 
            answer = word
            break
    return answer
    
    
def _main():    
    search_parameters = sys.argv[1]
    #search_parameters = "(11, {'p':1})"
    #print search_parameters
    filepath = "sentences.txt"
    dict = make_dict(filepath)
    answer = search_word(search_parameters, dict)
    print answer
    
    
if __name__ == "__main__":
    _main()