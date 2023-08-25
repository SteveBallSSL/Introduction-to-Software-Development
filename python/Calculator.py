
print("1- Add      +")
print("2- Subtract -")
print("3- Multiply *")
print("4- Divide   /")
print("5- Square   s")

Calc = input('Choose your calculation method')

Number1 = int(input('Please enter your first number'))
if Calc != 's':
    Number2 = int(input('Please enter your second number'))
    
if Calc == '+':
    result = Number1 + Number2
elif Calc == '-':
    result = Number1 - Number2
elif Calc == '*':
    result = Number1 * Number2
elif Calc == '/':
    result = Number1 / Number2
elif Calc == 's':
    result = Number1 * Number1

print(result)