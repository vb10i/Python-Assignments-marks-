#Q1
#a
n = int(input("enter length of list of integers:")) 
l=list() 
l2=list()
  
  
for i in range(n): 
    l.append(int(input("enter a integer: "))) 
  
for j in l: 
    if j not in l2: 
        l2.append(j) 
print(f'original list: {l}')
print(f'Removing duplicate elements from the list: {l2}')

#b
n = int(input("enter (length of list of integers):")) 
l=list() 
l2=list() 
  
  
for i in range(n): 
    l.append(int(input("enter a integer: "))) 
  
for j in l: 
    if j not in l2: 
        l2.append(j) 
a=set(l2) 
b=list(a)
print(f'original list: {l}')
print("list: ",b )
print(f'set: {a}')


#Q2
#a
n1 = int(input("enter length of integers:")) 
n2 = int(input("enter length of integers:"))
l1=list() 
l2=list() 
  
  
for i in range(n1): 
    l1.append(int(input("enter a integer: ")))
for j in range(n2):
    l2.append(int(input("enter a integer: ")))

a=set(l1)
b=set(l2)
print(f'original list: {l1}')
print(f'original list: {l2}')
print(f'set1: {a}')
print(f'set2: {b}')

#b
n1 = int(input("enter length of integers:")) 
n2 = int(input("enter length of integers:"))
l1=list() 
l2=list() 
  
  
for i in range(n1): 
    l1.append(int(input("enter a integer: ")))
for j in range(n2):
    l2.append(int(input("enter a integer: ")))

set_a=set(l1)
set_b=set(l2)

print(f'Union of set1 and set2: {set_a | set_b}')
print(f'Intersection of set1 and set2: {set_a & set_b}')
print(f'Difference of set1 and set2: {set_a - set_b}')
print(f'Symmetric difference of set1 and set2: {set_a ^ set_b}')

#c
n1=int(input("Enter number: ")) 
n2=int(input("Enter number: ")) 
l=list() 
l2=list() 
l3=list() 
  
  
for i in range(n1): 
    l.append(int(input("enter a integer: "))) 
  
for j in range(n2): 
    l2.append(int(input("Enter elements: "))) 

for k in range(0,n1+1): 
    if (k in  l) and (k  in l2): 
        l3.append(k) 
print(f'original list: {l}')
print(f'original list: {l2}')
print(f'intersection of l1 and l2: {l3}')

#d
n1=int(input("Enter number: ")) 
n2=int(input("Enter number: ")) 
l=list() 
l2=list() 
l3=list() 

for i in range(n1): 
    l.append(int(input("enter a integer: "))) 
for j in range(n2): 
    l2.append(int(input("Enter elements: "))) 
for k in l:
    if k in l or k in l2:
        l3.append(k)
for k in l2:
    if k in l or k in l2:
        l3.append(k)
print(f'original list: {l}')
print(f'original list: {l2}')
print(f'intersection of l1 and l2: {l3}')


#Q3
N = int(input("Enter the value of N: "))
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(f'Matrix: {matrix}')
is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(N) for j in range(N))
print("Symmetric" if is_symmetric else "Not Symmetric")
principal_diagonal_sum = sum(matrix[i][i] for i in range(N))
non_principal_diagonal_sum = sum(matrix[i][N-i-1] for i in range(N))
print("Sum of Principal Diagonal elements:", principal_diagonal_sum)
print("Sum of Non-Principal Diagonal elements:", non_principal_diagonal_sum)
is_upper_triangular = all(matrix[i][j] == 0 for i in range(1, N) for j in range(i))
is_lower_triangular = all(matrix[i][j] == 0 for i in range(N) for j in range(i+1, N))
print("Upper Triangular" if is_upper_triangular else "Not Upper Triangular")
print("Lower Triangular" if is_lower_triangular else "Not Lower Triangular")
transpose = [[matrix[j][i] for j in range(N)] for i in range(N)]
print("Transpose of the matrix:")
for row in transpose:
    print(' '.join(map(str, row)))


#Q4
N = int(input("Enter the value of N: "))
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(f'Matrix: {matrix}')



lead = 0
rowCount = len(matrix)
columnCount = len(matrix[0])

for r in range(rowCount):
    if lead >= columnCount:
        break
    i = r
    while matrix[i][lead] == 0:
        i += 1
        if i == rowCount:
            i = r
            lead += 1
            if columnCount == lead:
                break
    matrix[i], matrix[r] = matrix[r], matrix[i]
    lv = matrix[r][lead]
    matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
    for i in range(rowCount):
        if i != r:
            lv = matrix[i][lead]
            matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
    lead += 1

    


