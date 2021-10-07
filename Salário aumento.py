print('We will calculate the salary increase!')
Salary = float(input('Enter the employee salary: '))
Increase = float(input('Enter the increase in porcent: '))
Increase /= 100
print('The new salary is: {:.2f}'.format((Salary * Increase) + Salary))
