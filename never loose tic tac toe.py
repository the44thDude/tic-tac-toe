from tkinter import *
import base64
from PIL import Image, ImageTk
import random


with open('tic and tacs.jpg','wb') as wf:
    pic=base64.b64decode(b'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')
    wf.write(pic)

root=Tk()
root.title('never lose')
root.geometry('500x500')
root.resizable(False,False)

image=Image.open('tic and tacs.jpg')
size=(500,500)
image=image.resize(size)
dilly=ImageTk.PhotoImage(image)
background_label =Label( image=dilly)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

class info:
    b1state="normal"
    b2state="normal"
    b3state="normal"
    b4state="normal"
    b5state="normal"
    b6state="normal"
    b7state="normal"
    b8state="normal"
    b9state="normal"

    b1words='yes'
    b2words=''
    b3words='no'
    b4words=''
    b5words=''
    b6words=''
    b7words=''
    b8words=''
    b9words=''

    words="do you want to play a game?"

    turn=0
    center=False
    gamestart=False
    player=0
    computer=3
    board=[0,0,0,0,0,0,0,0,0]
    playermove=0

def move(x):
    info.board[x]=info.computer
    if x==0:
        info.b1state="disabled"
        if info.player==1:
            info.b1words="O"
        else:
            info.b1words="X"
    elif x==1:
        info.b2state="disabled"
        if info.player==1:
            info.b2words="O"
        else:
            info.b2words="X"
    elif x==2:
        info.b3state="disabled"
        if info.player==1:
            info.b3words="O"
        else:
            info.b3words="X"
    if x==3:
        info.b4state="disabled"
        if info.player==1:
            info.b4words="O"
        else:
            info.b4words="X"
    elif x==4:
        info.b5state="disabled"
        if info.player==1:
            info.b5words="O"
        else:
            info.b5words="X"
    elif x==5:
        info.b6state="disabled"
        if info.player==1:
            info.b6words="O"
        else:
            info.b6words="X"
    elif x==6:
        info.b7state="disabled"
        if info.player==1:
            info.b7words="O"
        else:
            info.b7words="X"
    elif x==7:
        info.b8state="disabled"
        if info.player==1:
            info.b8words="O"
        else:
            info.b8words="X"
    elif x==8:
        info.b9state="disabled"
        if info.player==1:
            info.b9words="O"
        else:
            info.b9words="X"

def boardread():
    result=[]
    if info.board[0]==info.player:
        result=[0]
    if info.board[1]==info.player:
        result=result+[1]
    if info.board[2]==info.player:
        result=result+[2]
    if info.board[3]==info.player:
        result=result+[3]
    if info.board[4]==info.player:
        result=result+[4]
    if info.board[5]==info.player:
        result=result+[5]
    if info.board[6]==info.player:
        result=result+[6]
    if info.board[7]==info.player:
        result=result+[7]
    if info.board[8]==info.player:
        result=result+[8]
    return result

def logic():
    if info.turn==1:
        if info.playermove==4:
            info.center=True
            move(0)
        else:
            info.center=False
            move(4)
    else:
        board=boardread()
        if info.center==True:
            if 0 in board and info.board[8]==0:
                move(8)
            elif 1 in board and info.board[7]==0:
                move(7)
            elif 2 in board and info.board[6]==0:
                move(6)
            elif 3 in board and info.board[5]==0:
                move(5)
            elif 5 in board and info.board[3]==0:
                move(3)
            elif 6 in board and info.board[2]==0:
                move(2)
            elif 7 in board and info.board[1]==0:
                move(1)
            elif 8 in board and info.board[0]==0:
                move(0)
            elif 0 in board and 1 in board and info.board[2]==0:
                move(2)
            elif 0 in board and 3 in board and info.board[6]==0:
                move(6)
            elif 2 in board and 1 in board and info.board[0]==0:
                move(0)
            elif 2 in board and 5 in board and info.board[8]==0:
                move(8)
            elif 8 in board and 5 in board and info.board[2]==0:
                move(2)
            elif 8 in board and 7 in board and info.board[6]==0:
                move(6)
            elif 6 in board and 7 in board and info.board[8]==0:
                move(8)
            elif 6 in board and 3 in board and info.board[3]==0:
                move(3)
            else:
                if info.board[3]==0:
                    move(3)
                if info.board[1]==0:
                    move(1)
        else:
            if 0 in board and 1 in board and info.board[2]==0:
                move(2)
            elif 0 in board and 3 in board and info.board[6]==0:
                move(6)
            elif 2 in board and 1 in board and info.board[0]==0:
                move(0)
            elif 2 in board and 5 in board and info.board[8]==0:
                move(8)
            elif 8 in board and 5 in board and info.board[2]==0:
                move(2)
            elif 8 in board and 7 in board and info.board[6]==0:
                move(6)
            elif 6 in board and 7 in board and info.board[8]==0:
                move(8)
            elif 6 in board and 3 in board and info.board[0]==0:
                move(0)
            elif 6 in board and 8 in board and info.board[7]==0:
                move(7)
            elif 6 in board and 0 in board and info.board[3]==0:
                move(3)
            elif 8 in board and 2 in board and info.board[5]==0:
                move(5)
            elif 0 in board and 2 in board and info.board[1]==0:
                move(1)
            elif 0 in board and info.board[1]==0:
                move(1)
            elif 0 in board and info.board[3]==0:
                move(3)
            elif 2 in board and info.board[1]==0:
                move(1)
            elif 2 in board and info.board[3]==0:
                move(3)
            elif 6 in board and info.board[3]==0:
                move(3)
            elif 6 in board and info.board[7]==0:
                move(7)
            elif 8 in board and info.board[7]==0:
                move(7)
            elif 8 in board and info.board[5]==0:
                move(5)
            else:
                if info.board[0]==0:
                    move(0)
                elif info.board[1]==0:
                    move(1)
                elif info.board[2]==0:
                    move(2)
                elif info.board[3]==0:
                    move(3)
                elif info.board[5]==0:
                    move(5)
                elif info.board[6]==0:
                    move(6)
                elif info.board[7]==0:
                    move(7)
                elif info.board[8]==0:
                    move(8)
