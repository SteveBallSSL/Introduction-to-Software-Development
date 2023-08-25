InitialInvestment =  int(input('Please input your Initial Investment'))
TargetValue = int(input('Please input your Target Value'))
InterestRate = int(input('Please input your Interest Rate'))
Years = 0
ActualInterest = InterestRate/100

while InitialInvestment < TargetValue:
    Years = Years+1
    InitialInvestment = InitialInvestment * (1+ActualInterest)
    
print (Years)