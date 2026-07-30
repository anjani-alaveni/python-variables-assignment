# List Datatype Practice Assignment

# Task 1: Create a list containing numbers 1 through 5
numbers_list = [1, 2, 3, 4, 5]
print("numbers_list:", numbers_list)


# Task 2: Append number 6 to the end of the list
numbers_list.append(6)
print("Append function:-", numbers_list)


# Task 3: Insert number 0 at the beginning
numbers_list.insert(0, 0)
print("Insert function:", numbers_list)


# Task 4: Remove the first occurrence of number 2
numbers_list.remove(2)
print("Remove function:", numbers_list)


# Task 5: Sort the list in ascending order
numbers_list.sort()
print("Sorted function:-", numbers_list)


# Task 6: Print the third element using indexing
print("Third element =", numbers_list[2])


#  Create a copy using slicing
copied_list = numbers_list[:]
print("copied_list", copied_list)
