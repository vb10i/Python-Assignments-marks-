#Ques1
line = str(input("enter the line: "))
l = len(line)

vowels = constants = 0
for i in range(l):
    if(line[i]=='a' or line[i]=='e' or line[i]=='i' or line[i]=='o' or line[i]=='u'):
        vowels += 1
    elif line[i]!= " ":
        constants += 1
    i += 1

print("vowels are: ", vowels)
print("constants are: ", constants)


#Ques2
#a)
n = int(input("enter the number of terms: "))
i = 1
count = 0
for i in range(n):
    i += 1
    y = 1/i
    count += y
print(round(count,9))

#b)
n = int(input("enter the number of terms: "))
i = 1
fact = 1
count = 0
for i in range(n):
    i += 1
    fact = fact*i
    y = 1/fact
    count += y
print(round(count,9))

#c)
n = int(input("enter the number of terms: "))
i = 1
pi = 3.14
count = 0
for i in range(n):
    i += 1
    y = pi/i
    count += y
print(round(count,9))