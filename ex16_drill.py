from sys import argv

script, username = argv
filename = input("enter filename here: ")
print(f" {username}, I'm gpoing to read {filename}.")

txt = open(filename)
print(txt.read())
