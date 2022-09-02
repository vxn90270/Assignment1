# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)
conv = 0.45359237
N = int(input("Please input number of students: "))
students = []
for i in range(N):
	lbs = input("Please input lbs: ")
	students.append(float(lbs))
print(students)

output = []
for i in range(len(students)):
	output.append(round(float(lbs) * conv, 2))
print(output)