#!/usr/bin/env python3
#  Thursday afternoon challenge!

#  Create a function (or functions) to:
#      * accept two integers, multiply them, and return that value
#      * accept a string, and return the counts of the number of vowels and consonants in it

#  Then
#  Create a new file in which you pass a string to the function(s) you just created, and
#  multiply the number of vowels by the number of consonants.

#  Use the string:
#  "Look out!  I have learned enough Python to be dangerous!"

def mult(int1, int2):
    answer = int1 * int2
    return answer

print(mult(7, 4))

def string(str1):
    str1 = input("Please Enter Your Own String : ")
    vowels = 0
    consonants = 0
    
    for i in str1:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
        else:
            consonants = consonants + 1
        print("Total Number of Vowels in this String = ", vowels)
        print("Total Number of Consonants in this String = ", consonants) 
    return str1

print(string(str1))

