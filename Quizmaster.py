import random
import time
import os
money = 0
x = 1
questions_asked = []

def questions(end): # function that calls the questions
    x = 1
    while x % 2 != 0:
        x = random.randint(0,end)
    return x+1

def answers(end): # function that varifys the answer
    x = 1
    while x % 2 == 0:
        x = random.randint(0,end)
    return x+1

print(" $$$$$$\            $$\                                               $$\ ")  # lines 20 too 36 are an opening visual
time.sleep(0.4)
print("$$  __$$\           \__|                                              $$ | ")
time.sleep(0.4)
print("$$ /  $$ |$$\   $$\ $$\ $$$$$$$$\ $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\ ")
time.sleep(0.4)
print("$$ |  $$ |$$ |  $$ |$$ |\____$$  |$$  _$$  _$$\  \____$$\ $$  _____|\_$$  _|  $$  __$$\ $$  __$$\ ")
time.sleep(0.4)
print("$$ |  $$ |$$ |  $$ |$$ |  $$$$ _/ $$ / $$ / $$ | $$$$$$$ |\$$$$$$\    $$ |    $$$$$$$$ |$$ |  \__| ")
time.sleep(0.4)
print("$$ $$\$$ |$$ |  $$ |$$ | $$  _/   $$ | $$ | $$ |$$  __$$ | \____$$\   $$ |$$\ $$   ____|$$ |   ")
time.sleep(0.4)
print("\$$$$$$ / \$$$$$$  |$$ |$$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |      ")
time.sleep(0.4)
print(" \___$$$\  \______/ \__|\________|\__| \__| \__| \_______|\_______/    \____/  \_______|\__|      ")
time.sleep(0.4)
print("     \___|  ")

print("welcome to quizmaster! The game where you can become rich by answering questions!")
name = input("to start, what is your name?")
print("welcome to quizmaster " + name + "!")
play = input("have you been on quizmaster before?")
play = play.lower()
while x == 1:  # while statement is used to ensure the user enters either yes or no
    if play == "yes":
        input2 = input("would you like to import your saved data?")
        input2 = input2.lower()
        if input2 == "yes":
            os.chdir("..")
            os.chdir("Questions")
            q = open("saved_data.txt", "r")
            empty = []
            lines2 = q.readlines() # this puts the reading lines function into a new variable
            tt = len(lines2)
            empty.append(lines2[0].strip()) # this line and 55 accesses the index of the lines and adds them to an empty list
            empty.append(lines2[1].strip())
            empty.append(lines2[2].strip())
            for s in range(3,tt):  # this block appends the questions that have been previously asked to the questions_asked list based on how many questions there are
                questions_asked.append(lines2[s].strip())
            y = empty[1] # this sets the iteration variable to the value the user was on when they saved the game
            y = int(y)  # this converts the value of 'y' which was a string to a int, same idea is used on line 59
            money = empty[2] #this sets the money variable to what they had in their saved data
            money = int(money)
            print("great!, welcome back " + str(empty[0]))
            print("you currently have $" + str(empty[2]) + "and are on question " + str(y))
        elif input2 == "no":
            print("great! our categories you can choose from today are history of Toronto, Toronto sports, and general Toronto Trivia")
            print("also, if at any time you would like to save your progress, type 'save ")
            y = 1  # if the user has no saved data, the iteration variable is set to 1
        else:
            input2 = input("would you like to import your saved data?")  # defensive coding
        x = x + 1  # x = x + 1 ends the while loop
    elif play == "no":
        print("""great! how quiz master works is there are 3 categories of trivia to choose from and for each question you get right, you win money, and for each you get wrong you lose money""")
        print("today, the categories you can choose from are history of Toronto, Toronto sports, and general Toronto Trivia")
        print("if at anytime you want to save your progress, type 'save' ")
        y = 0
        x = x + 1
    else:
        play = input("have you been on quizmaster before?")
