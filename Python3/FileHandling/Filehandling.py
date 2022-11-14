file1 = open("file1.txt","r")
line1 = file1.readline()
line2 = file1.readline()


file2 = open("file2.txt","w+")
file2.write(line1)
file2.write(line2)
content = file2.read()
file1.close()
file2.close()
print(content)
