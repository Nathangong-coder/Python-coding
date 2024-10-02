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
    letter=spell(choices)
    return choices

def spell(choice):
 #   letternumbercounter=0
    for letter in choice:
        print(letter)
   #     letternumbercounter+=1
   #     if letternumbercounter%2 ==1:
   #         print('1,2,5,6')
   #     elif letternumbercounter%2 ==0:
    #        print('3,4,7,8')
    
def my_function_odd():
    odd_input=input('Now choose between 1, 2, 5, or 6. ')
    if odd_input=='1':
        print()
        print(fortune_1)
    if odd_input=='2':
        print()
        print(fortune_2)
    elif odd_input=='5':
        print()
        print(fortune_5)
    elif odd_input=='6':
        print()
        print(fortune_6)
    

def my_function_even():
    even_input=input('Now choose between 3, 4, 7 or 8. ')
    if even_input=='3':
        print()
        print(fortune_3)
    if even_input=='4':
        print()
        print(fortune_4)
    elif even_input=='7':
        print()
        print(fortune_7)
    elif even_input=='8':
        print()
        print(fortune_8)
    
#calling my function
choose_color()