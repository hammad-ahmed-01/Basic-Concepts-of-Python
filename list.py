# Author == Hammad Ahmed
# Python IDLE

# a program to make list by user input and find Maximum,Minimum,Sum and Average of the list
# making a list by append function in for loop
a=int(input("Enter the length of the list:"))
list1 = []
for i in range(a):
    b=int(input("Enter the elements:"))
    list1.append(b)
# defining function myMax() and myMin() to find maximum and minimum number in the list
def myMax(list1):
    MAX = list1[0]
    for x in list1:
        if x > MAX :
             MAX = x
    return MAX
def myMin(list1):
    MIN = list1[0]
    for x in list1:
      if x < MIN :
        MIN = x
    return MIN
print("Largest element is:", myMax(list1))
print("Smallest element is:", myMin(list1))
# finding sum and average of numbers in the list
count = 0
for i in list1:
    count += i
avg = count/len(list1)  
print("sum = ", count)
print("average = ", avg)
