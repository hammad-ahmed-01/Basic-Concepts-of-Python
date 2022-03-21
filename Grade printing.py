# Author == Hammad Ahmed
# Python IDLE

#a program to enter marks in five subjects and print the grades based on their average
#taking marks in five subjects as INPUT
a=float(input(" Enter the marks in first subject : ")) #a represents the marks in first subject
b=float(input(" Enter the marks in second subject : "))#b represents the marks in second subject
c=float(input(" Enter the marks in third subject : "))#c represents the marks in third subject
d=float(input(" Enter the marks in fourth subject : "))#drepresents the marks in fourth subject
e=float(input(" Enter the marks in fifth subject : "))#e represents the marks in fifth subject
#the average will be calculated by dividing the sum of the subject marks by total number of subjects
#sum variable represnts the sum of the marks of five subjects
sum=a+b+c+d+e
#avg variable represents the average of the marks of five subjects
avg=sum/5
#the average will be printed to the screen as follows
print(" The average marks are ", avg)
#the grades will be assigned using if condition
#if the average is higher than or equal to 90 and smaller than 100, then it will print grade A
if (avg>=90 and avg<=100):
 print( " The grade is A ")
#if the average is higher than or equal to 80 and smaller than 90, then it will print grade B
elif (avg>=80 and avg<90):
 print(" The grade is B ")
#if the average is higher than or equal to 70 and smaller than 80, then it will print grade C 
elif (avg>=70 and avg<80):
 print(" The grade is C ")
#if the average is higher than or equal to 60 and smaller than 70, then it will print grade D 
elif (avg>=60 and avg<70):
 print(" The grade is D ")
#if the average is higher than or equal to 50 and smaller than 60, then it will print grade E 
elif (avg>=50 and avg<60):
 print(" The grade is E ")
 #if the average is higher than or equal to 0 and smaller than 50, then it will print grade F 
elif (avg>=0 and avg<50):
 print(" The grade is F ")
#The grades, according to the average marks are A,B,C,D,E and F
else:
 print(" Write the correct numbers ")
#if the average marks are not between 0 to 100, then the else option will be printed
