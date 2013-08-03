#Counting number of unique words in a file and also counting the frequency of each word 


from string import punctuation
from collections import defaultdict

import re

number = 10000
words = {}
total_unique = 0
words_only = re.compile(r'^[a-z]{2,}$')
counter = defaultdict(int)


"""Define words as 2+ letters"""
def count_unique(s):
    count = 0
    if word in line:
        if len(word) >= 2:
            count += 1
    return count


"""Open text document, read it, strip it, then filter it"""
txt_file = open('reverse_list.py', 'r')

for line in txt_file:
    for word in line.strip().split():
        word = word.strip(punctuation).lower()
        if words_only.match(word):
            counter[word] += 1


# Most Frequent Words
top_words = sorted(counter.iteritems(),
                    key=lambda(word, count): (-count, word))[:number]

print "Most Frequent Words: "

for word, frequency in top_words:
    print "%s: %d" % (word, frequency)


total_unique = len(counter.keys())

# Total Unique Words:
print " "
print "Total Number of Unique Words: %s " % total_unique

#########OUTPUT###########

#Most Frequent Words: 
#method: 5
#print: 5
#in: 2
#for: 1
#list: 1
#python: 1
#reversing: 1
#the: 1
 
#Total Number of Unique Words: 8 


