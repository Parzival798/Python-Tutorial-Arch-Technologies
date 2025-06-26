file1 = open("harry.txt", "wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Write this to my file", "UTF-8"))
file1.close()

# file io - reading the content of a file

file1 = open('harry.txt', 'r+')
text_to_read = file1.read()
print(text_to_read)
