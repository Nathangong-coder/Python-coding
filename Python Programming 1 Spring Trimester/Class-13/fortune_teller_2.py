#April 27, 2022
#May 2022
#EPS Prog 1
#Ms. Lewellen
#Nathan Gong

#stating my variables
COLOR1="red"
COLOR2="blue"
COLOR3="yellow"
COLOR4="green"
fortune_1='You will earn a million dollars'
fortune_2='You will do well in school'
fortune_3='You will be successful in life'
fortune_4='You will land your dream job'
fortune_5='You will get a free TV'
fortune_6='You will find hidden treasure'
fortune_7='You will be a very successful inventor and innovator'
fortune_8='You will get an A on a test'
#stating my functions
#input parameters = 
#return value: Choice (a string containing a color)
#user input: choice (a string containing a color)
def choose_color():
    choices=input('Choose a color'+" "+COLOR1+" "+COLOR2+" "+COLOR3+" "+COLOR4+"\n")
    return choices

#function that spells out a word (color) that was passed in
#input parameters: choice (string) contains the name of a color
#return value: -
#user input: -
def spell(choice):
    letternumbercounter=0
    for letter in choice:
        print(letter)
        letternumbercounter+=1
    return(letternumbercounter)

#function to allow the user to pick a number
#input parameter: set (int) - set is the length of the spelled word
#return value: the number that they chose
#user input: the number that they chose
def pick_number(set):
    if set%2 ==0:      #even
        choice=input("Your number is even. Choose between 1,2,5 or 6.\n")
    else: #odd
        choice=input("Your number is odd. Choose between 3,4,7, or 8.\n")
    return choice
#function to actually print out the fortune
#input parameter: choice- the user's chosen number
#return value: -
#output: the fortune that match the chosen number (print)
#user input: -
def print_fortune(choice):
    if choice=="1":
        print(fortune_1)
    elif choice=="2":
        print(fortune_2)
    elif choice=="3":
        print(fortune_3)
    elif choice=="4":
        print(fortune_4)
    elif choice=="5":
        print(fortune_5)
    elif choice=="6":
        print(fortune_6)
    elif choice=="7":
        print(fortune_7)
    elif choice=="8":
        print(fortune_8)
    else:
        print("That was not a very good choice.")
chosen_color=choose_color()
length_of_color=spell(chosen_color)
chosen_number=pick_number(length_of_color)
print_fortune(chosen_number)