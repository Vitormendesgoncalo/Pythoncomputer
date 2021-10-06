print('How much do you want to pay?!')
Price = float(input("Enter the price product: "))
Discount = float(input("Enter the percentage discount amount: "))
Discount /=100
Discount -=1
Discount *=-1
print('You will pay: {}'.format(Price * Discount))
