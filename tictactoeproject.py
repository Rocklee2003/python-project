#1. make GUI part

from tkinter import *;

root = Tk() 
#here an object is created of the class inside the package tkinter
root.geometry("500x500")
#geometry is a function inside the class TK() of the tkinterr library 
root.title("Tic tac Toe")

#Now here we are going to make the 9 grid , so we will use button for it 
#consider frame 1 as a base layer on which another layer will display the game
frame1 = Frame(root)#function and root is provided as a parameter
frame1.pack()
'''The frame1.pack() line is used to make the frame (frame1) visible within the main 
window. In Tkinter, the pack() method is a geometry manager that organizes widgets in 
blocks before placing them in the parent widget.
So, frame1.pack() is responsible for displaying the frame and making it visible within 
the main window of the Tic Tac Toe GUI.'''
titleLable = Label(frame1,text="Tic Tac Toe",font=("Arial",30),bg="yellow")
titleLable.pack()

#2nd frame on frame 1 on which we will display buttons in grid 
frame2 = Frame(root)
frame2.pack()

#now we are making the dictionary to store the values on the each button in the form of key value pairs
#if the values of the keys are similar then we will declare as a winner
board = { 1:" ",2:" ",3:" ",
          4:" ",5:" ",6:" ",
          7:" ",8:" ",9:" " }

turn="x"  #made a global variable .i.e whose value we cant change in functions

def checkForWin(player):
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    
    #all cols
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    
    #check in sliding line
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True
#Now we have to display the x and o so we use this function.GOING TO USE BIND METHOD 

def checkforDraw():
    for i in board.keys():
        if board[i] == " ":#check the empty value if yes then return is false
            return False
        
    return True #if position is not there then its true   

def play(event): 
    global turn
    button = event.widget

#now we will make a logic to put the values into the dictionary ;i.e values to the key 
    buttonText=str(button)  #here we type cast the button type into the string as to access its last elements.    
    clicked=buttonText[-1]  # here above we used indexing method where -1 is uesd to show the last element of the string .In the string or list we can access the last element by using the -ve value to access the elements from the last
    print(clicked)
    if clicked == "n":
        clicked = 1
    else :
        clicked = int(clicked)

    if button["text"] == " ":   #will help to only print the value once and avoid the overwrite of the value. here if the text is empty then only user will be able to give it a vlaue
        if turn == "x" :
            button["text"] = "X" 
            board[clicked]= turn
            if checkForWin(turn):
                winningLabel = Label(frame2 ,text=f"{turn} wins the game",bg="green",font=("Arial",20))
                winningLabel.grid(row=3,column=0,columnspan=3)
            turn="o"
            
        else :
            button["text"] = "O"
            board[clicked]= turn
            if checkForWin(turn):
                winningLabel = Label(frame2 ,text=f"{turn} wins the game" , bg="green" ,font=("Arial",20))
                winningLabel.grid(row=3,column=0,columnspan=3)
            turn="x"

        if checkforDraw():
            DrawLabel = Label(frame2 ,text=f"GAME DRAW!!" , bg="green" ,font=("Arial",20))
            DrawLabel.grid(row=3,column=0,columnspan=3)

        print(board)
        if checkForWin(turn):
            print(turn,"win the game")
            print("game over")
#tic tac toe game    
#FIRST ROW AT INDEX 0
            
button1 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)   #text is empty to show x or o in the game;look=> Arial is type of letter and 30 is a size of a letter   
button1.grid(row=0 , column=0)  #shows the direction
button1.bind("<Button-1>",play)

button2 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button2.grid(row=0 , column=1)#shows the direction
button2.bind("<Button-1>",play)

button3 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button3.grid(row=0 , column=2)#shows the direction
button3.bind("<Button-1>",play)

#SECOND ROW AT INDEX 1
button4 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button4.grid(row=1 , column=0)#shows the direction
button4.bind("<Button-1>",play)

button5 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button5.grid(row=1 , column=1)#shows the direction
button5.bind("<Button-1>",play)

button6 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button6.grid(row=1 , column=2)#shows the direction
button6.bind("<Button-1>",play)

#THIRD ROW AT INDEX 2
button7 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button7.grid(row=2 , column=0)#shows the direction
button7.bind("<Button-1>",play)

button8 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button8.grid(row=2 , column=1)#shows the direction
button8.bind("<Button-1>",play)

button9 = Button(frame2,text=" ",width="4" , height="2", font=("Arial",30),bg="skyblue" ,relief=RAISED,borderwidth=5)#text is empty to show x or o in the game
button9.grid(row=2 , column=2)#shows the direction
button9.bind("<Button-1>",play)
root.mainloop()
#this is the main loop!!! without this the window for the game will not appear!!


''' 
Main Logic Explanation:

turn = "x": This initializes a global variable named turn with the value "x". The purpose of this variable is to keep track of whose turn it is in a game (either "X" or "O").

def play(event):: This line defines a function named play that takes an event object as a parameter. This function is intended to be called when a button is clicked.

global turn: This line declares that the function will use the global variable turn instead of creating a local variable with the same name.

button = event.widget: This line retrieves the widget (in this case, a button) on which the event occurred. The event.widget attribute provides access to the widget associated with the event.

The function then checks the value of turn:

If turn is "x", it sets the text of the button to "X" and updates turn to "o" for the next turn.
If turn is not "x" (i.e., it is "o"), it sets the text of the button to "O" and updates turn to "x" for the next turn.
'''