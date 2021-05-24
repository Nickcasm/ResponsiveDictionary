from difflib import SequenceMatcher
from difflib import get_close_matches # to get all the matching words
import json
data = json.load(open("data.json")) # Returns dictionary of json file

def findMeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        word = get_close_matches(word,data.keys(),cutoff=0.8)[0]
        wordcheck = input("Do you mean {}? y/N ".format(word))
        if wordcheck in "yY":
            return data[word]
        elif wordcheck in "nN":
            return "Word dosen't exist please double check it..."  
        else:
            return "We did't understand your query..."      
    else:
        return "Oops...!! Not the correct word, Check it again"    

word = input("Enter Word: ")
wordMeanings = findMeaning(word)
if type(wordMeanings) == list:
    for meaning in wordMeanings:
        print(meaning)
else:
    print(wordMeanings)        