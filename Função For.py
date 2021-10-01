import time
number = int(0)
start = int(input('Write the first number:'))
end = int(input('Write the last number:'))
degree = int(input('Write the degree that it will count:'))
for number in range(start,end,degree):
    print(number)
    time.sleep(1)
        
    
