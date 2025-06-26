# If else statements

print("Enter Your Marks")
number = int(input())
print(number)

if (number>90 or number<100):
    grade = 'A'
elif (number>80 and number<100):
    grade = 'B'
else:
    grade = 'Dont Know'

print("The grade is", grade)
