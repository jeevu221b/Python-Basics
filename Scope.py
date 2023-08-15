import ast

# Open the file in read mode
file = open("users.txt", "r")
content = file.read()

# Convert the content to a dictionary using ast.literal_eval
user_data = ast.literal_eval(content)

# Access and print the email key
print(len(user_data))
