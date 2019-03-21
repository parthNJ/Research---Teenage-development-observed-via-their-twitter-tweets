import re
import sys
from collections import Counter
def words_and_count(filename):
    input_file = open(filename, 'r')
    lower_string = input_file.read().lower()
    word_count = {}
    for word in lower_string.replace(',', ' ').split():
        word_count[word] = word_count.setdefault(word, 0) + 1
    print(word_count, "\n")
    

def print_word_counts(count, minimu):
    temp = 0
    for k, v in count.items():
        temp = temp+v
    for k, v in count.items():
        if v >= minimu:
            print(k,v)
    return total
        

#4 searching for words with a number of frequency
def frequency_above(filename, frequency_of_words_above):
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    word_count = {}
    for word in source_string.replace(',', ' ').split():
        word_count[word] = word_count.setdefault(word, 0) + 1
    for (word, frequency) in word_count.items():
        if frequency > frequency_of_words_above:
            print(word, frequency)
   
            
    
def frequency():
    #use open() for opening file.
    #Always use `with` statement as it'll automatically close the file for you.
    with open(r'levi1.txt') as f:
        #create a list of all words fetched from the file using a list comprehension
        words = [word for line in f for word in line.split()]
        print ("The total word count is:", len(words))
       
        
