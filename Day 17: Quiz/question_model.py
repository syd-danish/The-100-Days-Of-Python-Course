class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
    def __str__(self):
        return f"{self.question} (True/False)\n"
