from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in range (0,len(question_data)):
    question_bank.append(Question(question=question_data[i]["text"],answer=question_data[i]["answer"]))
qb=QuizBrain(question_list=question_bank)
qb.question_loop()
