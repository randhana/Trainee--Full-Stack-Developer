

"Complete the code to take the input as an integer and output a square of "*" characters. "

def starptn():
    
    val = int(input())
    for x in range(0,val):
        for r in range(0,val):

            print('*',end='')
        print('') #default print() --> new line '\n'


""" 
Complete the code to find if a given number is a prime number? 
The program will take a positive integer greater than 1 as input and indicate if it is a prime number by saying "prime", and if it is not a prime number saying "not a prime". 
Note there are 3 places in the given code that you need to fix for this code to work properly and give the expected output. 
"""


def isPrime():
    i = int(input())
    j = 2 # fix the code (1) 
    while (j <= (i/j)):
        if not(i%j): 
            print("not a prime")
            break; # fix the code (2)
        j = j + 1 # fix the code (3)
    if (j > i/j): 
        print ("prime")

isPrime()
