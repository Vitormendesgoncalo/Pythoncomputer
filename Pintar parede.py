print('We need how much we need to paint the wall!')
Wallx = float(input('Enter the value length(m): '))
Wally = float(input('Enter the value height(m): '))
print('Your wall have {:.2f}m lenght and {:.2f}m height. So the area is {:.2f}m² and you need {:.2f}l to paint.'. format(Wallx, Wally, Wallx * Wally, (Wallx*Wally)/2))