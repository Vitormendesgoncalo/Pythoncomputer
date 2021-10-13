import random
print("Now we going to draw a name!\n")
Name = []
for Number in range(10):
    Name.append(Number)
    Name[Number] = str(input("Write 3 names"))
Choice = random.choice(Name)
print(Choice)
