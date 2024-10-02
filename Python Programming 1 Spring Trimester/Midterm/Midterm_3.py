#Nathan Gong
#Spring Trimester 2022, Prog 1
#Ms. Lewellen
#Midterm_2
#passing grade is 60 percent or more, failing grade is less than 60 percent 

import random

number = random.randrange(0,53)
#this changes the top number, 0-53, and divides it by 4. Now, the lowest value will be 0, but the last one will be 13, since it will only choose numbers from 0-52. We want the value to be an integer, so then the next line
#basically just casted our value, our decimal/float number back into an integer. This is a bit confusing to me since there will be 53 cards in the deck. Also, the computer will round down, so 1/4 will round to 0.
value = int(number / 4)

#now, there isn't a "0", card in the deck, so it has been replaced by the K. There also isn't a "1", "11", or "12" card in the deck, so those have also all been replaced. 
if value == 1:
    value = 'A'
elif value == 11:
    value = 'J'
elif value == 12:
    value = 'Q'
elif value == 0:
    value = 'K'
#I am a bit confused by the code, however, since it is possible to get 13, but there isn't a card available for that one, so is it possible to get "13 of hearts"
#everything else has a value stated for the number, for the 2 equalling the 2 of something, 3 equalling the 3 of something, etc.
else:
    value = value
#Then you just split the probability of getting any of the cards equal to around 25%, with each one equalling a different suit. 
if number % 4 == 0:
#you did a percent because then the bottom 1/4 of the numbers will be 0, which is similar to the probability of drawing a H.
    print(value, "of hearts")
#the same has happened with diamonds, spades, and clubs.
elif number % 4 == 1:
    print(value, "of diamonds")
elif number % 4 == 2:
    print(value, "of spades")
elif number %4 == 3:
    print(value, "of clubs")
