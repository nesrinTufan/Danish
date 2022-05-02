import tkinter as tk
import random
import Danish.HouseKeeping as HouseKeeping
from Danish.HouseKeeping import *


with OpenFile('report_card.csv', 'a') as r:
    r.write('greetings, universe\n')

NumberOfQuestions = 0
MaxPossibleScore = 0
attempt = 0
maxAttempt = 2


window = tk.Tk()
window.configure(bg='black')
greeting = tk.Label(text='Allo Allo velkom to your danish class')
greeting.pack()
question = tk.Label(text='')
question.pack()
scoreLabel= tk.Label(text='0')
scoreLabel.pack()
score = 0
correctAn = tk.Label(text='')
correctAn.pack()


entry = tk.Entry()
entry.pack()



def nextQues ():
    global NumberOfQuestions
    NumberOfQuestions += 1
    global MaxPossibleScore
    MaxPossibleScore += maxAttempt
    k = random.randint(0,N-1) #random number between 0 and 331
    flashcard = flashcardsInf[k] #flashcard = kth infinitiv in our list of keys
                              # DICT[flashcard] = corresponding value [eng, pres, preterit, perfect]

    #DICT['gøre'] = ['go','gør','gjorde','har gjort']
    choice = random.randint(0,3) # eg we get 2
    tense = tenses[choice] #that corresponds to 'past'
    question['text'] = 'what is the ' +  tense + ' of '+ flashcard + '?'+ (tense=='present perfect')*' har / er...'
    return DICT[flashcard][choice]

    
    # in the case of present perfect, we only ask for the verb per se, the auxiliary verb being conditionally given.
    # NOTE : in case the verb ends with pronoun (sig) or preposition (ud...),  this does not work yet, because I fetched 'sig' and 'ud' as the verb when reading through the csv


answer = nextQues()

def submit(event): #triggered whenever a key is pressed.
    global answer
    global attempt
    global score
    correctAn['text'] = '' #correct answer to the previous question erased as soon as user presses any key
    correctAn['bg'] = 'black'
    if event.keysym == 'Return': # the main effect of our function submit only happens if the pressed key is the Enter key
        print(attempt)    
        if entry.get() == answer:
            answer = nextQues()         
            score += maxAttempt - attempt + 1
            scoreLabel['text']=str(score)
            scoreLabel['bg']='grey'
            attempt = 0

        elif attempt < maxAttempt:
            attempt += 1
            scoreLabel['bg']='red'

        else: #case where user is still wrong and max number of attempts is reached
            correctAn['text'] = answer
            correctAn['bg']= 'green'
            answer = nextQues()
            attempt = 0
            scoreLabel['bg']='grey'
            

        entry.delete(0, tk.END)


# Bind keypress event to submit()
window.bind('<Key>', submit)


window.mainloop()

print('you scored ',score, ' out of ', MaxPossibleScore)

#menu
#Number of questions
#Timer
#maximum score

#Report card - derives from map of most incorrect value based on flashcardInf