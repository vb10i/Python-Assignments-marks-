#Ques1 
list1 = list(map(int, input().split()))
unique_set_of_list = set(list1)
unique_list = list(unique_set_of_list)
unique_list.sort()
print(unique_list)


#Ques2
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

setA = set(list1)
setB = set(list2)

#union
union_list = list(set().union(list1, list2))
union_list.sort()
print(union_list)

#intersection
int_set = setA.intersection(setB)
int_list = list(int_set)
print(int_list)

#set difference
set_dif = setA - setB
dif_list = list(set_dif)
print(dif_list)

#symmetric set difference
setC = setA - setB
setD = setB - setA
listC = list(setC)
listD = list(setD)
symm_dif_list = list(set().union(listC, listD))
symm_dif_list.sort()
print(symm_dif_list)


#Q3
n=int(input("Enter number of elements : "))
l=list()
for i in range(n):
    l.append(int(input("enter a number:")))
for j in range(n):
    for k in range(j+1,n):
        if l[j]>=l[k]:
            l[j],l[k]=l[k],l[j]
print(f"the sorted list is {l}")


#Q4
a=int(input("enter no of rows:"))
b=int(input("enter no of columns:"))
c=int(input("enter no of rows in 2nd matrix:"))
d=int(input("enter no of columns in 2nd matrix:"))
mat1=[]
mat2 = []

for i in range(a):
    mat1.append([ ]) 
    for j in range(b):
        mat1[i].append(int(input("enter matrix elements")))
for i in range(c):
    mat2.append([ ])
    for j in range(d):
        mat2[i].append(int(input("enter matrix elements")))
print(f'the matrix is {mat1}')
print(f'the matrix is {mat2}')

for i in range(len(mat1)):   

    for j in range(len(mat2[0])):
        mat3 = mat1[i][j] + mat2[i][j]
print(f'the matrix addition is {mat3}')

for i in range(len(mat1)):
   for j in range(len(mat2[0])):
       for k in range(len(Y)):
           mat4=mat4+mat1[i][k] * mat2[k][j]
print(f'the multiplication of the matrices is {mat4}')

#Q5
#a 
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=str(input("enter a string:"))
   l.append(a)
print(f"the list of strings is {l}")
b=str(input("enter a string to be searched:"))
for j in l:
    if b==j:
        s=s+1
print(f"the string {b} is repeated {s} times")

#b 
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=int(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')
new_list=[]
for i in l:
    if i>0:
         new_list.append(i**2)
         
    elif i<0:
         new_list.append(0)
print(f'the new list is {new_list}')

#c
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=int(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')
new_list=[]
for i in l:
    if i>=10 and i<=20:
         new_list.append(i**2)
         
    else:
         new_list.append(i)
print(f'the new list is {new_list}')

#d
N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=str(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')

new_list=[i.title() if not i.title() else i for i in l]
print(f'the new list is {new_list}')


#Q6
n = int(input("Enter the number of students: "))
records = []
for i in range(n):
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = int(input("Enter total marks (out of 100) for {}: ".format(name)))
    records.append({'Name','RollNo', 'Marks'})
print(f'The records are {records}')
for student in records:
    print(f"Name: {student['Name']}")
    print(f"Roll No: {student['Roll No']}")
    print(f"Total Marks: {student['Total Marks']}")
    print()


#student with highest marks

    max_marks_student = records[0]
    for student in records:
        if student["Total Marks"] > max_marks_student["Total Marks"]:
            max_marks_student = student
    
     print(max_marks_student)



    if max_marks_student:
        print("Student with Maximum Marks:")
        print(f"Name: {max_marks_student['Name']}")
        print(f"Roll No: {max_marks_student['Roll No']}")
        print(f"Total Marks: {max_marks_student['Total Marks']}")
    else:
        print("No student records found.")

#part 2 of the question
for i in range(len(records)):
        rank = 1
        for j in range(len(records)):
            if records[j]["Total Marks"] > records[i]["Total Marks"]:
                rank += 1
        records[i]["Rank"] = rank

    # Display student details in ascending order of ranks
print("Student Details in Ascending Order of Ranks:")
for rank in range(1, len(records) + 1):
    for student in records:
        if student["Rank"] == rank:
            print(f"Rank: {student['Rank']}")
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll No']}")
            print(f"Total Marks: {student['Total Marks']}")
            print()

