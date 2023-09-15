#Ques1
N = int(input("enter the number: "))
for i in range(1,21):
    Nxi = N*i
    print(N, 'x', i, '=', Nxi)

N = int(input("enter the number: "))
i = 0
while i < 20:
    i += 1
    Nxi = N*i
    print(N, 'x', i, '=', Nxi)
    


#Ques2
X = int(input("enter first num: "))
Y = int(input("enter second number: "))
N = int(input("enter N: "))
i = X+1
while i<=Y:
    if i%N == 0:  
        print(i)
    i +=1
    



#Ques3   
N = int(input("enter the number: ")) 
sum = 0
if N>0:
    while N>0:
        num = N%10
        sum += num
        N = N//10
    print(sum)


#Ques6
N = str(input("enter the word: "))
back = N[::-1]
print(back)
if N == back:
    print("its a palindrome")
else:
    print("it not a palindrome")



#Ques5
n = int(input())
i = 1
fact = 1
while i<=n:
    fact = fact*i
    i += 1
print(fact)




#Ques4
n = int(input("enter n: "))
div = 0
nondiv = 0
while True:
    num = int(input("enter divisible num: "))
    if num == -999:
        break
    if num%n == 0:
        div += 1
    else:
        nondiv += 1
        
print(div)
print(nondiv)


#Ques7
a = 1
b = int(input("enter the second term of sequence: "))
c = int(input("enter the third term of sequence: "))
d = int(input("enter the fourth term of sequence: "))
e = int(input("enter the fifth term of sequence: "))
f = int(input("enter the sixth term of sequence: "))
print("given sequence", a,b,c,d,e,f)
if a==b and a+b==c and b+c==d and c+d==e and d+e==f:
    print("sequence is fibonacci")
else:
    print("sequence isn't fibonacci")


#Ques8
i = int(input())
if i == 1:
    print("given number isn't prime")
elif i == 0:
    print("given number isn't prime nor composite")
elif i < 0:
    print("given number cannot be defined as prime or not")
elif i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 :
    print("given number is prime")
else:
    print("given number isn't prime")


#Ques9
line = str(input("enter the line: "))
l = len(line)

large = small = specialch = digits = 0 
for i in range(l):
    if(line[i]>="A" and line[i]<="Z"):
        large += 1
    elif(line[i]>='a' and line[i]<='z'):
        small += 1
    elif(line[i]>='0' and line[i]<='9'):
        digits += 1
    else:
        specialch += 1
    i += 1 


#Ques10
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
D = (b**2)-4*a*c

if D>0:
    x1 = (-b + (D)**(0.5))/(2*a)
    x2 = (-b - (D)**(0.5))/(2*a)
    print(x1, x2)
elif D==0:
    x1 = -b/(2*a)
    x1 = x2
    print(x1,x2)
elif D<0:
    i = (-1)**(0.5)
    D = D*i
    x1 = (-b + (D)**(0.5))/(2*a)
    x2 = (-b - (D)**(0.5))/(2*a)
    print(x1,x2)
    




