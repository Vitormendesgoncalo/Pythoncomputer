#CASE THREE
Number = int(input("Enter the 4 numbers: "))
u = Number // 1 % 10
d = Number // 10 % 10
c = Number // 100 % 10
m = Number // 1000 % 10

print("U = {}".format(u))
print("D = {}".format(d))
print("C = {}".format(c))
print("M = {}".format(m))

#CASE TWO
#while True:
#    Split = int(1000)
#    Sequence = int(1)
#    Number = int(input('Enter the number:'))
#    for Sometimes in range(4):
#        Number1 = Number//Split
#        print("The {:.0f}º is the number {:.0f}".format(Sequence, int(Number1)))
#        Number1 *= -Split
#        Number1 += Number
#        Number = Number1
#        Sequence += 1
#        Split /= 10


#CASE ONE
#while True:
#    print("We going to show you the type of numer you enter here!")
#    Number = int(input("Enter the number until 4 type:"))
#    if Number >= 1000 and Number < 10000:
#        print('Unit is {}'.format('4'))
#    elif Number >= 100 and Number < 1000:
#        print('Unit is {}'.format('3'))
#    elif Number >= 10 and Number < 100:
#        print('Unit is {}'.format('2'))
#    elif Number >= 0 and Number < 10:
#        print('Unit is {}'.format('1'))