for y in range(y,10):  # y variable in the range is used to load the saved data
    input1 = input("which category would you like to choose from? (history, sports, or general)")
    input1 = input1.lower()

    if input1 == "save":
        print("your data will be saved")
        os.chdir("..")
        os.chdir("Questions")
        try:  # try except is used so if the file "saved_data.txt" exists, no error happens
            g = open("saved_data.txt", "x")
        except:
            g = open("saved_data.txt", "w")  # lines 86 to 89 save the iteration value, money, and questions asked list to the "saved_data.txt" file
            g.write('{}'.format(name) + '\n')
            g.write('{}'.format(y) + '\n')
            g.write('{}'.format(money) + '\n')
            g.write('\n'.join(questions_asked))
            exit()

    if input1 == "history":
        print("great choice, your question is ...")
        os.chdir("..")
        os.chdir("Questions")
        f = open("History.txt", "r")
        f1 = f.readlines()
        lines = f1
        z = questions(len(lines))  # this takes the questions function and picks an index based on the length of the line * note this logic and all other comments for history section apply to the other sections
        question = lines[z]
        while question in questions_asked:  # while loop is used so if a question choosen has been picked, a new one will be pick
            z = questions(len(lines))
            question = lines[z]
        answer = lines[z + 1]  # answer is on the next line after the question, so this line accesses the answer
        print(question)
        rr = questions_asked.append(question)
        answer_history = input("what is your answer?").strip()
        answer_history = answer_history.lower()
        if answer_history == answer.strip():
            print("correct! you will be awarded $100 for completing that question")
            money = money + 100
        else:
            print("im sorry, that is not correct!")
            print("the correct answer is " + str(answer))
            money = money - 100
            if money < 0:  # this is so the users money cant reach negitive values
                money = money + 100


    elif input1 == "sports":
        os.chdir("..")
        os.chdir("Questions")
        c = open("Sports.txt", "r")
        f2 = c.readlines()
        lines = f2
        ty = questions(len(lines))
        question = lines[ty]
        while question in questions_asked:
            ty = questions(len(lines))
            question = lines[ty]
        answer = lines[ty + 1]
        print(question)
        rr = questions_asked.append(question)
        answer_sports = input("what is your answer?").strip()
        answer_sports = answer_sports.lower()
        if answer_sports == answer.strip():
            print("correct! you will be awarded $100 for completing that question")
            money = money + 100
        else:
            print("im sorry, that is not correct!")
            print("the correct answer is " + str(answer))
            money = money - 100
            if money < 0:
                money = money + 100

    elif input1 == "general":
        print("excellent choice, your question is...")
        os.chdir("..")
        os.chdir("Questions")
        e = open("General.txt", "r")
        f3 = e.readlines()
        lines = f3
        ff = questions(len(lines))
        question = lines[ff]
        while question in questions_asked:
            ff = questions(len(lines))
            question = lines[ff]
        answer = lines[ff + 1]
        print(question)
        rr = questions_asked.append(question)
        answer_sports = input("what is your answer?").strip()
        answer_sports = answer_sports.lower()
        if answer_sports == answer.strip():
            print("correct! you will be awarded $100 for completing that question")
            money = money + 100
        else:
            print("im sorry, that is not correct!")
            print("the correct answer is " + str(answer))
            money = money - 100
            if money < 0:
                money = money + 100

    else:
        print("sorry! " + input1 + " isnt a category!")


if money == 0:
    print("im sorry! you did not win any money")
if money >= 100 and money <= 399:
    print("congratuations! you did ok! you won $" + str(money) + "!")
if money >= 400 and money <= 699:
    print("congratuations! you did well! you won $" + str(money) + "!")
if money >= 700 and money <= 999:
    print("Congratuations! you did great! you won $" + str(money) + "!")
if money == 1000:
    print("Congratulations! you did amazing you got every question right and won yourself $" +str(money) + "!")