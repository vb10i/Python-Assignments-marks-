#Q1
#displaying all characters from 'A' to 'Z' 
for i in range(65,91):
    print(chr(i),end=" ")

#Q2
#taking input from user
sto=str(input("Enter a string: "))
#initializing count to 0
count=0
#loop to count the length of string
for i in sto:
    if i!=" ":
        count=count+1
#displaying results
print(f'Length of string is:{count}')  

#Q3
#taking input from user
string=input("Enter a string: ")
#replacing space with hyphen
a=string.replace(" ","-")
print(f'Original string is: {string}')
print(f'Hyphen-separated string is: {a}')

#snakecase
b=a.replace("-","_")
print(f'Original string is: {string}')
print(f'Snakecase string is: {b}')

#camelcase
print(f'Original string is: {string}')
temp=string.split(" ")
for ele in temp[1:]:
    res=temp[0]+"".join(ele.title())
print(f'Camelcase string is: {res}')

#Q4
#task: Write a program to check whether a string is palindrome or not.
#taking input from user
st=str(input("Enter a string: "))
#empty string
w=""
#loop to reverse the string
for i in st[::-1]:
    w=w+i
#checking if the reversed string is equal to the original string
if st==w:
    print("Palindrome")
else:
    print("Not Palindrome") 

#Q5
#input from user
sting=str(input("Enter a string: "))
#initializing variables
alphabets=0
digits=0
special=0
upp=0
low=0
#calculating length of string
s=len(sting)
#loop to check for alphabets, digits and special characters, upper and lower case
for i in range(s):
    if sting[i].isalpha():
        alphabets=alphabets+1
        if sting[i].isupper():
            upp=upp+1
        elif sting[i].islower():
            low=low+1
    elif sting[i].isdigit():
        digits=digits+1
    elif sting[i]==" " or sting[i]=="\n" or sting[i]=="\t":
        special=special+1
#displaying results
print(f'Alphabets:{alphabets}')
print(f'Digits:{digits}')
print(f'Special Characters:{special}')
print(f'Upper Case:{upp}')
print(f'Lower Case:{low}')

#Q6
#taking input
stion=str(input("Enter a string: "))    
print("Original String:",stion) 

#reversing order of words
j=stion.split()
l=len(j)
#loop to reverse the order of words
for i in range(-1,-l-1,-1):
    print(j[i],end=" ")

#Q7
#taking input from user
sti=str(input("Enter a string:"))
#empty string
p=""
#loop to check for duplicate characters
for char in sti:
    if char not in p:
        p=p+char
#displaying results
print(f'Original string is: {sti}')
print(f'New string without duplicate characters is: {p}')

#Q8
#program to count the number of times a word occurs in a sentence
#without inbuilt function
#taking input from user
sen=str(input("enter a sentence:"))
word=str(input("enter a word:"))
#initializing counter
c=0
#loop to check for word
for i in sen.split():
    if i==word:
        c=c+1
#displaying results
print(f'Number of times {word} occurs in {sen} is {c}')

#with inbuilt function
#taking input from user
sen=str(input("enter a sentence:"))
word=str(input("enter a word:"))
#displaying results
print(f'Number of times {word} occurs in {sen} is {sen.count(word)}')

#Q9
#this program checks whether a string is pangram or not
#taking input from user
sty=str(input("Enter a string:"))
#initializing alphabet wtih all the alphabets
alphabet="abcdefghijklmnopqrstuvwxyz"
#loop to check if all the alphabets are present in the string
for char in alphabet:
    if char not in sty.lower():
        print("Not Pangram")
        break
else:
    print("Pangram")

#Q10
s = str(input('enter a hyphen sep string:'))
s = s.replace('-',' ')
s= s.split()
print(s)
l= len(s)

i=0
a=['-']
while i <l:
    x = min(s)
    a.append(x)

    s.remove(x)
    

    i=i+1
a.remove('-')
print('-'.join(a))

#Q11
histogram = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

while True:
    user_input = int(input("Enter a number (1-10, -1 to exit): "))
    
    if user_input == -1:
        break
    
    if 1 <= user_input <= 10:
        histogram[user_input] += 1
    else:
        print("Invalid input. Enter a number in the range 1-10.")

for start, end in [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]:
    count = sum(histogram[i] for i in range(start, end + 1))
    percentage = (count / sum(histogram.values())) * 100 if sum(histogram.values()) != 0 else 0
    print(f"{start} - {end}: {' # ' * count} {percentage:.2f} %")

#Q12
N=int(input("enter a number: "))
 
hline=" +/" + "\/" *(N-2) + "+"
vline=" |" +   " "*(N-2) +   "|"
for i in range(N):
    if i==0 or i==N-1:
        print(hline)
    else:
        print(vline)
