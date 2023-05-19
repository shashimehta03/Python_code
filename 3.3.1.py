from collections import Counter
def word_count(fname):
        with open(fname) as f:
           return Counter(f.read().split())
        print("Number of words in the file :",word_count("test.txt"))


# import string 
# for letter in string.ascii_letters:
#    fd = open (letter + ".txt", "w") 
#    fd.close()