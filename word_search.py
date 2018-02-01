import codecs
import sys
import re
import argparse


class Dict:
    
    def __init__(self, filepath):
        self.filepath = filepath
        
    def make_dict(self):  #make a dictionary of words; group words by their lengths
        with codecs.open(self.filepath, encoding = "utf8") as f:
            data_list=list(f)

        data_list = list(map(lambda x: x.lower(), data_list)) #all words to lower register
        data_list = list(map(lambda x: re.split("[^a-z-']", x), data_list)) #delete all punctuation 

        self.dict = {}  
        for line in data_list:
            for word in line:
                word_length = len(word)
                if word_length in self.dict.keys(): 
                    self.dict[word_length].append(word)
                else:
                    self.dict[word_length] = [word]
        self.dict.pop(0)  #delete all empty words
        #return self.dict

    
class Word(Dict):

    def __init__(self, filepath, length, letters):
        Dict.__init__(self, filepath)
        self.length = length
        self.letters = letters
    
    
    def conditions_list(self):
    #makes from letters string a dictionary of letter conditions (self.letters_list) like {1:'a', 2:'b', 3:'c'}
        if (self.letters is None):  #then we can return first met word with given length
            return False
        
        self.letters_list={}
        self.letters = self.letters[1:-1].split(',')
        
        if (len(self.letters)==1) and (len(self.letters[0])>5): #check if ',' is a separator of letters' conditions
            print 'Wrong punctuation in the input.'
            raise SystemExit
        
        for condition in self.letters:
            
            condition = condition.split(':')
            
            if (len(condition)==1):      #check if ':' is a separator between a letter and a position 
                print 'Wrong punctuation in the input.'
                raise SystemExit
            
            if len(condition[0])!=3:   #check if letter input is ok
                print 'Wrong input: ',condition[0]
                raise SystemExit
            letter = condition[0][1]
    
            try:                      #check if position of the letter is ok
                position = int(condition[1])-1
            except ValueError:
                print 'Wrong input: ',condition[1]
                raise SystemExit
            #print letter, position
            
            self.letters_list[position]=letter
        return True
    
    def fit_parameters(self, word):  
    #check if the word fits given letter conditions
        fit = True
        for position in self.letters_list.keys():
            
            try:  
                if position>len(word): raise IndexError
            except IndexError:
                print "Wrong input: letter's position is bigger then word's length: ",position+1
                raise SystemExit

            if not (word[position]==self.letters_list[position]): 
                fit = False
                #print self.letters_list[position], position, word
                return fit
        return fit
    

    def search_word(self):  #look through the words with given length  
        answer = 'There is no such word...'
        if not (self.length in self.dict):
            return answer
        answers_list = self.dict[self.length]
        i = self.conditions_list()
        if i==False:   #then we can return first met word with given length
            return answers_list[0]
        for word in answers_list:
            if self.fit_parameters(word): 
                answer = word
                break
        return answer

'''
def _main():    
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', help='Length of word, obligatory parameter, should be integer', type=int)
    parser.add_argument('--letters', help="Known letters, the format is as {'a':1,'b':2}")
  
    args = parser.parse_args()

    filepath = "sentences.txt"
    
    answer = Word(filepath, args.length, args.letters)
    answer.make_dict()
    
    if args.length:
        print answer.search_word()
    else:
        print('Wrong input: there is no length condition.')
        raise SystemExit
    
    
    
    
if __name__ == "__main__":
    _main()
'''