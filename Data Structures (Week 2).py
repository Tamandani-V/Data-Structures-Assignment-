# Create an empty list
my_list = []
print("Empty list created:", my_list)

# Append elements
my_list.append(10)
my_list.append(20)    
my_list.append(30)
my_list.append(40) 
print("After appending elements:", my_list)

# Insert 15 at second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at position 2:", my_list)

# Extend with another list
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# Remove last element
removed_element = my_list.pop()
print(f"Removed last element ({removed_element}). List now:", my_list)  

# Sort list
my_list.sort()
print(my_list)

# Find index of value 30
index_30 = my_list.index(30)
print("Index of value 30 in my_list:", index_30)



