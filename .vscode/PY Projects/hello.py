#Ask user for their name
name = input("What's your name? ").strip().title()

#split user name into first and last
first, last = name.split(" ")

#Say hello to user
print(f"Hello, {first}")

