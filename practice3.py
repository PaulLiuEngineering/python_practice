import random
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
n = len(WORDS)
word = WORDS[random.randint(0,n-1)]
print(word)
# c = 12
# while(c > 0):
#     letter = input("Guess a letter:  ")
#     if letter in word:
#         a = 0
#         show
#         for a in len(word):
#             if word[a] == letter
#         print("")