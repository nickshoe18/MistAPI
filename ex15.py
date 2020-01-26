# Imports the argument variable from system
from sys import argv
# Unpacking the argument variable and assigning filename to argument variable as well
script, filename = argv
#setting variable txt to open the file that is called out in the script from user input
txt = open(filename)
# Shows the filename from the argument assigned when running the script
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
# Setting the variable file_again to the filename
print("Type the filename again:")
file_again = input("> ")
# Opening the file again with the new variable name
txt_again = open(file_again)
# Printing the text within the newly assgined variables
print(txt_again.read())
txt_again.close()
