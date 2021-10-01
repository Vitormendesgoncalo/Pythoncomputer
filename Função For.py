import time
number = int(0)#It´s a number that it will sum the degree
start = int(input('Write the first number:'))#A number that it will be the start
end = int(input('Write the last number:'))#A number that it will be the end
degree = int(input('Write the degree that it will count:'))#It will be how much it will jump
for number in range(start,end,degree): # Comand for
    print(number) # Print the variable number
    time.sleep(1) # wait one second
        
    
