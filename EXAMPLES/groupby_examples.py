from itertools import groupby

with open('../DATA/words.txt') as words_in:  # open file for reading
    # create generator of all words, stripped of the trailing '
    all_words = (w.rstrip() for w in words_in)  

    # create a groupby() object where the key is the first character in the word
    g = groupby(all_words, key=lambda e: e[0])  

    # make a dictionary where the key is the first character, and the value 
    # is the number of words that start with that character; groupby groups 
    # all the words, then len() counts the number of words for that character
    counts = {letter: len(list(wlist)) for letter, wlist in g}  

# sort the counts dictionary by value (i.e., number of words, not the letter
#  itself) into a list of tuples
sorted_letters = sorted(counts.items(), key=lambda e: e[1], reverse=True)

# loop over the list of tuples and print the letter and its count
for letter, count in sorted_letters: 
    print(letter, count)
print()

# sum all the individual counts and print the result
print("Total words counted:", sum(counts.values()))
