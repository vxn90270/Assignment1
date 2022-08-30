sentence = "I am a teacher and I love to inspire and teach people"

# how many unique words have been used in the sentence? Use the split methods and set to get the unique words.
words = [n.lower() for n in sentence.split(" ")]
print("number of unique words: ", len(list(set(words))))