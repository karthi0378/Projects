# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct 
# keep track of the score
# tell the user their score

import random

questions = {
    "what is the capital of bengal" : "kolkata",
    "what is the capital of punjab" : "chandigarh",
    "what is the capital of maharashtra" : "mumbai",
    "what is the capital of rajasthan" : "jaipur",
    "what is the capital of india" : "new delhi",
    "what is the capital of bihar" : "patna"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx+1}. {question}")
        user_answer = input("your answer: ").lower().strip()
        correct_answer = questions[question].lower()

        if user_answer == correct_answer:
            print(f"correct!\n")
            score += 1
        else:
            print(f"wrong. the correct answer is {correct_answer}.\n")

    print(f"game over! you final score is: {score}/{total_questions}")

python_trivia_game()
