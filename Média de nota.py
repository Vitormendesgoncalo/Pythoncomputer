print('Now we are calculating the student grade!!!')
Gradeone = float(input('Enter the student´s first grade: '))
Gradetwo = float(input('Enter the student´s second grade: '))
Gradeaverage = ((Gradeone+Gradetwo)/2)
print('The student´s average grade is: {}'.format(Gradeaverage))

# If you want caculate with just one digit, you can use the comand :".1f" into keys

print('The grade average between {:.1f} and {:.1f} is {:.1f}'.format(Gradeone, Gradetwo, Gradeaverage))