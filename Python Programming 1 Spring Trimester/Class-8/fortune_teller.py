from tkinter import Variable
#stating my variables
fortune_1='You will earn a million dollars'
fortune_2='You will do well in school'
fortune_3='You will be successful in life'
fortune_4='You will land your dream job'
fortune_5='You will get a free TV'
fortune_6='You will find hidden treasure'
fortune_7='You will be a very successful inventor and innovator'
fortune_8='You will lose a million dollars'

#stating my functions
def my_function():
    x=input('Red, Blue, Green, or Yellow? ')
    if x=="Red":
        print('\nR.E.D.')
        my_function_odd()
    if x=="Blue":
        print('\nB.L.U.E.')
        my_function_even()
    if x=="Green":
        print('\nG.R.E.E.N.')
        my_function_odd()
    if x=="Yellow":
        print('\nY.E.L.L.O.W.')
        my_function_even()
    
def my_function_odd():
    odd_input=input('Now choose between 1, 2, 5, or 6. ')
    if odd_input=='1':
        print()
        print(fortune_1)
    if odd_input=='2':
        print()
        print(fortune_2)
    if odd_input=='5':
        print()
        print(fortune_5)
    if odd_input=='6':
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
    if even_input=='7':
        print()
        print(fortune_7)
    if even_input=='8':
        print()
        print(fortune_8)

#calling my function
my_function()