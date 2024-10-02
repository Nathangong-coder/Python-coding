from tkinter.messagebox import YES


print("You go to school",",then, you go to class",",then, you check for thirst.")
answer=input('Are you thirsty? ')

if answer=='yes':
    print("you drink some water")
elif answer=='no':
    print("you do not drink some water")
    answer=input('Now you feel dehydrated. Are you going to drink some more water? ')
    if answer=='yes':
        print("Now you feel refreshed")
    elif answer=='no':
        print("Now you feel depressed")
    else:
        print("bruh answer yes or no")
elif answer=='maybe':
    print("perhaps you should drink some water")
else: 
    print("bruh answer yes or no")