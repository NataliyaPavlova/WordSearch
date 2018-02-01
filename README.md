## WordSearch
Looking for a word in a text from sentences.txt according to given parameters. Tests are in "tests.py" file (unit tests).

### how to use:

launch from a command line: 

$ python word_search.py --length 5 --letters {'o':1,'d':4}


### search parameters requirements:

length is a obligitory requirement, should be integer.

in braces there are letters requirements: given letter should be on a given position (numbering is from '1').

in the example above the require word has 5 letters, 'o' is first, 'd' is fourth. The number of "letter parameters" may be >= 0.


### what to get:

the program prints first word met the parameters or an error message.
