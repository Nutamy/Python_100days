from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for question in question_data["results"]:
    questions.append(Question(question["question"], question["correct_answer"]))

# for q in range(len(questions)):
#     print(questions[q].text, questions[q].answer)
quiz = QuizBrain(questions)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")

