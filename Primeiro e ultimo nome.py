while True:
    Name = str(input("Write your complete name: "))
    Name = Name.split()
    print("Hi {}".format(Name))
    print("Your first name is: {}".format(Name[0]))
    print("Your last name is: {}".format(Name[len(Name)-1]))