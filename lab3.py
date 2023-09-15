#Ques1
x = int(input("Enter the length of the first parallel side: "))
y = int(input("Enter the length of second parallel side: "))
h = int(input("Enter the height: "))
area = ((1/2)*(x+y)*h)
print(area)


#Ques2
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = (weight)/(height**2)
print("Bmi is: ", bmi)

w = float(input("Enter weight(in pounds): "))
h = float(input("Enter height(in inches): "))
bm = (703*w)/(h**2)
print("The bmi in kg/m is: ", bm)


#Ques3
s1 = int(input("Enter side1: "))
s2 = int(input("Enter side2: "))
s3 = int(input("Enter side3: "))
if s1<0 or s2<0 or s3<0:
    print("Invalid sides")
if s1+s2>s3 or s2+s3>s1 or s1+s3>s2 and s1>0 and s2>0 and s3>0:
    print("The three sides form a triangle: ")
else:
    print("Error")


#Ques4
num = int(input("Enter a number:"))
sum = 0
while num != 0:
    sum = sum + (num % 10)
    num = num//10
print(sum)
if sum%3==0:
    print("Divisble")
else:
    print("Not Divisble")
    
    
#Ques5
num = int(input("Enter a five digit  number:"))
temp = num
rev = 0
while num>0:
    dig = num%10
    rev = rev*10+dig
    num = num//10
if temp==rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

#Ques6
a = int(input("Eenter a no: "))
b = int(input("enter a no: "))
print("Before swapping: ", a, b)
a,b = b,a
print("After swapping:", a, b)


#Ques7
a = complex(input("Enter a complex no: "))
b = complex(input("enter a complex no: "))
sum = a+b
mult = a*b
print(sum)
print(mult)


#Ques8
bsal = int(input("enter salary: "))
hra = 0.2*bsal
ta = 0.05*bsal
da = 0.1*bsal
gs = bsal+hra+ta+da
print("Gtoss Salary is: ", gs)


#Ques9
bsal = int(input("enter salary: "))
hra = 0.2*bsal
ta = 0.05*bsal
da = 0.1*bsal
gs = bsal+hra+ta+da
print("Gtoss Salary is:", gs)

if gs<300000:
    print("No Income Tax")
if gs>=300000 and gs<1000000:
    incometax=0.1*gs
    print(incometax)
if gs>=1000000 and gs<2500000:
    incometax=0.2*gs
    print(incometax)
if gs>=2500000:
    incometax=0.3*gs
    print(incometax)
    
    
#Ques10
s1 = int(input("Enter a no: "))
s2 = int(input("Enter a no: "))
s3 = int(input("Enter a no: "))
if s1>s2:
    if s1>s3:
        print("s1 is largest")
if s2>s1:
    if s2>s3:
        print("s2 is largest")
if s3>s1:
    if s3>s2:
        print("s3 is largest")
        
        
#Ques11
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")