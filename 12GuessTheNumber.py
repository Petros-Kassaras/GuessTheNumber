from tkinter import *
import os, sys
import random

def resource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


screen = Tk() #dimiourgia othonis
screen.title("Parathyro") #titlos
screen.geometry('300x400')#parathyro megethos
screen.configure(bg='#03fccf')
screen.resizable(width=False,height=False)

def Exit ():
    screen.destroy()

def Random ():
    ent.delete(0, END)
    global randnumber
    global tries
    choice = chce.get()
    ent.configure(state='normal')
    tries = 0
    lblt.configure(text="tries :" + str(tries))
    if choice == 1 :
        randnumber = random.randint(1, 50)
        print(randnumber)
    elif choice == 2 :
        randnumber = random.randint(1, 100)
        print(randnumber)
    elif choice == 3 :
        randnumber = random.randint(1, 200)
        print (randnumber)

def tyype (event):
    guess = ent.get()
    global tries
    global highscore
    if randnumber == int(guess) :
        lbli.configure(image=check)
        tries = tries + 1
        ent.configure(state='disable')
        lblt.configure(text="tries :" + str(tries))
        if highscore>tries :
           highscore = tries
           lblh.configure(text="highscore :" + str(highscore))
        tries=0
    elif randnumber>int(guess) :
        lbli.configure(image=up)
        tries = tries + 1
        lblt.configure(text="tries :" + str(tries))
    elif randnumber < int(guess):
        lbli.configure(image=down)
        tries = tries + 1
        lblt.configure(text="tries :"+ str(tries))


check = PhotoImage(file=resource_path("check.png"))
down = PhotoImage(file=resource_path("down.png"))
up = PhotoImage(file=resource_path("up.png"))
dice = PhotoImage(file=resource_path("dice.png"))

chce=IntVar()
chce.set(2)

tries = 0
highscore = 1000

tlbl = Label(screen,text="Guess The Number",font="Impact",bg='#03fccf',fg='#fc03f4')
rbe = Radiobutton(screen,text="Easy 1-50",value=1,bg='#03fccf',fg='#fc03f4',variable=chce)
rbm = Radiobutton(screen,text="Medium 1-100",value=2,bg='#03fccf',fg='#fc03f4',variable=chce)
rbh = Radiobutton(screen,text="Hard 1-200",value=3,bg='#03fccf',fg='#fc03f4',variable =chce)
lbl1 = Label(screen,text="In the game you will try to find a secret number.",bg='#03fccf',fg='#fc03f4')
lbl2 = Label(screen,text="Try to find the random number in the least possible tries.",bg='#03fccf',fg='#fc03f4')
lbli = Label(screen,image=dice,bg='#03fccf',fg='#fc03f4')
ent  = Entry(screen,state='readonly')
btnr = Button(screen,text="Randomize",bg='#03fccf',fg='#fc03f4',command = Random)
btne = Button(screen,text="Exit",bg='#03fccf',fg='#fc03f4',command =Exit)
lblt = Label(screen,text="tries : ",bg='#03fccf',fg='#fc03f4')
lblh = Label(screen,text="",bg='#03fccf',fg='#fc03f4')

screen.bind('<Return>',tyype)

tlbl.grid(row=0,column=0,columnspan=3)
rbe.grid(row=1,column=0)
rbm.grid(row=1,column=1)
rbh.grid(row=1,column=2)
lbl1.grid(row=2,column=0,columnspan=3)
lbl2.grid(row=3,column=0,columnspan=3)
lbli.grid(row=7,column=0,columnspan=3)
ent.grid(row=4,column=1)
btnr.grid(row=4,column=2)
btne.grid(row=5,column=2)
lblt.grid(row=5,column=1)
lblh.grid(row=6,column=1)

screen.mainloop() #kleinei programma