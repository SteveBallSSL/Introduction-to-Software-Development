companies = []
sales = []
with open("carSale.csv") as file:
    while True:
        line = file.readline().strip()
        if line == '' : break
        companies.append(line)
        data = file.readline().strip().split(',')
        sales.append(list(map(int,data)))

grandTotal=0

for col in range(len(sales[0])):
    total = 0
    for row in range(len(companies)):
        total +=  sales[row][col]
    print(total)
    grandTotal += total

print("Grand total: " , grandTotal)

count = 1 

   total = 0
    data = file.readline().strip().split(',')
    
    for row in range(len(data)):
        total +=  sales[row][col]
    print(total)
    grandTotal += total
    print("Grand total: " , grandTotal)