def wincheck():
    computer=info.computer
    if info.board[0]==computer:
        if info.board[1]==computer and info.board[2]==computer:
            return True
        elif info.board[4]==computer and info.board[8]==computer:
            return True
        elif info.board[3]==computer and info.board[6]==computer:
            return True
    elif info.board[1]==computer and info.board[4]==computer and info.board[7]==computer:
        return True
    elif info.board[2]==computer:
        if info.board[4]==computer and info.board[6]==computer:
            return True
        elif info.board[5]==computer and info.board[8]==computer:
            return True
    elif info.board[3]==computer and info.board[4]==computer and info.board[5]==computer:
        return True
    elif info.board[6]==computer and info.board[7]==computer and info.board[8]==computer:
        return True
    else:
        return False
def restart():
    global background_label
    info.b1state="normal"
    info.b2state="normal"
    info.b3state="normal"
    info.b4state="normal"
    info.b5state="normal"
    info.b6state="normal"
    info.b7state="normal"
    info.b8state="normal"
    info.b9state="normal"

    info.b1words='yes'
    info.b2words=''
    info.b3words='no'
    info.b4words=''
    info.b5words=''
    info.b6words=''
    info.b7words=''
    info.b8words=''
    info.b9words=''

    info.words="you have lost.\n\ndo you want to play again?"

    info.turn=0
    info.center=False
    info.gamestart=False
    info.player=0
    info.computer=0
    info.board=[0,0,0,0,0,0,0,0,0]
    info.playermove=0
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    prescreenwrite()

def action(com):
    info.playermove=com
    global textbox
    textbox['text']=''
    if info.gamestart==False:
        if com==0:
            if info.player==0:
                info.words='choose "X" or "O"'
                info.b1words="X"
                info.b3words="O"
                info.b3state='normal'
                info.player=3
            else:
                info.b1words=''
                info.b3words=''
                info.words='you may go first'
                info.player=1
                info.computer=-1
                info.gamestart=True
        elif com==2:
            if info.player==0:
                info.words="then why did you boot me up?"
                info.b1words="sorry, I'll play"
                info.b3state="disabled"
            else:
                info.b1words=''
                info.b3words=''
                info.words='you may go first'
                info.player=-1
                info.computer=1
                info.gamestart=True
        if info.player==0 or info.player==3:
            prescreenwrite()
        else:
            screenwrite()
    else:
        info.turn=info.turn+1
        if com==0:
            info.board[0]=info.player
            info.b1state="disabled"
            if info.player==1:
                info.b1words="X"
            elif info.player==2:
                info.b1words="O"
        elif com==1:
            info.board[1]=info.player
            info.b2state="disabled"
            if info.player==1:
                info.b2words="X"
            elif info.player==2:
                info.b2words="O"
        elif com==2:
            info.board[2]=info.player
            info.b3state="disabled"
            if info.player==1:
                info.b3words="X"
            elif info.player==2:
                info.b3words="O"
        elif com==3:
            info.board[3]=info.player
            info.b4state="disabled"
            if info.player==1:
                info.b4words="X"
            elif info.player==2:
                info.b4words="O"
        elif com==4:
            info.board[4]=info.player
            info.b5state="disabled"
            if info.player==1:
                info.b5words="X"
            elif info.player==2:
                info.b5words="O"
        elif com==5:
            info.board[5]=info.player
            info.b6state="disabled"
            if info.player==1:
                info.b6words="X"
            elif info.player==2:
                info.b6words="O"
        elif com==6:
            info.board[6]=info.player
            info.b7state="disabled"
            if info.player==1:
                info.b7words="X"
            elif info.player==2:
                info.b7words="O"
        elif com==7:
            info.board[7]=info.player
            info.b8state="disabled"
            if info.player==1:
                info.b8words="X"
            elif info.player==2:
                info.b8words="O"
        elif com==8:
            info.board[8]=info.player
            info.b9state="disabled"
            if info.player==1:
                info.b9words="X"
            elif info.player==2:
                info.b9words="O"
        logic()
        win=wincheck()
        info.words=str(info.board)
        if win==True:
            restart()
        else:
            screenwrite()

