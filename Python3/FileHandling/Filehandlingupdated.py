file1 = open("file1.txt","r")
file2 = open("file2.txt","w+")

line1 = file1.readline()
line2 = file1.readline()

file1.close()

file2.write(line1)
file2.write(line2)

file2.close()
file2 = open("file2.txt","r")
content = file2.read()


file2.close()

print(content)
