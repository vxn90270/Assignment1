it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# find the lenght of the set it_companies
print("Length of the set it_companies, ", len(list(set(it_companies))))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Add 'Twitter': ", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.add('Github')
it_companies.add('StackOverflow')
print('Insert multiple IT companies, ', it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Github")
print("Remove one of the companies from it_companies: ", it_companies)

# What is the difference between remove and discard
# The remove() method raises an error when the specified element doesn't exist in the given set, however the discard() method doesn't raise any error if the specified element is not present in the set and the set remains unchanged.

# Join A and B
print("Join A and B: ", A.union(B))

# Find A intersection B
print("Find A intersection B: ", A.intersection(B))

# Is A subset of B
print("Is A subset of B: ", A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets? ", A.isdisjoint(B))

# Join A with B and B with A
print("Join A with B: ", A.union(B))
print("Join B with A: ", B.union(A))

# What is the symmetric difference between A and B
# from Last element is not symmetric

# Delete the sets completely
A.clear()
B.clear()

print("Delete the sets completely: ", A)

# Convert the ages to a set and compare the length of the list and the list
age_set = set(age)

print("length of list ages: ", len(age))
print("length of set ages: ", len(age_set))