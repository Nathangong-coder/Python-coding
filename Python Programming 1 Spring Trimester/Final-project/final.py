#Nathan Gong
#June 2022
#Final Project
#Programmming 1 
#Ms. Lewellen


#importing the libraries
from tkinter import *
import time
from os import path
from tkinter.ttk import Progressbar
import random

#stating some variables
timer_milliseconds=20 #variable describing how long the timer will be in milliseconds, before timer function is re-called
end_milliseconds=1690 #variable describing how long it takes before the end function to be called (see line 149)
canvas_width=600 #variable storing how long the canvas is
canvas_height=615 #variable storing how high the canvas is
player_speed_vertical=45 #variable storing how fast the player is per key press (vertically)
player_speed_horizontal= 40 #variable storing how fast the player is per key press (horizontally)
progress_counter=0 #variable storing how much progress the player has
welcome_text="Welcome to Crossy Road! Try to cross the lanes!" #a variable storing a welcome message
lanes_crossed_text="0"
loss_text="Haha, you lost!" #a variable storing a loss message
win_text="Congrats,you won!"
lane_crossed_counter=0 #counter counts how many lanes are crossed
list_of_speeds=[] #an empty list (for now) of all the speeds
list_of_cars=[] #an empty list (for now) of all the 36 cars 
list_for_lanes=[]#an empty list (for now) the y value of all 12 lanes

#creating the window
window=Tk() #actually making the window
window.title("Crossy Road Game") #changing the window title to "cross road game"
window.resizable(0,0) #making so the window can't zoom in and be resized
window.wm_attributes("-topmost",1) #making it so the window cannot be resized (with the arrows dragging the window sides)


#creating the title/description of site
descript_of_site=Label(window, text=welcome_text)#this is a variable storing the welcome text data belonging to this window
descript_of_site.grid(row=0, column=0, columnspan=1) #this actually packs the description on a grid on the window


#creating a progress bar, showing how far you've gone
progress_meter=Progressbar(window,length=200, mode="determinate", orient=HORIZONTAL, max=12) 
#this is a variable storing the progress bar data, that is 80 pixels in length, and has 12 "bars", and belongs to this window
progress_meter.grid(row=0,column=1,columnspan=1) #this actually packs the progress bar on a grid on the window
progress_meter["value"]=progress_counter



#creating the canvas
canvas = Canvas(window, width=canvas_width, height=canvas_height, 
                    bg='black') #this creates a variable storing the canvas, which has its width and height determined by other variables
canvas.grid(row=1,column=0,columnspan=2) #actually creates the canvas on the window in a grid

#creating all the images
#creating road background
address_for_road_img = path.dirname(__file__) + "\\Roads.PNG" #makes a variable for the address for the road img "Roads.PNG"
road_img=PhotoImage(file=address_for_road_img) #having a new variable saying the variable for the address for the road img is a PhotoImage
road_img_resized=road_img.subsample(2,3) #resizing it by 2x smaller for x, 3 times smaller for y
canvas.create_image(0,0, image=road_img_resized, anchor=NW) #actually puts that on the canvas, since its first its the bottom layer
#the anchor shows which direction its oriented in, which is NW
#0,0, stating where to put it on the canvas, which is no movement from the origin (top of canvas)

#1st car
address_for_car0_img=path.dirname(__file__)+"\\Car 1.png" #makes a variable for the address for hte 
car_0_img=PhotoImage(file=address_for_car0_img) #similar to road_img
car_0_img_resized=car_0_img.subsample(14,14) #resizing it like road_img_resized
car0_height=car_0_img_resized.height() #has a variable stating how high the car is
car0_width=car_0_img_resized.width() #has a varialbe stating how long the car is

#2nd car (all code is similar to car 1, so I'm not adding a description)
address_for_car1_img=path.dirname(__file__)+"\\Car 2.png" 
car_1_img=PhotoImage(file=address_for_car1_img)
car_1_img_resized=car_1_img.subsample(9,9)
car1_height=car_1_img_resized.height()
car1_width=car_1_img_resized.width()

