pquestions = {
    "1. What is the correct way to print 'Hello, World!' in Python?": "C",
    "2. Which symbol is used to start a comment in Python?": "C",
    "3. Who created Python?": "B",
    "4. In which year was Python invented?": "A",
    "5. Python is tributed to which comedy group?": "D"
}
poptions = [
    ["A. echo('Hello, World!')", "B. printf('Hello, World!')", "C. print('Hello, World!')", "D. print Hello, World!"],
    ["A. //", "B. /*", "C. #", "D. <!--"],
    ["A. Elon Musk", "B. Guido van Rossum", "C. Elbert Einstein", "D. Newton"],
    ["A. 1991", "B. 1989", "C. 2025", "D. 3021"],
    ["A. Lonely Island", "B. Smosh", "C. SNL", "D. Monty Python"]
]

cquestions = {
    "1. Who developed the C++ programming language?": "B",
    "2. What is the latest stable version of C++ as of 2024?": "A",
    "3. C++ is an extension of which programming language?": "D",
    "4. Which of the following is a valid C++ data type?": "A",
    "5. Which symbol is used to end a statement in C++?": "D"
}
coptions = [
    ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. James Gosling", "D. Guido van Rossum"],
    ["A. C++23", "B. C++20", "C. C++14", "D. C++11"],
    ["A. Java", "B. Python", "C. Pascal", "D. C"],
    ["A. int", "B. integer", "C. number", "D. digit"],
    ["A. :", "B. .", "C. ,", "D. ;"]
]

jquestions = {
    "1. Who developed the Java programming language?": "C",
    "2. What is the latest stable version of Java as of 2024?": "D",
    "3. Which keyword is used to define a class in Java?": "C",
    "4. Which method is the entry point of any Java program?": "A",
    "5. What type of programming language is Java?": "B"
}
joptions = [
    ["A. Bjarne Stroustrup", "B. Dennis Ritchie", "C. James Gosling", "D. Guido van Rossum"],
    ["A. Java 8", "B. Java 11", "C. Java 17", "D. Java 21"],
    ["A. function", "B. define", "C. class", "D. struct"],
    ["A. main()", "B. start()", "C. init()", "D. run()"],
    ["A. Functional", "B. Object-oriented.", "C. Assembly", "D. Procedural"]
]


def check_answers(answer, guess):
    if answer == guess:
        print("✔️ Correct")
        return 1
    else:
        print("❌ Incorrect")
        return 0

def display_score(correct_guess, guesses, answer_key):
    print("---------------------------------------------------")
    print("RESULTS")
    print("Answers:", end=" ")
    for i in answer_key:
        print(answer_key.get(i), end=" ")
    print("\nGuesses:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print("\nYour score is:", correct_guess, "/", len(answer_key))


def py_quiz():
    guesses = []
    correct_guess = 0
    question_num = 1
    for key in pquestions:
        print("---------------------------------------------------")
        print(key)
        for i in poptions[question_num - 1]:
            print(i)
        guess = input("Enter your answer (A B C D)? : ").upper()
        guesses.append(guess)
        correct_guess += check_answers(pquestions.get(key), guess)
        question_num += 1
    display_score(correct_guess, guesses, pquestions)

def c_quiz():
    guesses = []
    correct_guess = 0
    question_num = 1
    for key in cquestions:
        print("---------------------------------------------------")
        print(key)
        for i in coptions[question_num - 1]:
            print(i)
        guess = input("Enter your answer (A B C D)? : ").upper()
        guesses.append(guess)
        correct_guess += check_answers(cquestions.get(key), guess)
        question_num += 1
    display_score(correct_guess, guesses, cquestions)

def j_quiz():
    guesses = []
    correct_guess = 0
    question_num = 1
    for key in jquestions:
        print("---------------------------------------------------")
        print(key)
        for i in joptions[question_num - 1]:
            print(i)
        guess = input("Enter your answer (A B C D)? : ").upper()
        guesses.append(guess)
        correct_guess += check_answers(jquestions.get(key), guess)
        question_num += 1
    display_score(correct_guess, guesses, jquestions)


def menu():
    print('''\nChoose what topic you want to play quiz on!
    1. Python
    2. C++
    3. Java
    ''')
    user = int(input("Enter your choice: "))
    if user == 1:
        print("Starting your quiz on Python")
        py_quiz()
    elif user == 2:
        print("Starting your quiz on C++")
        c_quiz()
    elif user == 3:
        print("Starting your quiz on Java")
        j_quiz()
    else:
        print("Choose options from 1-3")

def Play_again():
    response = input("\nDo you want to play again? (yes/no): ")
    response = response.strip().upper()
    return response == "YES"


while True:
    menu()
    if not Play_again():
        print("Thanks for playing! 👋")
        break
