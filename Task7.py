#Task1: Create a text file with current timestamp
import calendar
import datetime
import os


print("Program to create text file with current timestamp")
print("")
print("         **************************            ")
print("")
text_file = open("sample.txt", "w")
# ct stores current time
ct = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
text_file.write("Current timestamp is: ")
text_file.write(ct)
print("Text file created")
text_file.close()
print("")
print("-------------------------------------------------")
print("")

#Task2: Print the content in the text file
print("Program to read the content in the text file:")
print("")
print("         **************************            ")
print("")
text_file = open ("sample.txt", "r")
print("Content in the selected text file is: ")
print(text_file.read())
print()
text_file.close()
print("")
print("-------------------------------------------------")
print("")

#Task2: Print the name of the file
print("Program to Print the name of the file:")
print("")
print("         **************************            ")
print("")
# Path
path = 'D:\Python WorkSpace\sample.text'
basename = os.path.basename(path) 
# Print the base name  
print("Name the file is: ", basename)
print("")
print("-------------------------------------------------")
print("")