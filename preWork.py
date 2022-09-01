#Complete these 5 questions to test your understanding of the 
# python pre-work material.  You will upload this to a github.com 
# repository and submit the link to that repository in 
# your google classroom.

#Please save your 5 functions to one .py file demark the 
# question numbers and the question in a comment above it's 
# respective function


#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the 
# input of the function. The first line of the code has been 
# defined as below.

 
from ast import Num
from urllib import response


def hello_name(user_name):
    response = input(f"Please enter your username: ")
    print(f"hello_{response.upper()}!")
hello_name(response)


#Question 2
# Write a python function, first_odds that prints the odd 
# numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1,101):
       if number % 2 != 0:
            print(number, end="\n")
first_odds()

#Question 
# Please write a Python function, max_num_in_list to return 
# the max number of a given list. The first line of the code
# has been defined as below.


def max_num_in_list(a_list):
    return (max(a_list))
a_list =  [1,99,103,-42,-162,1500]
print(max_num_in_list(a_list))



#Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be 
# boolean Type (true/false).

    
 
def is_leap_year(a_year):
    if  int(inputYear) % 4 == 0:
        return True
    elif int(inputYear) % 100 == 0 and int(inputYear) % 400 == 0:
        return True
    else:
        return False
inputYear = (input ("Enter a 4-digit year: "))
print (is_leap_year(inputYear))


#Question 5
# Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are 
# consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

 
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+ 1))
a_list = [2,3,4,6,7]
print(is_consecutive(a_list))