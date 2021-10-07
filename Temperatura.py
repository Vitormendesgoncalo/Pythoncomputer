def Choice(Temperature, Type):
    Change = input('What temperature do you want to change (ºC, ºF, ºK)?: ')
    if Type == 'c' or Type == 'C':
        if Change == 'c' or Change == 'C':
            print('The temperature is {:.2f}'.format(Temperature))
        elif Change == 'f' or Change == 'F':
            print('The temperature is {:.2f}'.format((((9/5) * Temperature) + 32)))
        elif Change == 'k' or Change == 'K':
            print('The temperature is {:.2f}'.format(Temperature+273))
    elif Type == 'f' or Type == 'F':
        if Change == 'c' or Change == 'C':
            print('The temperature is {:.2f}'.format((((5/9) * Temperature) - 32)))
        elif Change == 'f' or Change == 'F':
            print('The temperature is {:.2f}'.format(Temperature))
        elif Change == 'k' or Change == 'K':
            print('The temperature is {:.2f}'.format((((5/9) * Temperature) - 32)+273))
    elif Type == 'k' or Type == 'K':
        if Change == 'c' or Change == 'C':
            print('The temperature is {:.2f}'.format(Temperature - 273)
        elif Change == 'f' or Change == 'F':
            print('The temperature is {:.2f}'.format(((Temperature - 273)*9/5)+32))
        elif Change == 'k' or Change == 'K':
            print('The temperature is {:.2f}'.format(Temperature))

while True:
    print('We will show you which temperature you want!')
    Temperature = float(input('Enter the temperature you measured: '))
    Type = input('Enter the temperature type (ºC, ºF, ºK): ')
    Choice (Temperature, Type)






