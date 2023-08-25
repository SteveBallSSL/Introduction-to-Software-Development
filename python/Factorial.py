UserNum = int(input('Please input a number'))

# While 
print ('Start While')
CurrVal = UserNum-1
while CurrVal > 0:
    UserNum = UserNum*CurrVal
    CurrVal = CurrVal -1
    
print(UserNum)  
print ('-----------')
print ('')
# For     
print ('Start For')
CurrVal = UserNum
for n in range(CurrVal):
    UserNum = UserNum*CurrVal
    n  = n  -1
print(CurrVal)   

print ('-----------')
print ('')
# From Trainer     
print ('From Trainer')
# Factorial of 5 
no = 5 
total = 1 
while no > 0: 
    total *= no 
    no -= 1 
print(total)

