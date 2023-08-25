

def getIncomeTax(salary):
    persAll = 11850
    if salary < persAll:
        return 0
    if salary < 34500:
        return round((salary-persAll)*0.2) 
    elif salary < 150000:
        return round((salary-persAll)*0.4) 
    else: 
        return round((salary-persAll)*0.45) 
        
tax = getIncomeTax(11950)

print(tax)

def getIncomeTax2(salary):
    pA = 11850
    if salary < pA:
        return 0 
    if salary < 34500:
        return round((salary-pA)*0.2) 
    if salary < 150000:
        return round((salary-pA)*0.4) 
    return round((salary-pA)*0.45) 
        
tax = getIncomeTax2(11950)

print(tax)