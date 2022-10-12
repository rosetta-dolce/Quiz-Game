print ("Welcome to my Computer Quiz")

playing = input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("What is my favourite colour? ")
if answer.lower() == "pink":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("Do you like cats? ")
if answer.lower() == "yes":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

print ("you got " + str(score) + " questions correct!")
print ("you got " + str((score / 4) * 100)+ "%.")