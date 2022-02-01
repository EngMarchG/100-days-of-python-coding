class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {current_question.text} True/False?").lower()
        correct_answer = current_question.answer
        self.check_answer(choice, correct_answer)
        # if choice == current_question.answer.lower():
        #     print("Correct!")
        # else:
        #     print("You are wrong")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def final_score(self):
        print(f"You've completed the quiz. Your final score is {self.score}/{self.question_number}")