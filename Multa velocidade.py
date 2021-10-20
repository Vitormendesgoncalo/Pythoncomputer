print("I will show you if you exceeded the limit of velocity!")
while True:
    Velocity = float(input("Enter the your velocity: "))
    if Velocity > 80:
        Velocity -= 80
        Velocity *= 7
        print("You must to pay a tax about {:.0f}".format(Velocity))
    else:
        print("Congratulation! You are a good driver!!!")

