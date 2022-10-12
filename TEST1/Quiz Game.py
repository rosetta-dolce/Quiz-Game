print ("Welcome to my Computer Quiz")

playing = input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play ")
score = 0

answer = input("What is the capital of Madagascar? ")
if answer.lower() == "Antananarivo":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("Where can you find the famous Mona Lisa painting? ")
if answer.lower() == "Louvre":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("Was Mozart a well known composer? ")
if answer.lower() == "yes":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

print ("you got " + str(score) + " questions correct!")
print ("you got " + str((score / 4) * 100)+ "%.")
