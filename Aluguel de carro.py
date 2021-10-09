def Calculate(Days, Km):
    print('You must pay: {0:.2f}'.format((Days * 60) + (0.15 * Km)))

while True:
    print("Price of days that you rented the car!\n")
    Days = int(input("Enter the days you had the car: "))
    Km = float(input('Enter the kilometers you ran with the car: '))
    Calculate(Days, Km)