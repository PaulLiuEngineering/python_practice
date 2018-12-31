import random
n = random.randint(1,10)
c = 0
while(c == 0):
    a = int(input("guess the number      "))
    if(a < n):
        print("your guess is too low")
    elif(a > n):
        print("your guess is too high")
    else:
        print("you got the right number")
        c+=1