#Nathan Gong
#Spring Trimester 2022
# Ms. Lewellen 
# Programming 1
#Challenge 1 Class 4

#testing random and randrange
from asyncio.windows_events import INFINITE
import  random 

x= random.randrange(1,10)

print(x)
#testing random and randrange, and using them to finish the CW
dice= random.randrange(1,7)

coin_flip= random.randrange(1,3)
deck_of_cards= random.randrange(1,53)
grade= random.randrange(70,101)
math= 2*random.randrange(INFINITE)

print(dice,coin_flip,deck_of_cards,grade,math)