def Upper():
    Name = str(input("Write your name complete: "))
    Split = Name.split()
    print("Your name {} upper is {}".format(Name, Name.upper()))
def Lower():
    Name = str(input("Write your name complete: "))
    print("Your name {} lower is {}".format(Name, Name.lower()))
def Countfirst():
    Name = str(input("Write your name complete: "))
    Split = Name.split()
    print("Your name {} have {} in first name".format(Name, len(Split[0])))
    print("Countfirst")
def Countall():
    Name = str(input("Write your name complete: "))
    Split = Name.split()
    print("Your name {} have {} all your name".format(Name, len(Name)-Name.count(' ')))
    print("Countall")
while True:
    Option = {
        0 : Upper,
        1 : Lower,
        2 : Countfirst,
        3 : Countall,
    }
    Option = Option.get (int(input("Enter  with 0 to upper, 1 to lower, 2 to countfirst, 3 to count: ")))
    Option()