import os

class QuizQuestion:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices

    def show(self):
        print(self.text)
        for choice in self.choices:
            print(choice)

def read_file_lines(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except IOError as e:
        print(f"Failed to read file {filepath}: {e}")
        return []

def load_quiz_content():
    questions_data = read_file_lines('questions.txt')
    answers_data = read_file_lines('answers.txt')
    
    questions = []
    for i in range(0, len(questions_data), 5):
        if i + 4 < len(questions_data):
            question_text = questions_data[i]
            choices = questions_data[i+1:i+5]
            questions.append(QuizQuestion(question_text, choices))
    
    return questions, answers_data

def record_score(player_name, player_score, total):
    try:
        with open('score.txt', 'a') as file:
            file.write(f"{player_name}: {player_score}/{total}\n")
    except IOError as e:
        print(f"Failed to save score: {e}")

def execute_quiz():
    player_name = input("Enter your name: ").strip()
    questions, answers = load_quiz_content()
    
    if not questions or not answers or len(questions) != len(answers):
        print("Error: Inconsistent or missing quiz data.")
        return
    
    score = 0
    total_questions = len(questions)
    
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question.text}")
        question.show()
        
        while True:
            user_input = input("Choose an option (A/B/C/D): ").strip().upper()
            if user_input in ['A', 'B', 'C', 'D']:
                break
            print("Invalid choice. Please enter A, B, C, or D.")
        
        if user_input == answers[index]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {answers[index]}.")
    
    print(f"\nYour final score: {score}/{total_questions}")
    record_score(player_name, score, total_questions)

def start_quiz():
    print("Welcome to the Ultimate Quiz Challenge!")
    try:
        execute_quiz()
    except KeyboardInterrupt:
        print("\nQuiz terminated early. Goodbye!")
    print("Thank you for participating!")

if __name__ == '__main__':
    start_quiz()
