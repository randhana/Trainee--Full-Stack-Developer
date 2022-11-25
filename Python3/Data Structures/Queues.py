#Queues implementation using list
#Real world application of queues: File reading in computers
#head,tail

my_list = []

#Enqueue fun
def enqueue(queue, value):
    queue.append(value)

#Dequeue fun
def dequeue(queue):
    return queue.pop(0) #0 index means 1st one


enqueue(my_list,10)
enqueue(my_list,20)
enqueue(my_list,30)
print("new queue",my_list)
dequeue(my_list)
print("After dequeue by 1 time",my_list)
dequeue(my_list)
print("After dequeue by 2 time",my_list)



