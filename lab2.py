#Ques1
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length*width
print("Area of the plot in metre square is: ", area)


#Ques2
length = int(input("Enter length in feet: "))
width = int(input("Enter width in feet: "))
area_feet = length*width
area_sqmeter = (area_feet)*(0.3048*0.3048)
print("Area in feet: ", area_feet)
print("Area in square meter:", area_sqmeter)


#Ques3
x = int(input("enter x: "))
y = int(input("enter y: "))
if x<0 or y<0:
    print("Invalid Input")
elif y%x==0:
    print("Divisble")
else:
    print("Not divisble")
    
    
#Ques4
num = int(input("enter number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")
    
    
#Ques5
radius = int(input("Enter the radius: "))
if radius>1 and radius<100:  
    area = (22/7)*radius*radius
    print("area is: ", area)
else:
    print("Error")


#Ques6
temp_in_celcius = int(input("Enter temp:"))
print("Temperature in celsius is: ", temp_in_celcius)
temp_in_far =((9/5)*(temp_in_celcius))+32
print(temp_in_far)
temp_in_kelvin = temp_in_celcius + 273
print(temp_in_kelvin)


#Ques7
for c in range(-273,100000):
    f = ((9/5)*c)+32
    if f==c:
        print(c)
        break   
    c += 1
    
    
#Ques8
year = int(input("Enter the year: "))
if year%100==0 and year%400==0 :
    print("Leap year")
elif year%4==0 and year%100!=0:
    print("Leap year")
else:
    print(" Not a leap year")
    
    
#Ques9
P = int(input("enter principal amount: "))
r = 7.1
t = int(input("enter time: "))
n = int(input("enter the no of times interest compounds in a year: "))
if  P<500 or t<6:
    print("error!")
else:
    x =(P*(( 1 + r/n)**(n * t)))
    print(x)
    
    
#Ques10
seconds = int(input("enter time in seconds: "))
seconds= seconds%(24 * 3600)
hour = seconds//3600
seconds %= 3600
minutes = seconds//60
seconds %= 60
print(hour, "Hours", minutes, "Minutes", seconds, "Seconds")