#3rd car (all code is similar to car 1 & 2, so I'm not adding a description)
address_for_car2_img=path.dirname(__file__)+"\\Car 3.png"
car_2_img=PhotoImage(file=address_for_car1_img)
car_2_img_resized=car_2_img.subsample(9,9)
car2_height=car_2_img_resized.height()
car2_width=car_2_img_resized.width()

#making the controlled car/character inside the window
address_for_player_img=path.dirname(__file__)+"\\Control car 1.png"
player_car_img=PhotoImage(file=address_for_player_img)
player_car_img_resized=player_car_img.subsample(35,35)
playercar_height=player_car_img_resized.height()
playercar_width=player_car_img_resized.width()
#the line below creates the player's car on the canvas, at 300, 575 (lower than 0,0) with the anchor facing north (since the car faces north)
player_car=canvas.create_image(300,575, image=player_car_img_resized, anchor=N)
#the line below states the coords for the car, which is used later in the collision function
player_coords=canvas.coords(player_car)

#lose image, for when the player loses
address_for_loss_img=path.dirname(__file__)+"\\Lose Image.PNG"
loss_img=PhotoImage(file=address_for_loss_img)

#win image, for when the player wins
address_for_win_img=path.dirname(__file__)+"\\Win Image.PNG"
win_img=PhotoImage(file=address_for_win_img)
#statements for the functions
for num_cars_in_each_lane in range(3): #this for statement has a variable, number of cars, which automatically increase by 1 after running everything once
    #this happens 3 times, where the number of cars variable increases by 1
    for i in range(4): #draws/spawns the cars in the canvas, 4 times in "i"
        #added car number 1 into the list
        #the x value of each car in the lane will be 200 apart, the 1st will have an x value of 200, 2nd will have an x value of 400, etc.
        #means that there are 3 cars in each lane
        #the same car image is separated by 143, since the function has a variable "i", which also increase by 1
        
        list_of_cars.append(canvas.create_image(num_cars_in_each_lane*200,143*i+15, image=car_0_img_resized, anchor=NW))
        #added car number 1 into the list and spawn it into the game, in its actual lane.
        #The first car in the lane will be at x=200, the second will be at x=400, etc
        #Also spanws this car at 143+15, then 143*2+15, etc, which roughly corresponds to a lane
        list_of_cars.append(canvas.create_image(num_cars_in_each_lane*200,143*i+45+15, image=car_1_img_resized, anchor=NW))
        #added car number 2 into the list and draws/spawns it in the game, and adds it into the list
        #uses a different car image
        #x and y are similar to 1st car, except the y is shifted down a bit on canvas
        list_of_cars.append(canvas.create_image(num_cars_in_each_lane*200,143*i+90+15, image=car_2_img_resized, anchor=NW))
        #added car number 3 into the list of cars, and draw/spawns it in the game
        #uses a different car image
        #x and y are similar to 1st and 2nd car, except the y is shifted down a bit more on canvas

        #below will later be used to help track when the car crosses a lane and changes the progress bar
        list_for_lanes.append(143*i+15)
        #uses the i to also add the approximate values/location of the lanes, which is similar to where the car spawns
        #did the same thing for the other lanes, it will end up having 12 lanes, 3 different lanes that shift by a factor of 143.
        list_for_lanes.append(143*i+45+15)
        list_for_lanes.append(143*i+90+15)
#in the end, you add 36 cars, by adding (3 cars 4 times <-[12 cars in the lanes]) 3 times<- [each lane]

#functions
for i in range(12): #has a range of 12, for the 12 lanes (meaning 12 speeds that might be different from each other)
    list_of_speeds.append(random.randint(3,8)) #randomly generates a speed from 1-20 pixels, per timer milliseconds (20)
                    #then adds that into the list of speeds
     
