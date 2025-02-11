
## Q1: remove duplicates from a list
numbers = [3, 1, 2, 3, 4, 1, 5, 2]
new = []
for i in numbers: 
    if i not in new: 
        new.append(i)
print(new)

#### Q2: merge 2 lists 
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
## method1: list3 = list1 + list2 
## method2: list1.extend(list2) 
## method3: list comprehesion 
#new = [item for item in list1] + [item for item in list2]

## method4: itertools.chain()
from itertools import chain 
list3 = list(chain(list1,list2))
print(list3)

### Q3: get second largest num in a tuple
## method1: convert to list -> 2
n = (10, 5, 8, 20, 15)
a = list(n)
a.sort(reverse=True)
print(a)
## sort() is a list method 
## sorted() is a function 

## method2: 
m = (10, 5,8,30,15)
v = tuple(sorted(m, reverse=True))
print(v)
print(v[1])

## method3: heapq
import heapq
j = [1,12,5,7,13,14]
u = heapq.nlargest(2, j)
print(u)


# Count "Tree Species" in a Forest with Python
trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]

treeList = {}

for tree in trees: 
    treeList.setdefault(tree, 0)
    treeList[tree] = treeList[tree] + 1

print(treeList)