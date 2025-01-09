username = input("Enter an username: ")

temp_title = input("Enter a title: ")
temp_title2 = input("Enter a title2: ")
temp_title3 = input("Enter a title3: ")

title = [temp_title, temp_title2, temp_title3]

content = input("Enter a content: ")
status = input("Enter a status: ")
created_date = input("Enter a created date in format dd-mm-yy: ")
issue_date = input("Enter a issue date in format dd-mm-yy: ")

print(username)
print(title)
print(content)
print(status)
print(created_date[:-3])
print(issue_date[:-3])
