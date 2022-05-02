import tkinter as tk
from tkinter.constants import COMMAND
import time
import random
from Danish.HouseKeeping import *



"""
n = 3
def func(x): 
    global n #required to modify n, but not to fetch its value
    n += 1
    return n + x

print('>>>',func(4),n)

L = [0,1,2]
def Func(A):
    L.append(A) #Here it modifies even without global
    return L + [A]

print('>>>',Func(4),L)

1/0
"""


window = tk.Tk()

frame_a = tk.Frame()


totalQues = tk.Label(master=frame_a, text="Input total number of questions")
totalQues.pack()
totalQuesInput = tk.Entry()
totalQuesInput.pack()
label_a = tk.Label(master=frame_a, text="Make a choice")
label_a.pack()
button_a1 = tk.Button(master=frame_a, text="Quick Play")
button_a2 = tk.Button(master=frame_a, text="Track your progress")
button_a1.pack()
button_a2.pack()
finished_label = tk.Label(master=frame_a)
finished_label.pack()
frame_a.pack()

total = 0
NumberOfQuestions = 0

question = None
scoreLabel = None
correctAn = None
entry = None
currentFrame_game = None

NumberOfQuestions = 0
MaxPossibleScore = 0
attempt = 0
maxAttempt = 2

def newGame(timerBoolean):
    global question
    global scoreLabel
    global correctAn
    global answer
    global score
    global entry
    global currentFrame_game
    global total

    total = int(totalQuesInput.get())

    frame_game = tk.Frame()
    label_game = tk.Label(master=frame_game, text="QuickPlay")
    label_game.pack()
    currentFrame_game = frame_game

    if timerBoolean == True:
        timer_game = tk.Label(master=frame_game, text=str(time.asctime()))
        timer_game.pack()

    question = tk.Label(master=frame_game, text='')
    question.pack()
    scoreLabel= tk.Label(master=frame_game, text='0')
    scoreLabel.pack()
    score = 0
    correctAn = tk.Label(master=frame_game, text='')
    correctAn.pack()

    answer = nextQues()
    
    entry = tk.Entry(master=frame_game)
    entry.pack()

    # Bind keypress event to submit()
    window.bind('<Key>', submit)

    quit_label = tk.Button(master=frame_game, text="Quit", command=frame_game.destroy)
    quit_label.pack()
    frame_game.pack()



def nextQues ():
    global NumberOfQuestions

    if NumberOfQuestions == total:
        finished_label['text']='Finished!'
        NumberOfQuestions = 0
        endGame()

    NumberOfQuestions += 1

    global MaxPossibleScore
    MaxPossibleScore += maxAttempt
    k = random.randint(0,N-1) #random number between 0 and 331 of all the verb stem keys
    flashcard = flashcardsInf[k] #flashcard = kth infinitiv in our list of keys
                            # DICT[flashcard] = corresponding value [eng, pres, preterit, perfect]

    #DICT['gøre'] = ['go','gør','gjorde','har gjort']
    choice = random.randint(0,3) # eg we get 2
    tense = tenses[choice] #that corresponds to 'past'
    question['text'] = 'what is the ' +  tense + ' of '+ flashcard + '?'+ (tense=='present perfect')*' har / er...'
    return DICT[flashcard][choice]

    
    # in the case of present perfect, we only ask for the verb per se, the auxiliary verb being conditionally given.
    # NOTE : in case the verb ends with pronoun (sig) or preposition (ud...),  this does not work yet, because we fetched 'sig' and 'ud' as the verb when reading through the csv




def submit(event): #triggered whenever a key is pressed.
    global answer
    global attempt
    global score
    global NumberOfQuestions

    correctAn['text'] = '' #correct answer to the previous question erased as soon as user presses any key
    correctAn['bg'] = 'black'
    if event.keysym == 'Return': # the main effect of the function submit only happens if the pressed key is the Enter key 
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


def endGame():
    currentFrame_game.destroy()

def openTimedGame():
    if currentFrame_game != None:
        currentFrame_game.destroy()
    newGame(True)

def openQuickGame():
    if currentFrame_game != None:
        currentFrame_game.destroy()
    newGame(False)

button_a1['command']=openQuickGame
button_a2['command']=openTimedGame

window.mainloop()