ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sort the list and find the min and max age
for n in range(len(ages)-1, 0, -1):
	for i in range(n):
		if ages[i] > ages[i + 1]:
			ages[i], ages[i + 1] = ages[i + 1], ages[i]
print("Sorted list")
print(ages)

min_value = ages[0]
max_value = ages[-1]
print("Min Value: ", min_value)
print("Max Value: ", max_value)

# add the min age and max age again to the list
ages.append(min_value)
ages.append(max_value)
print("List after add min and max value: ", ages)

# find the median age
print("Median age")
if(len(ages) % 2 == 0):
	print((ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2)
else:
	print(ages[len(ages) / 2])

# find the average age
print("Average Age")
sum_value = 0
for i in range(len(ages)):
	sum_value += ages[i]
print(sum_value / len(ages))

# find the range of ages
print("Range of ages")
print(max_value - min_value)