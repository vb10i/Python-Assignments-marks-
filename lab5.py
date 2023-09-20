#Ques1
n = int(input("enter a no between 1 and 20: "))
i = 1
if n<21 and n>0:
    while i<=n:
        a=1
        while a<=20:
            print(i, 'x', '=', a*i)
            a += 1
        i += 1
else:
    print('invalid')


#Ques2
n = int(input("enter no.: "))
i = 0
while i<100:
    i += 1
    if i%n == 0:
        continue
        print(i)


#Ques3
n = int(input("Enter number of lines: "))
i = 1
while i <= n:
    print("*"*i)
    i += 1


n = int(input("Enter number of lines: "))
i = 1
a = (2*n)-1
while i<=n:
    print(" "*a,"* "*i)
    i += 1
    a -= 2
    

n = int(input("Enter number of lines you want to print: "))
i = 1
a = 2*n-1
while i<=(2*n):
    print(" "*a,"* "*i)
    i += 2
    a -= 2


#Ques4
n = int(input("Enter the no.: "))
x = int(input("Enter no.: "))
count1 = 0
count2 =0
while x!=-999:
    if x%n == 0:
        count1 += 1
    else:
        count2 += 1
    x= int(input("Enter number: "))
print("no of divisible numbers: ", count1)
print("no of non divisible numbers: ", count2)


#Ques5
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
minimum = min(a,b)
i = 2
j = 1
while i>0:
    if i <= minimum:
        if a%i == 0 and b%i == 0:
            j=i
            print("LCM is", j)
            break
        else:
            i += 1
    else:
        LCM = (a*b)/j
        print("LCM is",LCM)
        break


#Ques6
a = int(input("Enter a no.: "))
b = int(input("Enter another no.: "))
minimum = min(a,b)
i = 2
j = 1
while i>0:
    if i <= minimum:
        if a%i == 0 and b%i == 0:
            j = i
            print("LCM is", j)
            break
        else:
            i += 1
    else:
        print("LCM is",j)
        break


#Ques7
i = 1
n = int(input("Enter number of lines: "))
a = n-1
while i<=(n):
    print(" "*a,"* "*i)
    i += 1
    a -= 1