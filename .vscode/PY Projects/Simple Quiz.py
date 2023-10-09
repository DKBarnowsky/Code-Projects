
print("Welcome to the Danny Quiz!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()            

print("Great, heres your first question!")

score = 0

answer = input("How old will Danny be in January 2023? ")
if answer == "21" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Does he enjoy programing? ")
if answer.lower() == "yes" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Did he serve a mission for the church? ")
if answer.lower() == "yes" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Is yellow his favorite color? ")

if answer.lower() == "yes" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("How many dogs live with Danny? ")
if answer == "3" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " +str(score) + " questions correct!")
print("You got " +str((score / 5) * 100) + " %.")

quit = input("Would you like to quit? ")
if (quit.lower()) != "no" :
    quit()
else:
    print("Stay as long as you need pal...")
