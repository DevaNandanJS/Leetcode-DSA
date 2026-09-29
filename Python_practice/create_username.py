# create username

username= str(input("Enter your username: "))

if len(username)>12:
    print(f"your username {username} is more than 12 numbers")

elif not username.find(" ") == -1:
    print(f"Your username {username} has space in it")

elif not username.isalpha():
    print(f"your username {username} cannot contain digits")

else:
    print(f"username accepted: {username}")

