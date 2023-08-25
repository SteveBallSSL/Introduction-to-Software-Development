file = open("carSale.csv") 
lines = file.readlines() 
file.close() 
count = 1 
companies = [] 
sales = [] 
for line in lines: 
    if count % 2 != 0: # odd number 
        companies.append(line) 
    else: 
        sales.append(line.split(',')) 
    count += 1 
print(companies) 
print(sales)
    

