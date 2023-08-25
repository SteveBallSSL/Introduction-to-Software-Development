ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
print(ages)

ages_len = len(ages)

print("Length of ages",ages_len)
'''
print("-------------------")
print("List of ages")
for age in ages: 
    print(age)
'''
    
print("-------------------")
print("Add 1 to ages")
n = 0
while n < len(ages):
    ages[n] += 1
    n += 1
print(ages)

print("-------------------")
print("Remove some")

new_ages = ages
n=0
while n<len(new_ages):
    if new_ages[n] < 16  or new_ages[n] > 25:
        ages.remove(new_ages[n])
    else:
        n+=1
print(new_ages)

print("-------------------")
print("Sort")
ages.sort()
print(ages)

print("-------------------")
print("Proportion")

'''
Note, the range we need is already in new_ages so will use that
'''
range_len = len(new_ages)
proportion = ages_len

print((range_len/ages_len)*100,'%')