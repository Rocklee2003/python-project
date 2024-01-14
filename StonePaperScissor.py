from tkinter import *
from PIL import Image,ImageTk
from random import randint
# main window
root=Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")


#Picture
rock_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors_user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))

#insert picture
User_label=Label(root,image=scissor_img,bg="#9b59b6")
comp_label=Label(root,image=scissor_img_comp,bg="#9b59b6")

#placing the pic in fixed position
comp_label.grid(row=1,column=0)
User_label.grid(row=1,column=4)


#playerscore
playerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicator
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
comp_indicator.grid(row=0,column=1)
user_indicator.grid(row=0,column=3)

#messages
msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text']=x

#update user score
def updateUserScore():  
    score=int(playerScore["text"])  
    score+=1
    playerScore["text"]=str(score)

#update comp score
def updateCompScore():      
    score=int(computerScore["text"])  
    score+=1
    computerScore["text"]=str(score)

#check winner
def checkWin(player,computer):  
    if player == computer:
        updateMessage["Its a tie"]
    elif player == "rock":
        if computer == "paper":
            updateMessage("you loose")
            updateCompScore()
        else:   
            updateMessage("you win")
            updateUserScore()

    elif player == "paper":
        if computer == "scissor":
            updateMessage("you loose")
            updateCompScore()
        else:     
            updateMessage("you win")
            updateUserScore()  

    elif player == "scissor":
        if computer == "rock":
            updateMessage("you loose")
            updateCompScore()
        else:     
            updateMessage("you win")
            updateUserScore()                          

    else:
        pass
#Update choices
choices=["rock","paper","scissor"]
def updateChoice(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)     

#for user
    if x=="rock":
        User_label.configure(image=rock_img)
    elif x=="paper":
        User_label.configure(image=paper_img)    
    else:
        User_label.configure(image=scissor_img)

    checkWin(x,compChoice)

#buttons
rock = Button(root,width=20,height=4,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=4,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=4,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissor")).grid(row=2,column=3)

 
root.mainloop()

