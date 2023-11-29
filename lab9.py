"""#Ques1 
list1 = list(map(int, input().split()))
unique_set_of_list = set(list1)
unique_list = list(unique_set_of_list)
unique_list.sort()
print(unique_list)
"""

#Ques2
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

setA = set(list1)
setB = set(list2)


#union
union_set = setA.union(setB)
union_list = list(union_set)
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


