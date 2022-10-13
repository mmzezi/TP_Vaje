#random cifra x = 23, upoirabnik vnese 0-30 (vnos), če vnese 10 naj javi premahjno, če 30 pa preveliko, naj ima 5 poskusov

#random cifra
import random
x = random.randrange(0,30)
c = 5

while c > 0:
    y = input("Vnesi število: ")
    if x == int(y):
        print("Wau bravo uganil si število!")
        break
    else:
        if x < int(y):
            print("To ni pravo število, je preveliko")
        if x > int(y):
            print("To ni pravo število, je premajhno")
    c = c - 1
