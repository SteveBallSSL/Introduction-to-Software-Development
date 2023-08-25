grade = int(input('Please enter your grade'))

if grade < 50:
    print('Fail')
elif grade >= 50 and grade <= 60:
    print('Pass')
elif grade >= 61 and grade <= 70:
    print('Merit')
elif grade >= 71 and grade <= 100:
    print('Distinction')
else:
    print('Not a valid grade!')