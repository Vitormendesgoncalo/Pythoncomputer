while True:
    Name = str(input("Write your name complete, please: ")).strip()
    print("Your upper name: {}".format(Name.upper()))
    print("Your tiny name: {}". format(Name.lower()))
    print("Your complete name without spaces have: {}".format(len(Name)-Name.count(' ')))
    print("Your first name have: {}".format(Name.find(" ")))
    Cut = Name.split()
    print('Your first name have: {}'.format(len(Cut[0])))
