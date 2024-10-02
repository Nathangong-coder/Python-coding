#Topics in Programming 
#Sudo Sensei
#March 16th, 2023

#Nathan Gong
#DRAGONS Hw


# requirements 

# 1. if/elif/else decision trees 

# 2. two input questions, one for string, another for a number 

# 3. user input should handle both lower and upper case input 

# 4. user input should be converted to an int for math 

# 5. use a math function to calculate the answer 

# 6. must handle for all invalid input 
from random import randrange 
import random
loop='yes'
loop_count=0

while loop=='yes' and loop_count<3:
    print('\nWelcome to the math dragon! Solve some math, get lucky, and do not get eaten!')
    path_choice=input('You walk up to the lair of the math dragon. You see two paths into the lair, a right path and a left path.\n Which do you choose? Left or right?')
    path_choice=path_choice.lower()
    unlucky=random.randrange(0,10)
    if path_choice=='left':
        if unlucky=='0':
            print('\nWhile walking left, you get crushed by a falling piano. You lose!')
        else:
            print('\nYou walk left, and encounter a gold chest filled with dubloons, guarded by an evil knight!')
            knight_math_problem=input('The knight has a math problem on their armor. The problem reads: What is 12+6*2?')
            try:
                knight_math_problem=int(knight_math_problem)
                if knight_math_problem==12+6*2:
                    print('\nYou slay the knight and get all the treasure. You win!')
                else:
                    print('\nYou answer the problem incorrectly, and are stabbed by the knight. You lose!')
            except:
                type(knight_math_problem)!=int
                print('\nPlease choose an integer!')        
            

    elif path_choice=='right':
        if unlucky=='0':
            print('\nWhile walking left, you get crushed by a falling piano. You lose!')
        else:
            print('\n\nYou walk right, and encounter a horde of gold, guarded by an evil two headed dragon! Thankfully, you have a sword that can cut the heads of the dragon, as long as your number matches the answer to the math problems.')
            dragon_math_problem=input('The first head has the problem: What is 5^2+12^2=? The second head has the problem: What is 10*20-31?')
            try:
                dragon_math_problem=int(dragon_math_problem)
                if dragon_math_problem==10*20-31:
                    print('\nYou slay the knight and get all the treasure. You win!')
                else:
                    print("\nYou try to slice the dragon's neck, but is quickly burned to a crisp. You lose!")
            except:
                type(dragon_math_problem)!=int
                print('\nPlease choose an integer!') 
    else:
        print('Please choose either left or right!')

    loop_answer=input('\nDo you want to play again?\n\n\n')
    loop=loop_answer.lower()
    loop_count+=1