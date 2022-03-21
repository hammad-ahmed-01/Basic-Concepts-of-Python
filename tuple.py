# Author == Hammad Ahmed
# Python IDLE

# a program to make two tuples by user input, compare them and find Maximum,Minimum of both. Also add in the original tuples to create new ones
# a function to create a tuple
def tup():
    n=1
    lis= []
    while n<=5:
        nu=input("input any data type in tuple: ")
        lis.append(nu)
        n+=1
    tu=tuple(lis)
    return tu

print(" Enter data of 1st Tuple")
print()
tup1= tup()
print()
print(" Enter data of 2nd Tuple now")
print()
tup2= tup()
print()
print(tup1,tup2)
print()

# conditional statement to check whether two tuples are equal or not
if tup1==tup2:
    print("Both tuples are same")
else:
    print("Tuples are not same")


# checking minimum and maxmum by builtin functions
print("maximum in tuple 1 is ",max(tup1))
print("maximum in a 2 is ",max(tup2))
print("minimum in tuple 1 is ", min(tup1))
print("minimum in tuple 2 is ", min(tup2))
print()

# adding in the original tuples to produce new tuples
tup3=tuple(list(tup1)+["Hammad Ahmed"])
tup4=tuple(list(tup2)+[1])
print(tup3,'\n',tup4)
