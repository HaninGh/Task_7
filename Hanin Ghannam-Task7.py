#Q1
# Create a new list.
names = ["Tanteel", "Asmaa", "Ahmed"]

# Add a new item to the start.
names.insert(0, "Sabrin")
print(names)

# Remove the last item.
names.pop()
print(names)

# Add a new item at the end.
names.append("Hamda")
print(names)

# Remove the third item.
names.remove("Asmaa")
print(names)

#Q2
# Create three new lists.
friends = ["Adel", "Ahmed"]
employees = ["Samah", "Anjad"]
school = ["Ali", "Basma"]
# Merge the lists.
all_people = friends + employees + school
print(all_people)

#Q3
dictionary1 = {1: 10, 2: 20}
dictionary2 = {3: 38, 4: 40}
dictionary3 = {5: 50, 6: 60}

# Concatenate the dictionaries.
new_dictionary = {**dictionary1, **dictionary2, **dictionary3}

# Print the new dictionary.
print(new_dictionary)

#Q4 uses a for loop to iterate over the numbers from 1 to 15 and creates a dictionary where the key is the number and the value is the square of the number.
# Create  an empty dictionary
squares = {}
# Using range function to iterate over the numbers from 1 to 15.
for number in range(1, 16):
  # Calculate the square of the number.
  square = number ** 2

  # Add the number and its square to the dictionary.
  squares[number] = square

#Q5
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 200, 'd': 400}

# Combine two dictionaries by adding values for common keys
d3 = {**d1, **d2}

# Print the combined dictionary
print(d3)

#Q6
keys = ['Ten', 'Twenty', 'Thinty']
values = [10,20, 50]

# Combine the two lists into a single iterable
zipped_list = zip(keys, values)
# Create a dictionary from the iterable
d = dict(zipped_list)
print(d)

#Q7
sampleDict = {
"class": {
"student": {
"name": "Mike",
"marks": {
"physics": 70,
"history": 80
}
}
}
}

# Get the value of the key 'history'
history_mark = sampleDict["class"]["student"]["marks"]["history"]

# Print the value
print(history_mark)

#Q8
myDict = {1: "Alaa", 5: "Hadeel", 7: "Hanin", 13: "Malak"}

for key, value in myDict.items():
    if key < 10:
        print(value, end="->")

print()




