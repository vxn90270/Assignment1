# create an empty dictionary called dog
dog = {}

# add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Baby'
dog['color'] = 'White'
dog['breed'] = 'Bulldog'
dog['legs'] = 4
dog['age'] = 3
print("Dog dictionary")
print(dog)

# create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, address
student = {}
student['first_name'] = 'John'
student['last_name'] = 'Smith'
student['gender'] = 'Male'
student['age'] = 23
student['marital'] = 'Single'
student['skills'] = ['Computer Science', 'Maths', 'Computer Architecture']
student['country'] = 'USA'
student['city'] = 'New York'
student['address'] = '47 W 13th St, New York, NY 10011, USA'

print("Student dictionary")
print(student)

# get the length of the student dictionary
print("Length of the student dictionary: ", len(student.keys()))

# get the value of skills and check the data type. it should be a list
print("Skills: ", student['skills'])
print("Data types: ", type(student['skills']))

# modify the skills values by adding one or two skills
print("Modify the skills values ")
student['skills'].append('Programming Design')
print(student)

# Get the dictionary keys as a list
print("Get the dictionary keys")
keys = list(student.keys())
print(keys)

# get the dictionary values as a list
print("Get the dictionary values")
print(list(student.values()))