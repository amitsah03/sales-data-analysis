import random
def quizgame():
    quiz_data = [
        {"question": "What is the output of '2 ** 3' in Python?", "options": ["A) 8", "B) 6", "C) 9", "D) Error"], "answer": "A"},
        {"question": "Which data type is immutable in Python?", "options": ["A) List", "B) Tuple", "C) Dictionary", "D) Set"], "answer": "B"},
        {"question": "What keyword is used to define a function in Python?", "options": ["A) loop", "B) define", "C) def", "D) function"], "answer": "C"},
        {"question": "Which loop executes at least once before checking the condition?", "options": ["A) for loop", "B) while loop", "C) if-else", "D) do-while loop"], "answer": "D"},
        {"question": "What is the correct way to access a dictionary value?", "options": ["A) dict[key]", "B) dict.value", "C) dict->key", "D) dict.get"], "answer": "A"}
    ]
    random.shuffle(quiz_data) # shuffle questions for randomness
    question_number = 0
    score = 0
    for i,data in  enumerate (quiz_data):
        print(f"\nQ{i+1}.",data["question"])
        for option in data["options"]:
            print(option)
        user_answer = input("Enter your answer: ")
        if user_answer.upper() == data["answer"]:
            score += 1
        question_number += 1
    print(f"Your score is {score}/{question_number}")

quizgame()
