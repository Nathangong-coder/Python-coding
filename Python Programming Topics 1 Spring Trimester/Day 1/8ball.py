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
fortune_1=("not a chance", 69)
fortune_2=("when pigs fly", 24)
fortune_3=("definitely", 42)
fortune_4=("probably", 240)
fortune_5=("without a doubt", 55)
fortune_6=("ask again later", 37)
fortune_7=("maybe", 19)
fortune_list=[fortune_1, fortune_2, fortune_3, fortune_4, fortune_5, fortune_6, fortune_7]
while loop=='yes' and loop_count<3:
    print('\n\n\nWelcome to the magic 8 ball! Ask a question, and see your lucky numbers and fortune for today!')
    input('Please enter your question now:')    
    fortune_slice=random.randrange(0,6)
    fortune_tuple=fortune_list[fortune_slice]
    print('Answer: ',fortune_tuple[0])
    print('Lucky number:', fortune_tuple[1])
    #need to use list changing tuple thingies that replaces one of the other fortunes
    new_fortune=input('\n\nPlease enter new fortune here:')
    new_luckyNumber=input('Please enter new lucky number here:')
    try:
        new_luckyNumber=int(new_luckyNumber) 
        new_fortune_tuple=(new_fortune,new_luckyNumber)
        fortune_list.append(new_fortune_tuple)
    except:
        type(new_luckyNumber)!=int
        print('\nPlease enter an integer as your new lucky number!')
    

    loop_answer=input('\nDo you want to hear another fortune?\n')
    loop=loop_answer.lower()
    loop_count+=1
if loop_count==3 and loop=='yes':
    print('\n\n\nToo bad, I am cutting you off!')
