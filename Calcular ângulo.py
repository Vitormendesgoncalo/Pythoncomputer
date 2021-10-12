import math
print("We are going to calculate angle!!!\n")

def Cos():
    Value = float(input("Enter the Cos: "))
    print("The cos is {}".format(math.cos(Value)))
def Sin():
    Value = float(input("Enter the Sen: "))
    print("The sin is {}".format(math.sin(Value)))
def Tan():
    Value = float(input("Enter the Tan: "))
    print("The tan is {}".format(math.tan(Value)))
while True:
    Option = {
        1: Cos,
        2: Sin,
        3: Tan,
    }
    Option = Option.get(int(input("Enter the option that you want.\n1 - Cos\n2 - Sin\n3 - Tan\n")))
    Option()
