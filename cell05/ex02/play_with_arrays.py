old_array = [2, 8, 9, 48, 8, 22,-12, 2]
new_array = [x+2 for x in old_array if x > 5]
print("Original array:", old_array)
print("New array:", new_array)