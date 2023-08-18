import ast

obj = {}
# Open the file in read mode
file = open("users.txt", "r")
content = file.read()
# print(content[0]["email"])
# Convert the content to a dictionary using ast.literal_eval
user_data = ast.literal_eval(content)

# Access and print the email key
key = user_data[0]["email"]
obj[key] = user_data[0]
print(obj)
