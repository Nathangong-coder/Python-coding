#Nathan Gong
#May 6th, 2022
#UI version of the fortune teller

from tkinter import *
from os import path 
#stating the variables
fortune_1='Your fortune is: You will earn a million dollars'
fortune_2='Your fortune is: You will do well in school'
fortune_3='Your fortune is: You will be successful in life'
fortune_4='Your fortune is: You will land your dream job'
fortune_5='Your fortune is: You will get a free TV'
fortune_6='Your fortune is: You will find hidden treasure'
fortune_7='Your fortune is: You will be a very successful inventor and innovator'
fortune_8='Your fortune is: You will get an A- on a test'
even="Your choice is even. Choose between 1,2,5 or 6."
odd="Your choice is odd. Choose between 3,4,7 or 8."
#defining my spell function, where I spell the word out
def spell(choice):
    #starting my letternumbercounter at 0
    letternumbercounter=0
    #creating a variable that stores my word
    color_spelled="" 
    #the actual "spell" function, where it spells out every letter. 
    # instead of printing it, it adds the letters of the color (whose name was shown through the variable/parameter color_term )          
    for letter in choice:
        #add an uppercase letter to the variable that stores my word
        color_spelled+=letter.upper()
        #add a dash to the variable that also stores my word
        color_spelled+="-"
        #for letternumbercounter it adds 1, storing how many letters are in the color
        letternumbercounter+=1
    number_directions0.config(text=color_spelled) #prints the word, spelled out by the color_spelled, that stored the upper letters and dashes
    #modular arithmetic, and it shows when the number of letters is odd, it configs "choose a number" with the odd number directions
    if letternumbercounter%2 ==1:
        odd_even_picture.config(image=odd_img)
        number_directions.config(text=odd)
    #modular arithmetic, where the number of letters is divisible by 2, and configs it with even number directions    
    if letternumbercounter%2 ==0:
        odd_even_picture.config(image=even_img)
        number_directions.config(text=even)

#creating a function
def color_search():
    #this will get whatever was typed in the entry box (entry)
    color_term=str(color_choice.get())
    #callign the function with the parameter set as "color_term"
    spell(color_term)

def number_search():
    #this will get whatever was typed in the entry box (entry)
    number_term=str(number_choice.get())
    #this is assuming when the user is good, when it inputs a number, it will print out the fortune, but if it asks for you to choose a number between 1, 2, 7, and 8, you can choose 3 and get fortune 3. 
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
#resizes the window, with geometry, by using 600x900 aspect ratio with pixels
window.geometry("600x900")
#change the window title to "Nathan's magic fortune teller"
window.title("Nathan's Magic Fortune Teller")
#filling in parts of a window
#the "Label", makes text
descript_of_site= Label(window,text="Fortune Teller: Pick a color and I will tell your fortune")
#packs it in, and fits the window into the text
descript_of_site.pack()
#adding a picture
#finding our image, the 1st line was actually grabbing, the file, the 2nd telling python that it's an image
main_img_path=path.dirname(__file__)+"\\fortune_teller_1.png"
main_img=PhotoImage(file=main_img_path)
#creating and packing the label
main_img_label=Label(window,image=main_img)
main_img_label.pack()
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

#..., will spell out the word
number_directions0=Label(window,text="...")
number_directions0.pack()

#..., will be replaced by an odd/even picture
odd_even_picture=Label(window,text="...")
odd_even_picture.pack()
#odd picture code, may replace the ...
odd_img_path=path.dirname(__file__)+"\\fortune_teller_3.png"
odd_img=PhotoImage(file=odd_img_path)
#even picture code, may replace the ...
even_img_path=path.dirname(__file__)+"\\fortune_teller_2.png"
even_img=PhotoImage(file=even_img_path)
#directions of picking a number from
number_directions= Label(window, text="Pick a number from...")
number_directions.pack()
#search bar
number_choice=Entry(window)
number_choice.pack()
#search button for the number choice
number_button= Button(window,text="Submit number", command=number_search)
number_button.pack()


#telling the fortune
fortune=Label(window, text="Your fortune is....")
fortune.pack()
#actually launches the window
#this main loop has to be in the end
window.mainloop()