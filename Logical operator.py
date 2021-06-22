# coding by Md Arif Uddin
# Python logical operator using . I give three example
# Example 1

"""

num1 = 23
num2 = 45
num3 = 102

if num1 > num2 and num1 > num3 :
  print("number 1 large ",num)

elif num2>num1 and num2 > num3:
 print("Number 2 is large ",num2)

else:
    print("number three is large ",num3)

"""
# Example 2
# we find out vowel and consonant
# we know vowel is : a,e,i,o,u

"""
# Example 2 code start 
ch = 'B' 

if ch == 'a'or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
  print("This latter is a vowel")

else:
    print("This latter is consonant")

    # Example 2 code End

    """

# Example three 
# Letter Grade System program

marks = 20

if marks >= 80 and marks <= 100:
    print("A+")

elif marks >= 75 and marks <= 79:
    print("A")

elif marks >= 70 and marks <= 74:
    print("A-")

elif marks >= 65 and marks <= 69:
    print("B")

elif marks >= 60 and marks <= 64:
    print("B-")

elif marks >= 55 and marks <= 59:
    print("C")

elif marks >= 50 and marks <= 54:
    print("C-")

elif marks >= 40 and marks <= 49:
    print("D")

else:
    print("Fall")






