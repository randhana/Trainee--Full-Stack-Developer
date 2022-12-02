#Tuples

my_tuple = (10,20,30)
my_tupleWithoutparan = 'a','b','c','d'

print(my_tuple)

#access values
print(my_tuple[-1]) #last element

#slicing
print(my_tuple[0:3])

#nested tuples
nestedTuple = ((1,2),('a','b'))
#print(nestedTuple[1][1])

#tuple packing
a,b,c = my_tuple
print(a)
print(b)
print(c)

#Insertion
my_tuple[0] =100
#print(my_tuple ) Tuples are immutable