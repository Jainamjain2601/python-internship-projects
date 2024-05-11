print("Welcome to my quiz game!!!")

question_data = [
    {"question": "Which of the following is the correct extension of the Python file?", "options": ["A.python", "B.pl", "C.py", "D..p"], "correct_answer": "C"},
    {"question": "Which type of Programming does Python support?", "options": ["A. object-oriented programming", "B. structured programming", "C. functional programming", "D. all of the mentioned"], "correct_answer": "D"},
    {"question": "Is Python code compiled or interpreted?", "options": ["A. Python code is both compiled and interpreted", "B. Python code is neither compiled nor interpreted", "C. Python code is only compiled", "D. Python code is only interpreted"], "correct_answer": "A"},
    {"question": "All keywords in Python are in _________", "options": ["A. Capitalized", "B. lower case", "C. UPPER CASE", "D. None of the mentioned"], "correct_answer": "B"},
    {"question": "Which of the following is used to define a block of code in Python language?", "options": ["A. Indentation", "B. Key", "C. Brackets", "D. All of the mentioned"], "correct_answer": "A"}
]

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def display_question(self):
        current_question = self.questions[self.question_number]
        print("********************************")
        print(current_question["question"])
        for option in current_question["options"]:
            print(option)

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.question_number]["correct_answer"]
        if user_answer.upper() == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")

    def next_question(self):
        self.question_number += 1
        if self.question_number < len(self.questions):
            self.display_question()
            user_answer = input("Enter your answer (A/B/C/D): ")
            self.check_answer(user_answer)
        else:
            print("You've completed the quiz!")
            print(f"Your final score was: {self.score}/{self.question_number}")

# Quiz instance
quiz = Quiz(question_data)

# Start the quiz
quiz.display_question()
user_answer = input("Enter your answer (A/B/C/D): ")
quiz.check_answer(user_answer)

while quiz.question_number < len(quiz.questions):
    quiz.next_question()
