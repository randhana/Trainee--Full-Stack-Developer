#Dictionary
#Create an empty dictionary
new_Dictionary = dict()


my_dictionary={'saman':75,'nimal':80}
print(my_dictionary)
print(my_dictionary.get('nimal')) #items() keys() values()

#Adding a new element
my_dictionary['kasun']=76
print(my_dictionary)

#Updating an element
my_dictionary['kasun']=86
print(my_dictionary)

#removing an element
my_dictionary.pop('nimal')
#removing all elements
#my_dictionary.clear()
print(my_dictionary)

#get the list of all keys
allKeys = list(my_dictionary.keys())
print("ALL Keys: ",allKeys)

#get the list of all values
allValues = list(my_dictionary.values())
print("All Values: ",allValues)


#Iterating through a dictionary
for key in my_dictionary:
    print(key,my_dictionary[key])
