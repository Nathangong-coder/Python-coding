#Nathan Gong
#May 6th, 2022
#UI version of the fortune teller

from tkinter import *
from os import path 
#stating the variables
fortune_1='Your fortune is: you will earn a million dollars'
fortune_2='You will do well in school'
fortune_3='You will be successful in life'
fortune_4='You will land your dream job'
fortune_5='You will get a free TV'
fortune_6='You will find hidden treasure'
fortune_7='You will be a very successful inventor and innovator'
fortune_8='You will get an A on a test'
even="Your choice is even. Choose between 1,2,5 or 6."
odd="Your choice is odd. Choose between 3,4,7 or 8."

def spell(choice):
    letternumbercounter=0
    color_spelled=""
    for letter in choice:
        color_spelled+=letter
        color_spelled+="-"
    number_directions0.config()

#creating a function
def color_search():
    #this will get whatever was typed in the entry box (entry)
    color_term=str(color_choice.get())
    if color_term=='blue':
        number_directions0.config(text="B-L-U-E")
        number_directions.config(text=even)
    elif color_term=='yellow':
        number_directions0.config(text='Y-E-L-L-O-W')
        number_directions.config(text=even)
    elif color_term=='red':
        number_directions0.config(text='R-E-D')
        number_directions.config(text=odd)
    elif color_term=='green':
        number_directions0.config(text='G-R-E-E-N')
        number_directions.config(text=odd)
    else:
        print("that was not the best choice")
def number_search():
    #this will get whatever was typed in the entry box (entry)
    number_term=str(number_choice.get())
    if number_term=='1':
        fortune.config(text=fortune_1)
    elif number_term=='2':
        fortune.config(text=fortune_2)
    elif number_term=='3':
        fortune.config(text=fortune_3)
    elif number_term=='4':
        fortune.config(text=fortune_4)
    elif number_term=='5':
        fortune.config(text=fortune_5)
    elif number_term=='6':
        fortune.config(text=fortune_6)
    elif number_term=='7':
        fortune.config(text=fortune_7)
    elif number_term=='8':
        fortune.config(text=fortune_8)
    else:
        fortune.config(text="That was not the best choice.")


#creates a window
#must be the first thing before you pack things
window = Tk()
#resizes the window, with geometry, by using 400x600 aspect ratio with pixels
window.geometry("400x600")
#filling in parts of a window
#the "Label", makes text
descript_of_site= Label(window,text="Fortune Teller: Pick a color and I will tell your fortune")
#packs it in, and fits the window into the text
descript_of_site.pack()
#directions of picking a color from red, blue, yellow, or green
color_directions= Label(window, text="Pick a color from red, blue, yellow, or green.")
color_directions.pack()
#asking for a search query, it's the bar that you type in
color_choice = Entry(window)
#packing it in, just like everything else
color_choice.pack()

#makes a search button, with the text on it that says "search"
#the command part actually gets the contents of the entry box, and just equals the function to call it
color_button= Button(window, text="Submit Color", command=color_search)
#packing it in, just like everything else
color_button.pack()

#...
number_directions0=Label(window,text="...")
number_directions0.pack()
#directions of picking a number from
number_directions= Label(window, text="Pick a number from...")
number_directions.pack()
#search bar
number_choice=Entry(window)
number_choice.pack()
#search button for the number choice
number_button= Button(window,text="Submit number", command=number_search)
number_button.pack()

#telling the fortuen
fortune=Label(window, text="Your fortune is....")
fortune.pack()
#adding a picture
#finding our image, the 1st line was actually grabbing, the file, the 2nd telling python that it's an image
main_img_path=path.dirname(__file__)+"\\fortune_teller.png"
main_img=PhotoImage(file=main_img_path)
#creating and packing the label
main_img_label=Label(window,image=main_img)
main_img_label.pack()
#actually launches the window
#this main loop has to be in the end
window.mainloop()