def master_timer():
    #variable for while loop, also helps separate the   36 different cars (3 in each lane) with the car counter
    #also can separate 3 different speeds and 3 different pictures
    car_counter=0 #starts a car counter at 0 for my while loop
    while car_counter <36: #made a while loop with my variable, car_counter, though could have also used a for loop 
        temp =list_of_cars[car_counter]  #makes a new variable, temp, that will describe each car
        #first, you find out which car it is with the car_counter, 0-36
        #then you make the temp equal to each car in the list
        temp_speed=list_of_speeds[car_counter%12]
        #makes temp_speed, the speed of the car of temp
        #temp_speed should be from 0-2, since there are only 3 list items for the speeds/3 speeds
        #it is car_counter%12, which looks for the remainder of the speed for each car
        canvas.move(temp,temp_speed,0)
        #actually moves the car, it moves the x by the speed chosen, and doesn't impact the y
        car_position=canvas.coords(temp)
        #describes the position of the temporary car
        right_x = car_position[0] 
        #adding the first term in the list, car positions is right_x
        if right_x >= canvas_width: #if the position is greater than the canvas width, then it will move the car
            canvas.move(temp,-right_x,0) #it will move the car back, by teleporting it back to the front, which can be a bit less than 0 (if the car passes the canvas width)
        car_counter+=1 #added 1 to my car counter, will do that until car_counter=36
    player_coords = canvas.coords(player_car)
    #the code below would be an if, elif statement, except for the fact that it could possibly go outside of the canvas while touching the car
    if player_coords[0]<=0 or player_coords[0]>=canvas_width or player_coords[1]>=canvas_height-playercar_height: #this is my anti-cheat code. 
        #When the car goes across the left side or right side, or touches the bottom of the screen, the game will say that the player is "cheating"
        #while normally this code below should be put into another function, when I tried putting the canvas thing in another function, it wouldn't work. 
        print("Stop cheating!") #prints stop cheating
        print("You got caught!") #prints you got caught
        descript_of_site.config(text=loss_text) #configs the welcome text to loss_text
        canvas.create_image(0,0,image=loss_img,anchor=NW) #creates a new image layer above the old image on the canvas, that has the loss image
        window.after(end_milliseconds,quit) #calls the quit function, which closes itself after 1690 milliseconds (end_milliseconds)
        return #return nothing, making it so this statement is only called once
    if player_catches_car(): #this function is called each time window is called, but only when it returns true will the rest of the statement work
        #while normally this code below should be put into another function, when I tried putting the canvas thing in another function, my code wasn't working.
        print("You got caught!") #prints you got caught
        descript_of_site.config(text=loss_text) #configs the welcome text to loss_text
        canvas.create_image(0,0,image=loss_img,anchor=NW) #creates a new image layer above the old image on the canvas, 
        window.after(end_milliseconds,quit) #after end_milliseconds (1690 milliseconds), the window will close itself automatically
        return #returns nothing, making it so this statement is only called once (and you got caught will only be printed once)
    if player_coords[1]<=0: #technically, this function and the player_catches_car functions can be called at the same time, resulting in this overriding and having the game show a "you win" screen. 
        #but if you got that far into my game, you deserve to win (also because I'm too lazy to disable movement, though it's just 1 line of code)
        print("Congrats! You win the game!") #prints a congrats message
        descript_of_site.config(text=win_text) #configs the welcome text to win_text
        canvas.create_image(0,0,image=win_img,anchor=NW) #creates a new image layer above the old image(s) on the canvas 
        window.after(end_milliseconds,quit) #after end_milliseconds (1690 milliseconds), the window will automatically close itself
        return #returns nothing, but makes it so the function is only called once
    global progress_counter #re-adding lane_crossed_counter, so when I can add to the counter and increase the progress bar
    progress_counter=0 #technically reset the progress counter back to 0, but the time it does that for is extremely short
    for i in range(11,-1,-1): #start the "i" variable from 11, and goes down by 1 each time till it reaches -1
        lane_coords=list_for_lanes[i] #made the lane coordinates equal to the each of the values of the location of the lanes
        if player_coords[1]< lane_coords: #if the y value of the player is further(aka smaller) than the lane coords (since lanes go from positive to 0)       
            progress_counter+=1    #then the progress_counter (to track progress) will increase by 1 
      
    progress_meter["value"]=progress_counter #updates the progress_counter, and displays the value
    
    window.update_idletasks() #updates the idletasks
    window.update() #updates the window
    window.after(timer_milliseconds,master_timer) #after timer_milliseconds, master_timer is called again

