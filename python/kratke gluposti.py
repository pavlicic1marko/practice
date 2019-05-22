import os
os.makedirs("salala")


def function1(x):
    return x + 1
def function2(x):
    pass
print(type(function1(1)))
print(type(function2(1)))
print(type(list))


list1=[4,5,6]
list2=[4,4,4]
d=sum([a != b for a, b in zip(list1,list2)])
print(d)

from itertools import *
for i in islice(count(),0,23,8):
    print(i)

for a,b in combinations([-2,-1,1,2],2):
    print(a,b)

x=1
d=lambda x:x+1
print(d(1))

n=[4,3,2,1]
print(list(map(lambda x:x>2,n)))


n=[[4,3,2,1],[4,3,2]]
print(list(map(lambda x:sum(x),n)))
print([sum(i) for i in n])

list1=[1,2,3,5,6,8,6,5,5,6,5,4,55,65,54,45,3,6,6456,534534,5345,34,5,34,5,34,5,34,5,34,-23]

print(ord('G'))

print(chr(105))

list1=[2,1,3,4,5,6,7]
print(list1)
list1[0],list1[1]=list1[1],list1[0]
print(list1)

import time
start = time.time()
print(start)
tuple1=tuple(range(10000000))
if 5000000 in tuple1:
    print("yes")
end = time.time()

elapsed = end - start
print(elapsed)

import math

n=29
k=5
print((math.factorial(n)//math.factorial(n-k))%1000000)
print(math.factorial(n)/10)
d=math.factorial(2)
print(d/2)
print(2/2)
d=(2//2)
print(type(d))
print(type(lambda x: x+1))

USERS={"1":'tarek',"2":'freya'}
reverse_key_value={val:id for id , val in USERS.items()}
print(reverse_key_value)



import timeit
start = timeit.timeit()

list23=[0,1,2,3,4,5,6,7,8,9]
list23=list23*10000


list23=[0,1,2,3,4,5,6,7,8,9]
list23=list23*1000000

import datetime
start = datetime.datetime.now()


counter=0
for i in list23:
    if i>8:
        counter+=1
print(counter,"counter")


end = datetime.datetime.now()
elapsed = end - start
print(elapsed)
# or


import datetime
start = datetime.datetime.now()
print(sum(1 for v in list23 if v >8 ))
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)

