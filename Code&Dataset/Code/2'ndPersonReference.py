ignore_list = [
'you',
'they',
'he',
'she',
'them',
'your',
'you all',
'yall',
'it',
'their',
'his',
'hers',
'its',
'theirs'
]

def others(filename):
    infile = open(filename)
    with open(filename) as f:
        #create a list of all words fetched from the file using a list comprehension
        words = [word for line in f for word in line.split()]
    print ("Out of the total :", len(words))
    counter = 0
    for line in infile:
        line = line.lower()
        if any(word in line for word in ignore_list):
            counter = counter + 1
    print("# of grammer errors found are: ",counter)
    f.close()
    infile.close()
