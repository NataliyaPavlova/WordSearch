#TESTS
import unittest
from word_search import Word

class TestWordMethods(unittest.TestCase):

    def setUp(self):
        self.length = 5
        self.letters="{'a':1}"
        self.filepath = "sentences.txt"
        self.case = Word(self.filepath, self.length, self.letters)
        self.case.make_dict()
    
    def test_conditions_list(self):
    
        #check if there is no letters' condition
        self.case.letters = None
        self.assertFalse(self.case.conditions_list())
        
        #check if a position of a letter is a number
        with self.assertRaises(SystemExit):
            self.case.letters = "{'a':w}"
            self.case.conditions_list()
        
        #check if there is one letter for a position, not 'ad':2
        with self.assertRaises(SystemExit):
            self.case.letters = "{'ad':2}"
            self.case.conditions_list()
        
        #check if ',' is a separator of letters' conditions
        with self.assertRaises(SystemExit):
            self.case.letters = "{'a':2;'n':3}"
            self.case.conditions_list()
        
        #check if ':' is a separator between a letter and a position 
        with self.assertRaises(SystemExit):
            self.case.letters = "{'a'-2}"
            self.case.conditions_list()
        

    def test_fit_parameters(self):
        self.case.conditions_list() #to create "letters_list" variable to make fit_parameters function work
        
        #check if the function works properly in an ordinary case
        self.assertTrue(self.case.fit_parameters('apple'))
        self.assertFalse(self.case.fit_parameters('banana'))
        
        #check if it stops the program whith wrong search parameters (letter position) 
        with self.assertRaises(SystemExit):
            self.case.letters = "{'a':10}"
            self.case.conditions_list() #new conditions -> new list
            self.case.fit_parameters('apple') 

      
    def test_search_word(self):
        
        #check if the function works properly in an ordinary case
        self.assertEqual(self.case.search_word(), 'apple')
        
        # check if length > max word's length in dict     
        self.case.length = 100
        self.assertEqual(self.case.search_word(), 'There is no such word...')
        
        # check if length < min word's length in dict
        self.case.length = -1
        self.assertEqual(self.case.search_word(), 'There is no such word...')
        
        
if __name__ == '__main__':
    unittest.main()