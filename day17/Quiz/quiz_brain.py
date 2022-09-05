class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)-1

    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Right!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Your score is: {self.score}/{self.question_number+1}\n")


