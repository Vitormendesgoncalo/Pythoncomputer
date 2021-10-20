from random import randint
from time import sleep
print("You need to guess the number that I am thinking but first you need enter the first and lat!\n")
while True:
    First = int(input("Enter the first number: "))
    Last = int(input("Enter the last number: "))
    Think = int(input("Enter the number that I thought: "))
    print("Processing. Wait please!")
    sleep(2)
    Number = randint(First, Last)
    print("I thought {} and you are {}!!!". format(Number, Number==Think))

