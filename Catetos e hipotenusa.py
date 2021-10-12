from time import sleep
import math
while True:
    def Hypotenuse():
        Leg1 = float(input("Enter the first leg: "))
        Leg2 = float(input("Enter the second leg: "))
        print("The leg {0:.2f} and leg {1:.2f} result in hypotenuse {2:.2f}".format(Leg1, Leg2, math.sqrt((Leg1**2) + (Leg2**2))))
        sleep(5)
    def Legs():
        Leg1 = float(input("Enter the leg: "))
        Hypotenuse1 = float(input("Enter the hypotenuse: "))
        print("The leg {0:.2f} and hypotenuse {1:.2f} result of second leg is {2:.2f}".format(Leg1, Hypotenuse1, math.sqrt(-1*((Leg1**2) - (Hypotenuse1**2)))))
        sleep(5)
    print("Now we are going to calculate hypotenuse or legs\n")
    Option = {
        0:Hypotenuse,
        1:Legs,
    }
    Option = Option.get (int(input("Enter with 0 to calculate the hypotenuse or 1 to calculate the legs: ")))
    Option()
