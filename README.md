# masai-project-iit-mandi
This Python-based Quiz Application is a thoughtfully designed, text-driven program that facilitates an interactive quiz experience directly from the command line. It leverages external text files to dynamically load questions, validate user responses, track scores, and store results persistently. The modular approach, clean separation of concerns, and reliance on reusable functions make it both scalable and easy to maintain. Below is a detailed walkthrough of each aspect of the program.
# Purpose of the Application
The application serves as an educational or entertainment tool where users can test their knowledge on various topics via a series of multiple-choice questions. It aims to:

-Provide a seamless and interactive user experience.

-Support dynamic updates to the quiz content without requiring changes to the source code.

-Track and store user performance for reference or analysis later.
# Program Workflow
1) Initialization: The program begins with a welcome message.

2) User Input: The player enters their name.

3) Loading Data: Questions and answers are dynamically loaded from questions.txt and answers.txt.

4) Quiz Execution: Each question is displayed one at a time, along with four options (A, B, C, D).

5) User Interaction: The user selects an answer, and the application validates their choice.

6) Score Tracking: Correct answers are counted to calculate the final score.

7) Result Display: The final score is displayed on the screen.

8) Score Recording: The player’s name and score are appended to score.txt.

9) Completion: A closing message is displayed, and the program gracefully exits.
