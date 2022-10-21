score = 0
answer = input("What time is it? ")
if answer == "time for you to get a watch":
    score = score + 1
    print("Great job!")
else:
    print("Gotcha! hehehehehe")
answer = input("How old is the president? ")
if answer == "too old":
    print("I know right?")
    score = score + 1
else:
    print("Nope. try again")
    answer = input("How old is the president? ")
    if answer == "too old":
        print("I know right?")
        score = score + 1
    else:
        print("Nope.")
answer = input("Are you right handed? ")
if answer == "yes":
    score = score + 1
    print("Me too!")
else:
    print("...why???")
    answer == input("")
    if answer == ".":
        print(".")
    else:
        print("Maybe you should ask for Cristmas.")
print("Your score is", score)