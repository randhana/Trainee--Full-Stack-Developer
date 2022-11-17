#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def Addition(a,b):
    return a+b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    try:
        return a/b
    except ZeroDivisionError:  #Division by zero
            print("float division by zero")
            return None

def Power(a,b):
    return a**b

def Remainder(a,b):
    return a % b

#Control Operations

def Terminate():
    print("Done. Terminating")
    exit()
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    validChoices =[ '+','-','*','/','^','%','#','$']
    if (choice in validChoices):
        if choice == '#':
            return -1
        if choice == '$':
            return 0
        
        first = (input("Enter first number: "))
        print(first)
        if first.endswith('$'):
            return 0
        second = (input("Enter second number: "))
        print(second)
        if second.endswith('#'):
            return -1
        try:
            a = float(first)
            b = float(second)

        except ValueError:
            
            return
        if choice == '+':
            print(a,'+',b,'=',Addition(a,b))
        if choice == '-':
            print(a,'-',b,'=',Subtraction(a,b))
        if choice == '*':
            print(a,'*',b,'=',Multiplication(a,b))
        if choice == '/':
            print(a,'/',b,'=',Division(a,b))
        if choice == '^':
            print(a,'^',b,'=',Power(a,b))
        if choice == '%':
            print(a,'%',b,'=',Remainder(a,b))
        
    else:
        print("Unrecognized operation")

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()