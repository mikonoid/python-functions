import random
import time

Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase = "abcdefghijklmnopqrstuvwxyz"
Digits = "0123456789"
Symbols = "()!?*+=_-"



Mixedlist = Uppercase + Lowercase + Digits + Symbols

def generate():

    while True:
        word_length = int(input("length:" ))
        print ("Starting the word generating process")

        time.sleep(1)
        Password = ""
        for x in range(word_length):
            ch = random.choice(Mixedlist)
            Password = Password + ch
        break
    print ( Password)

generate()
