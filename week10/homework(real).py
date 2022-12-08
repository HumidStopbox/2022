quiz =  [
    {
        "question": "choose knowlage to obtain:",
        "choices": [
            "happy birthday lyrics",
            "letters of alphabet",
            "worlds oldest president",
            "worlds best mom"
        ],
        "a": "happy birthday lyrics",
        "b": "letters of alphabet",
        "c": "worlds oldest president",
        "d": "worlds best mom"
    }
]

problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f"  {choice}")

    guess = input("Your choice: ")
    if guess == problem['a']:
        correct =+ 1
        print() #print a blank line for space
        print(f"Happy Birthday to You, Happy Birthday to You, Happy Birthday Dear (name), Happy Birthday to You.")
    
    elif guess == problem['b']:
        correct =+ 1
        print() #print a blank line for space
        print(f"A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    
    elif guess == problem['c']:
        correct =+ 1
        print() #print a blank line for space
        print(f"JOE BIDON!!!")
    
    elif guess == problem['d']:
        print() #print a blank line for space
        correct =+ 1
        print(f"your mom")
    
    else:
        print() #print a blank line for space
        print(f"Oops. Run the program again and type out a given choice.")

    print() #print a blank line for space

print(f"correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")