while True:
    Name = str(input("Write your complete name, please: ")).upper().strip()
    print("Your name {} have {} of A".format(Name ,Name.count("A")))
    print("The first word A is {}".format(Name.find("A")+1))
    print("The last word A is{}".format(Name.rfind("A")-1))
