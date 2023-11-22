import os # This module provides a portable way of using operating system dependent functionality.
import shutil # This module provides a number of high-level operations on files and collections of files.

lorem_path = f"{os.getcwd()}/python_basics_advanced/input.txt"
copy_path = f"{os.getcwd()}/python_basics_advanced/copy.txt"

# Open the file in read mode
file = open(lorem_path, "r")

# Read the contents of the file
contents = file.read()

# Create a new file in write mode
file_copy = open(copy_path, "w")

# Use the write operation to write the contents to a new file
file_copy.write(copy_path)
file_copy.close()

file_copy = open(copy_path, "r")
file_copy_contents = file_copy.read()
print(file_copy_contents)
file_copy.close()

# Use the write operation to write the contents to an existing file
file_copy = open(copy_path, "w")
file_copy.write(contents)
file_copy.close()
  
# Print the contents to the console
file_copy = open(copy_path, "r")
file_copy_contents = file_copy.read()

print(file_copy_contents)

# Close the file
file_copy.close()

# Work with the 'with' statement
# Open the file in read mode
# Read the contents of the file
with open(lorem_path, "r") as file:
    print(file.read())

# Use the write operation to write the contents to a new file
with open(copy_path, "w") as file_copy:
    file_copy.write(contents)


# Use the write operation to write the contents to an existing file
with open(copy_path, "w") as file_copy:
    file_copy.write(file_copy_contents)
  
# Print the contents to the console
with open(copy_path, "r") as file_copy:
    print(file_copy.read())
