print("1- Add 2 times")
print("2- Find the difference between 2 times")
print("3- Convert to Hours")
print("4- Convert to Minutes")
print("5- Convert Minutes to Time")
print("6- Convert Hours to Time")
print("7- Convert Days to Time")
print("8- Exit")

Option = input('Enter an option')


    
    
if Option == '1':
    Time1 = input("Enter first time")
    Time2 = input("Enter second time")
    Time1List = Time1.split(':')
    Time2List = Time2.split(':')
    result = int(Time1List[0])+int(Time2List[0])+(int(Time1List[1])+int(Time2List[1])+(int(Time1List[2])+int(Time2List[2]))//60)//60
elif Option == '2':
    Time1 = input("Enter first time")
    Time2 = input("Enter second time")
    result = Time2,Time1
elif Option == '3':
    Time = input("Enter time")
    result = Time
elif Option == '4':
    Time = input("Enter time")
    result = Time
elif Option == '5':
    Time = input("Enter time")
    result = Time
elif Option == '6':
    Number = input("Enter number")
    result = Number
elif Option == '7':
    Number = input("Enter number")
    result = Number   
    

    
print(result)