#Nathan Gong
#May 16, 2022
#Programming 1
#Lewellen Prog 1

from tkinter import *
from os import path
from tkinter.ttk import Progressbar

#you can replace pack with .grid with rows and columns, if spanning more than 1 column,
#then say xx.grid (row=y, column=lowest number, columnspan=z)
#starting these "welcome" text, which will change depending on the condition of the dog
welcome="Welcome to my pet project! This is my pug, Bob, take care of him!"
sad="Oh no! Bob is sad now!"
happy="Good job! Bob is happy now!"
#defining my variables, and having them start at 5
fullness_counter=7
fearfulness_counter=5
#defining my functions
def feed_button_clicked():
    global fullness_counter
    fullness_counter+=1
    update_ui()
def pet_button_clicked():
    global fearfulness_counter
    fearfulness_counter+=1
    update_ui()
def master_timer():
    #code to update values going down with time
    #made the variable global to use it in my function
    global fullness_counter
    global fearfulness_counter
    #will subtract 1 every time master_timer is called,
    #which is called after 2 seconds
    fullness_counter-=1
    fearfulness_counter-=1
    #this adjusts fullness and fearfulness counter if they less than 0
    if fullness_counter<0:
        fullness_counter+=1
    if fearfulness_counter<0:
        fearfulness_counter+=1
    #this adjusts fullness and fearfulness counter if they go over 10
    if fullness_counter>10:
        fullness_counter-=1
    if fearfulness_counter>10:
        fearfulness_counter-=1
    #updates ui based off of new stats
    update_ui()
    #repeats by calling master_timer function every 2 seconds 
    window.after(2000,master_timer)

def update_ui():
    print("updating UI")    
    global fearfulness_counter
    global fullness_counter
    #updating the fullness meter and calmness meter
    belly_full_meter["value"]=fullness_counter
    calm_full_meter["value"]=fearfulness_counter
    #your choice diagram goes here
    if fullness_counter>5 and fearfulness_counter>5:
        #if both are greater than 5 (6-10), then my pug will be happy, and the text will change to "Congrats! Bob is happy now!"
        image_label.config(image=resized_happy_pug_img) 
        descript_of_site.config(text=happy)
    elif 6>fearfulness_counter>-1 and fullness_counter>5: 
        #less than 6, that way some of my conditions don't override each other
        #this is when my fullness is greater than 5 but my fearfulness is lower than 6
        #this will also change it back to the "Welcome" text
        image_label.config(image=resized_scared_pug_img)
        descript_of_site.config(text=welcome)
    elif fearfulness_counter >5 and 6>fullness_counter>-1: 
        #less than 6, that way some of my conditions don't override each other
        #this is when my fearfulness is great than 5, but my fullness is lower than 6
        #this will also change it back to the "welcome" text
        image_label.config(image=resized_sad_pug_img)        
        descript_of_site.config(text=welcome) 
    else:
        image_label.config(image=resized_hangry_scared_pug_img) 
        #if the image label is less than 5 on both, it will fall into the else place, and make this hangry scared pug img
        descript_of_site.config(text=sad)
    #make sure tkinter processes all events
    window.update_idletasks()
    window.update()
#creating the window, changing its size, and adding a title
window=Tk()
window.geometry("450x900")
window.title("Midterm Pet Project")
#description with text of the website, and welcoming the player
descript_of_site=Label(window, text=welcome)
descript_of_site.grid(row=0, column=0, columnspan=2)

#starting picture of the website
hangry_scared_pug_path=path.dirname(__file__)+"\\Hangry scared pug.PNG"
hangry_scared_pug_img=PhotoImage(file=hangry_scared_pug_path)
resized_hangry_scared_pug_img=hangry_scared_pug_img.subsample(2,2) #resizing the image by zooming it out
#creating a label of the picture
image_label=Label(window,image=resized_hangry_scared_pug_img)
image_label.grid(row=1, column=0, columnspan=2, rowspan=2)

#replacements picture (happy, sad, and scared pug pngs)
#happy pug
happy_pug_path=path.dirname(__file__)+"\\Happy pug.PNG"
happy_pug_img=PhotoImage(file=happy_pug_path)
resized_happy_pug_img=happy_pug_img.subsample(2,2) #resizing the image by zooming it out
#sad pug
sad_pug_path=path.dirname(__file__)+"\\Sad pug.PNG"
sad_pug_img=PhotoImage(file=sad_pug_path)
resized_sad_pug_img=sad_pug_img.subsample(2,2) #resizing the image by zooming it out
#scared pug
scared_pug_path=path.dirname(__file__)+"\\Scared pug.PNG"
scared_pug_img=PhotoImage(file=scared_pug_path)
resized_scared_pug_img=scared_pug_img.subsample(2,2) #resizing the image by zooming it out
#fearfulness-label, describing the progress bar for fearfulness
fearfullness_label=Label(window,text="Fearfulness") 
fearfullness_label.grid(row=3, column=0)
#fullnessbar-label, describing the progress bar for the hungriness
belly_full_label=Label(window,text="Hungriness")
belly_full_label.grid(row=3, column=1)

#progressbar-fullness
belly_full_meter=Progressbar(window,length=100, mode="determinate", orient=HORIZONTAL, max=10)
belly_full_meter["value"]=fullness_counter 
#stating the meter progress as a variable, so i increase the number of the meter
belly_full_meter.grid(row=4, column=1)
#progressbar-fearfulness
calm_full_meter=Progressbar(window,length=100,mode="determinate", orient=HORIZONTAL, max=10)
calm_full_meter["value"]=fearfulness_counter 
#stating the meter progress as a variable, so i can increase the number of the meter later
calm_full_meter.grid(row=4, column=0)

#calm and full buttons
calm_button=Button(window,text="Play with Bob", command=pet_button_clicked) 
#calls the function pet_button_clicked when button is clicked
calm_button.grid(row=5, column=0)

full_button=Button(window,text="Feed Bob", command=feed_button_clicked) 
#call the function feed_button_clicked when the button is clicked
full_button.grid(row=5, column=1)

master_timer()
window.mainloop()