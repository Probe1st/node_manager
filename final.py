
note = []

note.append(input("Enter an username: "))

temp_title = input("Enter a title: ")
temp_title2 = input("Enter a title2: ")
temp_title3 = input("Enter a title3: ")

note.append([temp_title, temp_title2, temp_title3])
note.append(input("Enter a content: "))
note.append(input("Enter a status: "))
note.append(input("Enter a created date in format dd-mm-yy: "))
note.append(input("Enter a issue date in format dd-mm-yy: "))

print(note)
