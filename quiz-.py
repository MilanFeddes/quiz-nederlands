# Defining Score variables 
x = 0
score = x

# vraag 1
print("")
answer_1 = input("a)Zegt wat iets of iemand doet of overkomt.\nb)Kan in verschillende vormen voorkomen.:")
if answer_1.lower() == "a" or answer_1.lower() == "b":
    print("Correct, Goed zo")
    x = x + 1
else:
    print("Incorrect, A is goed")

# vraag 2
print("Wat is een lidwoord?")
answer_1 = input("a)De, het, een\nb)Zegt iets over het zelfstandige naamwoord.:")
if answer_1.lower() == "a" or answer_1.lower() == "b":
    print("Correct, Goed zo")
    x = x + 1
else:
    print("Incorrect, A is goed")

# vraag 3
print("Wat is een zelfstandige naamwoord?")
answer_1 = input("a)Zegt iets over een stof.\nb)Woord voor een mens,dier,plant of ding.") 
if answer_1.lower() == "a" or answer_1.lower() == "b":
    print("Correct, Goed zo")
    x = x + 1
else:
    print("Incorrect, A is goed")

# vraag 4
print("Wat is een zelfstandige naamwoord?")
answer_1 = input("a)Zegt iets over een stof.\nb)Woord voor een mens,dier,plant of ding.") 
if answer_1.lower() == "a" or answer_1.lower() == "b":
    print("Correct, Goed zo")
    x = x + 1
else:
    print("Incorrect, A is 

#Total Score
score = float(x / 5) * 100
print(x,"van de 5, is goed",score, "%")