import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# Instantiate BST with the first name of name_1 as the root node
tree = BSTNode(names_1[0])
# Insert all names from names_1 into the tree(not including the root node name)
for name_1 in names_1[1:]:
    tree.insert(name_1)
# Loop through names_2 looking for duplicate names
for name_2 in names_2:
    # If it finds a duplicate
    if tree.contains(name_2):
        # Append those duplicate names into the duplicates list
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print (f"Θ(log(n)) time complexity? Honestly not really sure, but might as well guess one")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
