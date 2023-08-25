# While 
print ('Start While')
n = 1
while n <= 100:
    ns = n*n
    if ns < 2000:
        print (n,' - ',n*n)
        n = n+1
    else:
        break
print ('-----------')
print ('')    
# For     
print ('Start For')
for n in range(100):
    ns = n*n
    if ns < 2000:
        print (n,' - ',n*n)
        n = n+1
    else:
        break
print ('-----------')
print ('')    
# From Mike     
print ('From Mike')    
x = 1 
while x <= 100: 
    sq = x ** 2 
    print(sq, end=",") 
    if sq > 2000: 
        break 
    x += 1
