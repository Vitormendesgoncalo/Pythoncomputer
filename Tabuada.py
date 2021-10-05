import time
def Table(Number):

    for First in range (11):
        print('{} X {} = {}'.format(Number, First, First * Number) )
        time.sleep(1)
while True:
    print('Now we will make times tables!')
    Number = int(input('\nEnter the value that you want know: '))
    Table(Number)