#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q3 Write a program to display current date and time.

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M
dt_string = now.strftime("%d/%m/%Y %H:%M")
print("date and time =", dt_string)


# In[ ]:


# Q4 Write a python program which takes radius of circle from the user and calculate the area.

import math as M  
Radius = float (input ("Please enter the radius of the circle: "))  
area_of_the_circle = M.pi* Radius * Radius  
print (" The area of the given circle is: ", area_of_the_circle)


# In[ ]:


# Q5 Write a python program to take user's first and last name and print them reversing order with space.

def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  
  
    # Given String  
    
str = "Arsalan Irfan"         
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) 


# In[ ]:


# Q6 Write a python program which takes two inputs from user and print them in addition.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
sum = a + b
print("sum of a and b is:", sum)


# In[ ]:


# Q7 Write a program which takes 5 inputs from user of differents subjects, total it generate marksheet using grades.

print("Enter Marks Obtained in 5 Subjects: ")
Computer = int(input("Enter marks of Computer"))
Science = int(input("Enter marks of Science"))
Maths = int(input("Enter marks of Maths"))
Islamiat = int(input("Enter marks of Islamiat"))
English = int(input("Enter marks of English"))
Total = 500

Obtain_marks = Computer+Science+Maths+Islamiat+English
percentage = Obtain_marks/Total*100

print(Obtain_marks);
print(percentage);

if avg>=91 and avg<=100:
    print("Your Grade is A+")
elif avg>=81 and avg<91:
    print("Your Grade is A")
elif avg>=71 and avg<81:
    print("Your Grade is B+")
elif avg>=61 and avg<71:
    print("Your Grade is B")
elif avg>=51 and avg<61:
    print("Your Grade is C+")
elif avg>=41 and avg<51:
    print("Your Grade is C")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E")
elif avg>=0 and avg<21:
    print("You are Fail")
else:
    print("Invalid Input!")


# In[ ]:


# Q8. Write a program which takes input from user and identify that the given number is even or odd.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[ ]:


# Q9 Write a program which print the length of the list.

inp_lst = ['Python','Java','C++','Ruby','asp.net']
size = len(inp_lst)
print(size)


# In[ ]:


# Q10 Write program to sum all the numeric item given in the list.

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[ ]:


# Q11 Write a python program to get the largest number froma list.

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, 8, 9, 12, -2, -7, 16]))


# In[ ]:


# Q12 Write a program to print out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

print(i)

