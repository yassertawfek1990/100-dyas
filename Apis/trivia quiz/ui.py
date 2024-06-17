from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):

        self.quiz_q = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(text=f"Score: 0",fg="white",background=THEME_COLOR)
        self.score_label.grid(column=1,row = 0)
        self.canv = Canvas(width=300,height=250)
        self.question_text = self.canv.create_text(150,125,text="whatever ", width=280 , fill= THEME_COLOR,font=("Arial",20,"italic"))
        self.canv.grid(column=0,row=1,columnspan=2,pady= 50)

        yes_photo =PhotoImage(file="trivia quiz/images/true.png")
        self.yes_but = Button(image=yes_photo,highlightthickness=0,command=self.right)
        self.yes_but.grid(column=0,row=3)
        no_photo = PhotoImage(file="trivia quiz/images/false.png")
        self.no_but = Button(image=no_photo,highlightthickness=0,command=self.wrong)
        self.no_but.grid(column=1,row=3)
        
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canv.config(background="white")
        if self.quiz_q.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_q.score}")
            q_text = self.quiz_q.next_question()
            self.canv.itemconfig(self.question_text,text = q_text)
        else:
            self.canv.itemconfig(self.question_text, text="You have reached the end")
            self.yes_but.config(state="disabled")
            self.no_but.config(state="disabled")

    def wrong(self):
        self.feedback(self.quiz_q.check_answer("false"))
        
        # self.score = self.quiz_q.score
    
    def right(self):
        self.feedback(self.quiz_q.check_answer("true"))
        
        # self.score = self.quiz_q.score

    def feedback(self, is_true):
        if is_true:
            self.canv.config(background="green")
        else:
            self.canv.config(background="red")
        
        self.window.after(1000, self.get_next_question)