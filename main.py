from question_model import Question 
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data :
    qtext = question['text']
    qanswer = question ['answer']
    newquestion = Question (text=qtext , answer=qanswer)
    question_bank.append (newquestion)

quiz = Quizbrain (question_bank)

while quiz.still_has_question () :
    quiz.nextquestion ()
    
print ("Your Final score is : ") 
print (f"Your final score was :  {quiz.score} / {quiz.question_number}")       





