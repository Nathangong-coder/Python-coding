from tkinter import ANCHOR, NW, PhotoImage, Tk, Canvas
import time
from os import path
# Question 1: what happens if you change these?
#if you change timer_milliseconds, then the master_timer function update time will change
#it is measured in milliseconds
TIMER_MILLISECONDS = 20
#if you change canvas_width, then your whole window increases in length,
#the ball will always bounce in the whole window
# (you cannot resize window)
CANVAS_WIDTH=400
#same as canvas width, but with canvas height
CANVAS_HEIGHT=600
#if you change ball size, it changes the size of the ball in pixels
BALL_SIZE=30
# Question 2: what happens if you change these?
#if you change ball_move_x, then it will change the speed of movement
#x is movement of horizontal, by pixels, affecting speed
ball_move_x=3
#y is movement of vertical, by pixels, affecting speed
ball_move_y=2
#the distance it moves/how fast the dino moves
# if changed, changes the speed of movement
dino_move = 5
# Question 3: What does this function do? 
# You might not fully  understand it, but can you get the gist?
#This function is called when dino touches ball
#Will return "true" if dino touches ball
#the ball_coords doesn't change, so doesn't move
def dino_catches_ball():
    ball_coords = canvas.coords(ball)
    overlap_result = canvas.find_overlapping(ball_coords[0], ball_coords[1], 
                                            ball_coords[2], ball_coords[3])
#variable says that overlap_variable happesn when it is in the ball coords
    if dino in overlap_result:
        return True
    else:
        return False
# Question 4: What does this function do? 
# You might not fully  understand it, but can you get the gist?
#is the function about how dino moves
#brings the variable, the parameter of the event
def move_dino(event):
    key_symbol = event.keysym
    #uses the variable with keysym
    #is the arrow key's symbolic name in tkinter
    print(key_symbol, "was pressed")
    #print what key was pressed
    if key_symbol == "Left":
        #says when key symbol left is pressed
        #then it moves left by changing dino's x location and moves left (- x)
        #doesn't impact y
        canvas.move(dino, -dino_move,0)
    elif key_symbol == "Right":
        #when key symbol right is pressed
        #doesn't impact y, but moves right by adding to dino's x location (+ x)
        canvas.move(dino, dino_move,0)
    else:
        #if prints up or down key, or any other key symbol
        #when up or down, says idk and doesn't change location
        print("don't know that one")
   
# Question 5: What does this function do? 
# You might not fully  understand it, but can you get the gist?
#describes how the ball moves
def draw_ball():
    #pulls in how the ball moves
    global ball_move_x, ball_move_y
    #if the dino_catches_ball is called, then prints "caught me"
    #the ball will stop moving
    if dino_catches_ball():
        print("caught me")
    #if else, then the ball will keep moving
    else: 
        canvas.move(ball, ball_move_x, ball_move_y)
    #describe the coordinates of the ball
    pos = canvas.coords(ball)
    #this is the top left position, describe when it is top left corner (pos 0)
    top_left_x = pos[0]
    #this is top right position, aka top right corner (pos 1)
    top_left_y = pos[1]
    #this is bottom right position, aka bottom right corner (pos 2)
    bottom_right_x = pos[2]
    #this is bottom 
    bottom_right_y = pos[3]
    if bottom_right_y >= CANVAS_HEIGHT: 
        #if the ball, bottom right, is just above canvas
        #then change direction of y (from going down to up)
        ball_move_y = - ball_move_y 
    elif top_left_y <= 0:
        #when it is in top, then ball moves opposite
        ball_move_y = - ball_move_y
    elif bottom_right_x >= CANVAS_WIDTH:
        #when it goes out of the screen, then change direction of ball
        ball_move_x = - ball_move_x
    elif top_left_x <= 0:
        #when it passes the left side, then also change x
        ball_move_x = -ball_move_x
# Question 5: What does this function do? 
# You might not fully  understand it, but can you get the gist?
#the definition of master_timer function
def master_timer():
    #will call all these functions, including making the function
    #gets updated with timer of timer_milliseconds
    draw_ball()
    root.update_idletasks()
    #calls update_function, to update position of ball
    root.update()
    root.after(TIMER_MILLISECONDS, master_timer)
#call the actual window and makes it
root = Tk()
#make the title "bouncing ball"
root.title("Bouncing Ball")
# Question 6: What happens if you remove these?
#you can resize the window if you remove this
root.resizable(0,0)
root.wm_attributes("-topmost",1)
# Note: A canvas is a new 
#describe canvas, which is the canvas behind the window
#is where the ball can go inside
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, 
                    bg='black')
#need to pack everything
canvas.pack()
# Question 7: What happens if you change the parameters here?
# Can you swap it out for create_line or create_polygon?
#describes the ball (oval with 0,0 change)
#describe how big it is, using the variable "ball_size", with red fill

ball = canvas.create_oval(0,0,BALL_SIZE,BALL_SIZE, fill="red")
# Question 8: What part of this is new or different?
#changes some names, but still makes image
address_for_image = path.dirname(__file__) + "\\dino.png"
dino_img = PhotoImage(file=address_for_image)
#resizes image, that is new
dino_img_resized = dino_img.subsample(4,4)
#makes variables to show how big the dino is in pixels
DINO_HEIGHT = dino_img_resized.height()
DINO_WIDTH = dino_img_resized.width()
# Question 9: What part of this is new or different?
#makes a new dino image, that spawns the dino
dino  = canvas.create_image(0,0, image=dino_img_resized, anchor=NW)
#describe how the canvas will move depending on how the dino moves
canvas.move(dino,(CANVAS_WIDTH-DINO_WIDTH)/2, (CANVAS_HEIGHT-DINO_HEIGHT)/2)
# Question 10: This allows keyboard input to work. Can you guess what it does?
#when key is pressed, it moves like the canvas, which moves the dino
canvas.bind_all("<KeyPress-Left>", move_dino)
canvas.bind_all("<KeyPress-Right>", move_dino)
canvas.bind_all("<KeyPress-Up>", move_dino)
canvas.bind_all("<KeyPress-Down>", move_dino)
#call the master_timer function
master_timer()
#makes the window
root.mainloop()