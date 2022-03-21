import random

print(' Creating two 3 by 3 matrices and adding all the elements to create another 3 by 3 matrix ')
print()

#............................................
# Creating matrix1

def matrix1(m,n):
 print(' Matrix1 of 3 by 3 order will be created by input from the user !! ')
 print()
 global listmain
 listmain=[]
 for i in range(1,m+1):
    list1=[]
    for j in range(1,n+1):
        appn=eval(input(' Enter element {}{} of matrix : '.format(i,j)))
        list1.append(appn)
    listmain.append(list1)
 print()

 for i in range(len(listmain)):
    for j in range(len(listmain[i])):
        print(listmain[i][j],end='\t')
    print()    
 print()
matrix1(5,3)

#..............................................
# Creating matrix2

def matrix2(a,b):
 print(' Matrix2 of 3 by 3 order will be created by input from the user !! ')
 print()
 global listmain2
 listmain2=[]
 for i in range(1,a+1):
    list2=[]
    for j in range(1,b+1):
        appn=eval(input(' Enter element {}{} of matrix : '.format(i,j)))
        list2.append(appn)
    listmain2.append(list2)
 print()

 for i in range(len(listmain2)):
    for j in range(len(listmain2[i])):
        print(listmain2[i][j],end='\t')
    print()    
 print()
matrix2(5,3)

#.............................................
# Adding matrix1 and matrix2

print(' The addition of matrix1 and matrix2 is as follows')
print()
c=5
d=3
addlist=[]
for i in range(c):
    list3=[]
    for j in range(d):
        a=listmain[i][j] + listmain2[i][j]
        list3.append(a)
    addlist.append(list3)
print()

for i in range(len(addlist)):
    for j in range(len(addlist[i])):
        print(addlist[i][j],end='\t')
    print()
print()
