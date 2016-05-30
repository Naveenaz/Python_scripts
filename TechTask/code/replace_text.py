#!/usr/bin/env python
#title           :replace_tests.py
#description     :This will create replacer function.
#author          :Naveen Zunjarwad
#date            :201600530
#version         :1.0.0
#notes           :Refer https://gist.github.com/sotsugov/e76b1988beac776616a6d62aa0c75782
#python_version  :2.7
#==============================================================================

__author__ = "Naveen Zunjarwad"
__version__ = "1.0.0"
__email__ = "jobfornaveeninuk@gmail.com"

'''replacer that can replace words in a string where the words are comma separated. It has 3 parameters, the first is the string to be altered, and the remaining two parameters are lists of words.

The first list contains the words to be replaced and the second list contains the replacement words, for example:

replacer(text, ["yes"], ["no"])
Replaces all instances of the word "yes" with the word "no" in the string text.

replacer(text, ["yes", "the"], ["no", "a"])
Replaces all instances of the word "yes" with the word "no" and all instances of "the" with the word "a" in the string text.

The function returns a list containing the updated string, a boolean flag which is set to true of the updates are successful and a summary of the number of replacements for each word.'''

def replacer(testString,first,second):
    print testString
    print first
    print second
    #countReplacements is a dictionary where "key" is each word and "value" is count of no of times word is replaced
    countReplacements={}
    concatinatedString=[]
    returningList=[]
    length_first=len(first)
    length_second=len(second)

    #Handling whole word case: This following for loop is added for the special case , when user specifies the part of the word in a string instead of whole word. Refer testcase:test_whole_word()
    for i in range(0, length_first):
        if first[i] in testString:   # This line required, so that user can still specify non-existing word as input.
            returnValue=word_in(first[i],testString)
            if returnValue==False:
                print "Test String do not contain this whole word: %s" %first[i]
                return testString
    #loop complete.

    if length_first != length_second:
        flag=False
        returningList=testString.split()
        returningList.append(flag)
        returningList.append("List lengths do not match")
        return returningList
    else:
        flag = True

        for i in range(0,length_first):
            #print first[i]
            #print testString.count(first[i])
            countReplacements[first[i]]=testString.count(first[i])
            testString=testString.replace(first[i],second[i])

        returningList=testString.split()
        returningList.append(flag)
        for key,value in sorted(countReplacements.iteritems(), key=lambda (k,v): (v,k),reverse=True):
            if value != 1:
                stringCount="%s: replaced %s times"%(key,value)
            else:
                stringCount = "%s: replaced %s time" % (key, value)
            concatinatedString.append(stringCount)

        returningList.append(''.join(concatinatedString))
        return returningList

#This function is needed if we want to check whether the "whole" word exist in the testString or not. Return True if whole word exists, else False.
def word_in(word, phrase):
    return word in phrase.split(",")


#resulted_string,flag,countReplacements=replacer(a,f,s)

#if flag:
 #   print "Updates are successful."
  #  print "Resulted string after update:  %s" %resulted_string
   # print "No of occurances of each word"
    #print countReplacements
#else:
 #   print "List lengths do not match."
