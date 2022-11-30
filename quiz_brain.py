from cv2 import correctMatches


class Quizbrain :
    def __init__(self ,q_list) -> None:
        self.question_number = 0 
        self.question_list = q_list
        self.score = 0 

    def still_has_question (self) :
        return  self.question_number < len (self.question_list) 
                 

    def nextquestion (self) :
        currquestion = self.question_list[self.question_number]
        self.question_number += 1 
        uinput = input (f"Q{self.question_number} : {currquestion.text} (True/False) ")   
        self.checkanswer (uinput , currquestion.answer)    

    def checkanswer (self , uinput , correctanswer):
        if uinput == correctanswer :
            self.score += 1 
            print ("You got it right ")
        else :
            print ("You got it right")
        print (f"The correct answer is {correctanswer}")
        print (f"Your current score is {self.score}/{self.question_number}")
        print ("\n")


        
