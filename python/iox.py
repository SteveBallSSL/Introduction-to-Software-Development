fp = open("students.txt","r") # r = readonly
line = fp.readline()
line = fp.readline()
line = fp.readline()

fp.close()

print(line)

print('---------------------------------')

fp = open("students.txt","r") # r = readonly
linelist = []
line = linelist.append(fp.readline())
line = linelist.append(fp.readline())
line = linelist.append(fp.readline())

fp.close()

print(linelist[1])

print('---------------------------------')

fp = open("students.txt","r") # r = readonly
lines = fp.readlines()
fp.close()

print(lines)

print('---------------------------------')

for line in lines:
    print(line)
    
print('---------------------------------')

for line in lines:
    print(line.strip())
    
print('---------------------------------')

fp = open("students.txt","r") # r = readonly

header = fp.readline()
lines = fp.readlines()

fp.close()

print(header)
for line in lines:
    print(line)
    
print('---------------------------------')

fp = open("students.txt","r") # r = readonly
fp.seek(20)
line = fp.readline()
fp.close()
print(line.strip())
    
print('---------------------------------')

