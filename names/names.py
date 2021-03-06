import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# PLAN: 
# 1) build binary search tree on names_1
# 2) traverse binary serach tree with name 2 for duplicates

# build binary search tree on names_1
names_tree = BinarySearchTree(names_1[0])
for i in range(1, len(names_1) - 1):
    names_tree.insert(names_1[i])

# traverse binary serach tree with names_2
for name in names_2:
    if names_tree.contains(name):
        duplicates.append(name)

# names_tree.in_order_print(names_tree)

# 6 second runtime code
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
