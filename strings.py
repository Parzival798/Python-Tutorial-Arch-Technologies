# Strings

string1 = "this is me"
print(string1[0:2])
print(string1[-2:])
print(string1[:-2])
print(string1.capitalize())
print(string1.find("thisdsfdfd"))
print(string1.replace("is", "are"))

#String in detail
file1 = open("harry.txt", "wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Write this to my file", "UTF-8"))
file1.close()