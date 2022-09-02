# create a tuple containing names of your sisters and your brothers
new_tuple = ('John Smith', 'Liam Olivia', 'Noah Emma', 'Oliver Charlotte', 'Elijah Amelia')
print("New tuple: ", new_tuple)

# join brother and sisters tuples and assign it to siblings
siblings = (('James Ava', 'William Ava'), ('Lucas Mia', 'Henry Mia'), ('Theodore Marper', 'Benjamin Marper'))
print("Join brothers and sisters, assign it to siblings: ", siblings)

# How many siblings do you have
num_siblings = 0
for i in range(len(siblings)):
	if type(siblings[i]) == tuple:
		num_siblings += 1
print("Number of siblings: ", num_siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ()
siblings = list(siblings)
siblings[0] = siblings[0] + (("Joseph Ava", "Asher Ava"),)
siblings[1] += (("Aiden Mia", "Wyatt Mia"),)
siblings[2] += (("Jacob Marper", "Ethan Marper"),)

family_members = tuple(siblings)
print("Family member: ", family_members)