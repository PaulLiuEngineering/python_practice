import random
import sys
def roll():
    b = int(random.random() * 6) + 1
    print(b)

c = 0
while(c == 0):
    a = input("Would you like to roll a dice?[y/n]")
    if a == 'y':
        roll()
    elif a== 'n':
        print('Program ended')
        c+=1
    else:
        print('Invalid request')

