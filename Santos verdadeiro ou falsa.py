while True:
    print("This programa will show if you born in Santos City!")
    City = str(input("Enter with your born city: ")).strip()
    print("{}".format(City[0:6].upper()) == "SANTOS")