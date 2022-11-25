#stack implemaentation
#Real world application: Undo function
my_stack = []

#push data
def push(stack, value):
    stack.append(value)

#pop data
#.pop built  in function in py, 
# no need to track pointer
    
def pop(stack):
    return stack.pop()  


push(my_stack,10)
push(my_stack,20)
print("new my stack: ",my_stack)
pop(my_stack)
print("After pop my stack: ",my_stack)

