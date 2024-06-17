from table import question_data

class Question:
    def __init__(self, text, answer):

        self.text = text
        self.answer = answer
        
class QuizBrain():
    def __init__(self, question_list):
        
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def more(self):
        if self.question_number < len(self.question_list):
            return True
    
    def check(self,an):
        n = self.question_list[self.question_number]
        if an.lower() == (n.answer).lower() :
            self.score += 1
            print("Good Answer")
        else:
            print("wrong answer")
        print(n.answer)
    
    

    def next_question(self):
        current_q = self.question_list[self.question_number]
        an = input(current_q.text)
        
        self.check(an)
        self.question_number += 1
        
        print(f"your score is {self.score} out of {self.question_number}")





l = []
for i in question_data:
   
    for key, value in i.items():
        if key == "question":
            a = value

        elif key == "correct_answer":
            b = value
    l.append(Question(a,b))


a =QuizBrain(l)
while a.more():
    a.next_question()
print("great")
print(f"final is {a.score} out of {a.question_number}")