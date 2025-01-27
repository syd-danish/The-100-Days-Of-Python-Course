from data import question_data

class QuizBrain:
    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.answer_score=0
    def question_loop(self):
        for i in range(0, len(self.question_list)):
            ans = input(f"Q{self.question_number + 1}. {self.question_list[self.question_number]}\n")
            if ans.upper().lower().title().strip() == question_data[i]["answer"]:
                print("WELL DONE! Your Answer is correct!")
                self.answer_score += 1
            else:
                print("Your Answer is Incorrect!")
            self.question_number += 1
            print(f"Your Score is: {self.answer_score}/{self.question_number}")
