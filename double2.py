import random
def findthe2():
    listoftwos=[]
    size=int(input("Enter the count of elements\n"))
    for i in range(0,10):
        if i/size==0:
            listoftwos.append(i)
    print(listoftwos)
    count =0
    for i in listoftwos:
        if listoftwos[i]==2:
            count+=1
    if count>=2:
        print(count)
        print("double truw")

findthe2()