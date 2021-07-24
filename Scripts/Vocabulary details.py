# Script to convert story text to vocab text.

import os
import re
import string
from tqdm import tqdm

chars = string.punctuation
chars = chars.replace("`", "")
chars = chars.replace("'", "")


files = ["","",] # Enter all files name.


total_words = 0

# Word Level

for i in tqdm(files):
    f = open(i)
    rFiles = f.read()
    f.close()
    rFiles = rFiles.replace(" '", '"')
    rFiles = rFiles.replace("' ", '"')
    rFiles = rFiles.replace(" `", '"')
    rFiles = rFiles.replace("` ", '"')
    rFiles = re.sub("\n\n+", "qwerty", rFiles)
    rFiles = rFiles.replace("\n", " ")
    for c in chars:
        rFiles = rFiles.replace(c," "+c+" ")
    rFiles = rFiles.replace("\t", " ")
    rFiles = rFiles.replace("*", " ")
    f = open(os.path.splitext(i)[0]+"_formatted.txt", "w")
    f.write(rFiles)
    f.close()
    rFiles = rFiles.lower()
    file_words = rFiles.split()
    vocab = set(file_words)
    total_words = total_words + len(file_words)
    f = open("word_vocab_details.txt", "a")
    f.write("\nFile Name : "+i)
    f.write("\nTotal Words : "+str(len(file_words)))
    f.write("\nTotal Vocab : "+str(len(vocab)))
    f.write("\n\n")
    f.close()
    f = open(os.path.splitext(i)[0]+"_word_vocabs.txt", "w")
    f.write(str(rFiles))
    f.close()
    f = open("all_word_vocabs.txt", "a")
    f.write(str(rFiles))
    f.close()


f = open("all_word_vocabs.txt")
text = f.read()
f.close()

text = text.lower()
text = text.split()
total_vocab = set(text)


f = open("word_vocab_details.txt", "a")
f.write("\nTotal Vocab and Words in whole file : ")
f.write("\nTotal Words : "+str(total_words))
f.write("\nTotal Vocab : "+str(len(total_vocab)))
f.write("\n\n")
f.close()



# Charcter level

import os
from tqdm import tqdm

files = ["",""] # Enter all files name.


for i in tqdm(files):
    f = open(i)
    rFiles = f.read()
    f.close()
    vocabulary = sorted(list(set(rFiles))) 
    char_to_indices = dict((c, i) for i, c in enumerate(vocabulary)) 
    indices_to_char = dict((i, c) for i, c in enumerate(vocabulary)) 
    f = open("char_vocab_details.txt", "a")
    f.write("\nFile Name : "+i)
    f.write("\nTotal Vocab : "+str(len(vocabulary)))
    f.write("\n\n")
    f.close()
    f = open(os.path.splitext(i)[0]+"_char_vocabs.txt", "w")
    f.write(str(vocabulary))
    f.close()
    f = open("all_char_vocabs.txt", "a")
    s = str(vocabulary) 
    f.write(s[1:-1])
    f.close()