def player_catches_car(): #function for when player hits the car
    return_variable = False #start the return variable as false, and only will change if it hits any of the cars
    for i in range(36): #makes it so it can check and go through all 36 cars easily, with a for function
        car_coords = canvas.coords(list_of_cars[i]) #checks the car coords, that is replaced for each car it checks
        #looks for the coordinates with canvas.coords of each car
        overlap_result = canvas.find_overlapping(car_coords[0], car_coords[1], 
                                                car_coords[0] + car0_width, car_coords[1] + car0_height)
        #will have the overlap for when its overlapping with any of the car's hitbox 
        #(done with 2 corners, and the other 2 corners added with the first car's width/height, becasue i'm too lazy to program all 4 corners)
        if player_car in overlap_result: #the statements says if any part of the player_car (which is the spawned player car) is in overlap_result, the 4 corners
            return_variable = True       #then return true. Else should move the cars, but they're already been moved, so it's just an if statement
    return return_variable #this will return return_variable, which will always be false, until player_car is in overlap result, it will then return true

#movement of the player (the canvas command is on the bottom, otherwise the canvas command will not call the functino to move the player)
def move_player(event): #this is the move player function, with the event variable/parameter, which is done with keypressup.
    key_symbol=event.keysym #this is a variable, key symbol, which stores the function of keysym when a key is pressed
    print(key_symbol,"was pressed") #prints the key symbol that is pressed
    if key_symbol=="Up": #if statement, that will move the canvas when the up botton is pressed
        canvas.move(player_car,0,-player_speed_vertical) #will move the player_car up when the up button is pressed, with a -y canvas movement
    if key_symbol=="Down": #if statement, that will move canvas when the down button is pressed
        canvas.move(player_car,0,player_speed_vertical) #will move the player_car down when the down button is pressed 
        #will move the player by player_speed_vertical pixels
    if key_symbol=="Left": #my brother told me to add a left, so this moves by player speed horizontal, which is 100 pixels
        canvas.move(player_car,-player_speed_horizontal,0) #moves the player's x left by player_speed_horizontal pixels
    if key_symbol=="Right": #my brother wanted a right, so same thing as left
        canvas.move(player_car,player_speed_horizontal,0) #moves the player's x right by player_speed_horizontal pixels
    if key_symbol=="space": #if statement for when space is pressed
        canvas.move(player_car,0,-player_speed_vertical) #my brother forced me to add a space bar
        #the spacebar moves the same as pressing the up arrow
        print("Imagine pressing space though, so cringe") #my brother wanted a spacebar,
#actually making the keybinds, so when the keys are pressed, it moves the player
canvas.bind_all("<KeyPress-Up>", move_player) #when "Keypressup", aka when the up key is pressed, it will call the move player function
canvas.bind_all("<KeyPress-Down>",move_player) #when "Keypressdown", aka when the down key is pressed, it will call the move player functino
canvas.bind_all("<KeyPress-Left>", move_player) #when "Keypressleft", aka when the left key is pressed, it will call the move player function
canvas.bind_all("<KeyPress-Right>", move_player) #same function as keypress up down and left but is when the right key is pressed
canvas.bind_all("<space>", move_player) #same function when up down left right keys are pressed but when space key is pressed
#this is the last thing on my code because that way I can change it easier (in case I want to bully my brother and delete a keybind >:)     

#calling the functions and my window
master_timer() #calls the master timer function, which automatically updates itself
window.mainloop() #calls the actual window and makes everything work 
