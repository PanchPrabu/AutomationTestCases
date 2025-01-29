#program to accept a filename from the user and print only the extension of the file

file_name=input('enter a file name with extension')
file_extension=file_name.split('.')
print(f"The extension for the file name {file_name} is:",file_extension[-1])