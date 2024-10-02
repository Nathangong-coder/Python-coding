#Nathan Gong
#EPS Spring Trimester
#3/29/2022
#Programming 1
#Class 5 Program 3-Adventure Game

from random import randrange

loop='yes'
loop_count = 0
for x in range(3):
    print('\n')
    print('Welcome to my adveeeenture game!\n')
    adventure_answer=input('Will you start this game? ')
    if adventure_answer=="no":
        print('\n Bruh. Do you want to retry this game? ')
    elif adventure_answer=="yes":
        print('\n')
        light_or_dark= randrange(1,3)
        if light_or_dark==1:
            y='dark'
        elif light_or_dark==2:
            y='light'    
        print('Great! You enter a',y,'room')
        if y=='light':
            light_answer=input('The light room you enter is hot. You suddenly feel thirsty. Do you look for water? ')
            if light_answer=='yes':
                print('\n')
                water= randrange(1,5)
                if water==4:
                    print('You did not find water. You die of dehydration. \n')
                if water==1 or water==2 or water==3:
                    left_or_right=input('You did find water. You drink water and survive. You then find a door, you open it and walk through a dark corridor to a path that diverges into 2 rooms. Do you go inside the room on the left or the room on the right? ')
                    if left_or_right=='left':
                        cupcake=input('\nYou walk inside a room filled with cupcakes. You see the door that might lead to your escape. You know that you need to eat a bunch of cupcakes to make a path to the door. Do you dare to eat one? ')
                        if cupcake=='yes':
                            poisin_cupcake= randrange(1,5)
                            if poisin_cupcake==2 or poisin_cupcake==3 or poisin_cupcake==4: 
                                print('\n You eat poisoned cupcakes and die from the poison. \n')
                            if poisin_cupcake==1:
                                print('\n You eat through the delicious cupcakes and form a small path that leads to the exit. Congratulations! You escaped the cave! \n')
                        elif cupcake=='no':
                            print('\n The door slams shut behind you. You end up not eating the cupcakes but get crushed by the amount of cupcakes. \n')
                        else:
                            print('\nBruh, please answer yes or no \n')
                    elif left_or_right=='right':
                        vines=input('\nYou walk inside an empty room that has walls teeming with vines. Once you walk it, the door slams shut behind you. Do you climb the vines? ')
                        if vines=='yes':
                            print('\n')
                            climb_yes= randrange(1,5)
                            if climb_yes==1: 
                                print('You climb up the vines and find the exit. Congratulations! You escaped the cave! \n')
                            else:
                                print('The vines snap while you climb and you fall to your doom. \n')
                        elif vines== 'no':
                            print('You get bored in the room. You end up still wanting to climb up the vines.')
                            climb_no= randrange(1,100)
                            if climb_no==1: 
                                print('You climb up the vines and find the exit. Congratulations! You escaped the cave! \n')
                            else:
                                print('The vines snap while you climb and you fall to your doom. \n')
                        else:
                            print('\nBruh, please answer yes or no \n')
                    else:
                        print('\nBruh, please answer left or right \n')
            elif light_answer=='no':
                print('You did not look for water. You die of dehydration. \n')
            else:
                print('\nBruh, answer yes or no \n')
        if y=='dark':
            dark_answer=input('The dark room you enter is chilly. Do you look for a jacket? ')
            if dark_answer=="yes":
                jacket= randrange(1,4)
                if jacket==3:
                    print('\nYou did not find a jacket. You die of coldness. \n')
                if jacket==1 or jacket==2:
                    up_or_down=input('\nYou did find a jacket. You wear the jacket and survive. You then stumble around the room and find the door. In a darkly lit path, you see two rooms, one above you, with a rope that you can climb, and a room below you, with a stepladder for you to climb down. Do you climb down or up? ')    
                    if up_or_down=="up":
                        rope=input('On the ceiling of the top of your room you see a small beam of light. You see some rope that you can climb to the top. Do you climb the rope? ')
                        if rope=='yes':
                            print('You climb the rope and reach the top. Congratulations! You escaped the cave! \n')
                        elif rope=='no':
                            rope_no= randrange(1,100)
                            if rope_no==1:
                                print('You get bored...... You end up climbing the rope and reaching the top. Congratulations! You escaped the cave! \n')
                            else:
                                print('You were too slow, and the ground below you shifts, and you fall to your doom. \n')
                        else:
                            print('\nBruh, please answer yes or no')
                    elif up_or_down=="down":
                        print('You reach a pit of vipers. You get bitten and slowly die from the poison. \n')
                    else:
                        print('\nBruh, please answer up or down \n')
            elif dark_answer=="no":
                print('You did not look for a jacket. You die of coldness. \n')
            else:
                print(' \nBruh, answer yes or no \n')    
    else:
        print('\nBruh, please answer yes or no \n')
    loop_count= loop_count + 1
    print('You have played',loop_count,'times. Your maximum number of attempts is 3.')
    print('Would you like to play again? Well too bad! I am forcing you to play again!')
if loop_count>=3:
    print('\nToo bad, I am cutting you off, goodbye!\n')
else:
    print('\nAlright then, thank you for playing, goodbye!\n')
