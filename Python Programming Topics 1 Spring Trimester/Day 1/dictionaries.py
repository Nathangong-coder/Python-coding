#Topics
#Sudo Sensei
#March 20, 2023
#Nathan Gong


from random import randrange 
import random
#challenge 1
peer = {
    "first_name": "Arthur",
    "last_name": "Gong",
    "age" : 14,
    "hobby" : "Bridge"
}
print('challenge 1:')
for x in peer:
    print(x+":",peer[x])
#challenge 2
favorite_animals = {
    "Nolan" : "Owl", 
    "Allie" : "Giraffe", 
}
print('\n\nChallenge 2:')
for y in favorite_animals:
    print(y+"'s favorite animal is: "+ favorite_animals[y])
new_name=input('Please enter new name: ')
new_fav_numb=input("Please enter "+new_name+"'s favorite animal: ")
favorite_animals.update({new_name:new_fav_numb})
print('\n')
for y in favorite_animals:
    print(y+"'s favorite animal is: "+favorite_animals[y])

#challenge 3
question_1="the function that allows you to make all letters lowercase in python"
question_2="the data set that is a collection, is ordered and unchangable, and allows duplicate members"
question_3="the data set that stores key/value pairs"
question_4="the country that ate the most meat in 2015"
question_5="the proper name for the # sign"
question_count=4
loop='yes'

question_list=[]
answer_list=[]
quiz={
    question_1: "lower()",
    question_2: "lists",
    question_3: "dictionary",
    question_4: "australia",
    question_5: "octothorpe"
}


def update():
    question_list.clear()
    answer_list.clear()
    for questions in quiz:        
        question_list.append(questions)
    for answers in quiz:
        answer_list.append(quiz[answers])

print('\n\n\nChallenge 3:')
while loop=='yes':
    update()
    question_number=random.randrange(0,question_count)
    question_answer=input("What is "+question_list[question_number]+"? ")
    question_answer=question_answer.lower()
    if question_answer==answer_list[question_number]:
        print('\nCorrect!')
    else:
        print('\nIncorrect! '+answer_list[question_number]+' is '+question_list[question_number])
    new_question=input("\nPlease enter new question:")
    new_answer=input("Please enter new answer:")
    quiz[new_question]=new_answer
    question_count+=1
    loop=input("Do you want to play again?\n\n\n")