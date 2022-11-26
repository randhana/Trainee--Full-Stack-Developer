#Sets
#Cannot use indexes Unordered

my_set =set(['Apple','Banana','Orange'])
for i in my_set:
    print(i)


x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)

print(x|y)

result = x.intersection(y, z)
print(result)

print(x&y)


A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

# Equivalent to A-B
print(A.difference(B))

# Equivalent to B-A
print(B.difference(A))

print(A-B)
print(B-A)

set1 = set([4, 5, (6, 7)])

set1.update([5, 2, 6])

check1 = 2 in set1

check2 = 6 in set1

print(check1 and check2)