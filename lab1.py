#Ques1
a = int(input("Enter value: "))
b = int(input("Enter value: "))
sum = a+b
mul = a*b
sub = a-b
div = a/b
print(sum)
print(mul)
print(sub)
print(div)


#Ques2
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
d = int(input("Enter the value: "))
sum = a+b+c+d
print(sum)
avg = sum/4
print("The average is: ", avg)


#Ques3
p = int(input("Enter the prinical interest: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time: "))
simple_interest = (p*r*t)/100
print("The Simple Interest is:", simple_interest)


#Ques4
time = int(input("Enter the time: "))
dist = int(input("Enter the distance: "))
speed=dist/time
print("Speed is: ", speed)


#Ques5
a = int(input("Enter side1: "))
b=int(input("Enter side2: "))
c=int(input("Enter side3: "))
s=((a+b+c)/3)
area=((s*(s-a)*(s-b)*(s-c))**(0.5))
print("area is: ", area) 


#Ques6
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d=((b**2)-(4*a*c))
if d<0:
    print("Roots are imaginary")
elif d==0:
    print("Roots are equal")
    x1 = -b/(2*a)
    x2 = x1
    print(x1,x2)
elif d>0:
    print("Roots are real and distinct")
    x1=((-b+d)/(2*a))
    x2=((-b-d)/(2*a))
    print(x1,x2)














