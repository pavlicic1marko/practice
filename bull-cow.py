#GGG
#gggg
from random import randint
def C_B():
    random='1234'
    user=input('enter a four digit number:')
    cow=0
    bull=0
    for i in range(4):
        if random[i] == user[i]:
            cow+=1
    for i in range(4):
        for x in range(4):
            if user[i] in random[x]:
                random=random.strip(user[i])
                random=random.__add__('c')
                bull+=1
    bull=bull-cow

C_B()