def screenwrite():
    global textbox
    button_1 = Button(root,state=info.b1state, bg='#fff', text=info.b1words,width=10,height=5, padx=10, pady=10,command= lambda: action(0))
    button_2 = Button(root,state=info.b2state, bg='#fff', text=info.b2words,width=10,height=5, padx=10, pady=10,command= lambda: action(1))
    button_3 = Button(root,state=info.b3state, bg='#fff', text=info.b3words,width=10,height=5, padx=10, pady=10,command= lambda: action(2))
    button_4 = Button(root,state=info.b4state, bg='#fff', text=info.b4words,width=10,height=5, padx=10, pady=10,command= lambda: action(3))
    button_5 = Button(root,state=info.b5state, bg='#fff', text=info.b5words,width=10,height=5, padx=10, pady=10,command= lambda: action(4))
    button_6 = Button(root,state=info.b6state, bg='#fff', text=info.b6words,width=10,height=5, padx=10, pady=10,command= lambda: action(5))
    button_7 = Button(root,state=info.b7state, bg='#fff', text=info.b7words,width=10,height=5, padx=10, pady=10,command= lambda: action(6))
    button_8 = Button(root,state=info.b8state, bg='#fff', text=info.b8words,width=10,height=5, padx=10, pady=10,command= lambda: action(7))
    button_9 = Button(root,state=info.b9state, bg='#fff', text=info.b9words,width=10,height=5, padx=10, pady=10,command= lambda: action(8))
    button_1.grid(row=1,column=0,padx=10,pady=10)
    button_2.grid(row=1,column=1,padx=10,pady=10)
    button_3.grid(row=1,column=2,padx=10,pady=10)
    button_4.grid(row=2,column=0,padx=10,pady=10)
    button_5.grid(row=2,column=1,padx=10,pady=10)
    button_6.grid(row=2,column=2,padx=10,pady=10)
    button_7.grid(row=3,column=0,padx=10,pady=10)
    button_8.grid(row=3,column=1,padx=10,pady=10)
    button_9.grid(row=3,column=2,padx=10,pady=10)
    textbox=Label(root,bg='gray1',fg='green2', text=info.words, font=("system", 16))
    textbox.grid(row=0,column=0, columnspan=5, padx=10, pady=10)

def prescreenwrite():
    global textbox
    button_1 = Button(root,state=info.b1state, bg='#fff', text=info.b1words,width=10,height=5, padx=10, pady=10,command= lambda: action(0))
    button_2 = Button(root,state=info.b2state, bg='#fff', text=info.b2words,width=10,height=5, padx=10, pady=10,command= lambda: action(1))
    button_3 = Button(root,state=info.b3state, bg='#fff', text=info.b3words,width=10,height=5, padx=10, pady=10,command= lambda: action(2))
    button_4 = Button(root,state=info.b4state, bg='#fff', text=info.b4words,width=10,height=5, padx=10, pady=10,command= lambda: action(3))
    button_5 = Button(root,state=info.b5state, bg='#fff', text=info.b5words,width=10,height=5, padx=10, pady=10,command= lambda: action(4))
    button_6 = Button(root,state=info.b6state, bg='#fff', text=info.b6words,width=10,height=5, padx=10, pady=10,command= lambda: action(5))
    button_7 = Button(root,state=info.b7state, bg='#fff', text=info.b7words,width=10,height=5, padx=10, pady=10,command= lambda: action(6))
    button_8 = Button(root,state=info.b8state, bg='#fff', text=info.b8words,width=10,height=5, padx=10, pady=10,command= lambda: action(7))
    button_9 = Button(root,state=info.b9state, bg='#fff', text=info.b9words,width=10,height=5, padx=10, pady=10,command= lambda: action(8))
    button_1.grid(row=1,column=0,padx=10,pady=10)
    #button_2.grid(row=1,column=1,padx=10,pady=10)
    button_3.grid(row=1,column=2,padx=10,pady=10)
    #button_4.grid(row=2,column=0,padx=10,pady=10)
    #button_5.grid(row=2,column=1,padx=10,pady=10)
    #button_6.grid(row=2,column=2,padx=10,pady=10)
    #button_7.grid(row=3,column=0,padx=10,pady=10)
    #button_8.grid(row=3,column=1,padx=10,pady=10)
    #button_9.grid(row=3,column=2,padx=10,pady=10)
    textbox=Label(root,bg='gray1',fg='green2', text=info.words, font=("system", 16))
    textbox.grid(row=0,column=0, columnspan=5, padx=10, pady=10)


prescreenwrite()

root.mainloop()
