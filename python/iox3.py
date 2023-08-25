file = open("students.txt","r") 
for line in file:
    print(line.strip())
    
    
file.close()

print('')
print('')
print('')

with open("students.txt","r")  as file:
    header = file.readline()
    lines = file.readlines()
    
print(header.strip())
print('---------------------------------')
for line in lines:
    print(line.strip())