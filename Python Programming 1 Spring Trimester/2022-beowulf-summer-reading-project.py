from random import randrange 
import random
from re import M 
def bad_3():
    print('Please choose a, b, or c! Because you did not choose a, b, or c, this attempt is cancelled.')
def bad_2():
    print('Please choose a or b! Because you did not choose a or b, this attempt is cancelled.')
def bad_4():
    print('Please choose a, b, c, or d! Because you did not choose a, b, c, or d, this attempt is cancelled.')

loop='yes'
loop_count=0
ignore_counter=0
warn_counter=0
nerves_counter=0
wait_counter=0
mom_counter=0
annoy_son_counter=0
revenge_son_counter=0
look_counter=0
victory_wait_counter=0
unferth_counter=0
wait_help_counter=0

while loop=='yes' and loop_count<3:
    print('\n')
    print('-----------------------------------------------------------------------------------------------------')
    print('\nWelcome to the Beowulf the adventure game, you get 3 tries to get all the endings, good luck!')
    print('\nMen do not know how to say truly-not trusted counselors, nor heroes under heavens-who received that cargo. -Beowulf (50-53)')
    print('\nPrologue: Scyld Scelfing was a good king, a king that all the encircling nations obeyed. He had a son named Beowulf, renowned, with his fame spreading through the Scandinavian Lands. After Scyld Scelfing passed away, he was buried on a treasure-filled ship set towards the sea.')
    print('\nNow it is your turn, to become a part of the Beowulf lore, who will you choose? ')
    character_choice=input('Would you like to be (a) Grendel, (b) the mother of Grendel, or (c) Beowulf? ')
    if character_choice=='a':
        print('\nYou have selected Grendel as your main character!')
        print('\n\nChapter 1: A bold demon [you, Grendel] who waited in darkness wretchedly suffered all the while, for every day he heard the joyful din loud in the hall, with the harp sounds, the clear song of the scop (86-90)')
        print('\nYou are tired of the citizens of the Geats/Scyldings of celebrating each night, resent their joy, and want to fill your thirst for blood.')
        grendel_chapter_1=input('\nDo you decide to (a) do something about it, (b) ignore it, or (c) ask your mother to do something about it? ')
        while grendel_chapter_1=='b' and ignore_counter<3:
            print('\nYou suffer while you decide to ignore the people in the mead hall.....')
            ignore_counter+=1
            grendel_chapter_1=input('\nIf you continue this, you will suffer greatly. Do you decide to (a) do something about it, (b) keep ignoring it, or (c) ask your mother to do something about it? ')
        while grendel_chapter_1=='c' and mom_counter==0:
            print('\n\nYou ask your mom for help, but she does not answer your call for help. She tells you to solve the problem on your own.')
            mom_counter+=1
            grendel_chapter_1=input('\nNow that you know your mom does not want to help you, do you (a) do something about it, (b) ignore it, or (c) keep asking your mom for help?')
        if grendel_chapter_1=='a':
            print('\n\nChapter 2: When night descended he went to seek out the high house, to see how the Ring-Danes had bedded down after their beer-drinking. He found therein a troop of nobles asleep after the feast; they knew no sorrow or human misery. The unholy creature, grim and ravenous, was ready at once, ruthless, and cruel, and took from their rest thirty thanes; thence he went rejoicing in his booty, back to his home, to seek out his abode with his fill of slaughter. (Beowulf 115-125)')
            print('\nYou decide to feast on some people, you occupy Heorot, and take home some treasure!')
            print('But, because of your crimes against the Geats, there are talks among the Geatish people about mounting an attack at you and getting revenge for the 12 winters that you ate people.')
            grendel_chapter_2=input('\nDo you decide to (a) prepare for a battle, (b) ignore the preparations, or (c) apologize to the Geats and promise not to do it again? ')
            if grendel_chapter_2=="a":
                print('\n\nChapter 3: In preparation for the battle that you are about to have, you sneak inside the Scylding armory to steal their weapons.')
                grendel_chapter_2_prepare=input('\nDo you steal (a) the Scylding blade named Hrunting, (b) the Scylding helmet, (c) the Scylding war-shirt , or (d) nothing?')
                if grendel_chapter_2_prepare=="a":
                    print('\n\nChapter 4:[T]hat hitled sword was named Hrunting, unique among ancient treasures-its edge was iron, etched with poison stripes, hardened with the blood of war; it had never failed any man who grasped it in his hands in battle (1457-1461)')
                    print('You steal the Scylding blade, and return back to your new lair in Heorot. Soon, Beowulf arrives in your lair with an army.')
                    grendel_chapter_3_prepare=input('\nDo you (a) fight Beowulf and his army with the sword, (b) fight Beowulf and his army with nothing but your bare arms, or (c) run away from battle?')
                    if grendel_chapter_3_prepare=='a':
                        sword_use=random.randrange(0,5)
                        if sword_use>=3:
                            print('\n\nChapter 5:Your sword is effective against the army, and quickly you wipe all the troops out. As Beowulf tries to leap at you, you stab him. You win!')
                        if sword_use<3:
                            print('\n\nChapter 5:Your sword is effective against the army, but quickly, Beowulf leaps at you and tears your arm off, forcing you to retreat back to your lair. Soon, you are decapitated by Beowulf. You lose.')
                    elif grendel_chapter_3_prepare=='b':
                        print('\n\nChapter 5: You try to fight the army with your bare hands, but out of nowhere, Beowulf jumps at your arm and tears it off. You are forced to retreat and quickly get beheaded. You lose. ')
                    elif grendel_chapter_3_prepare=='c':
                        print('\n\nChapter 5: You try to run away from Beowulf, but he catches you and captures you. You lose.')
                    elif grendel_chapter_3_prepare!='a' and grendel_chapter_3_prepare!='b' and grendel_chapter_3_prepare!='c':
                        bad_3()
                elif grendel_chapter_2_prepare=="b":
                    print('\n\nChapter 4: The shining helmet, decorated with treasure, encircled with a splendid band, as a weapon-smith in days of old had crafted it with wonders, set boar-images, so that afterwards no blade or battle-sword might ever bite it (1450-1454).')
                    print('You steal the Scylding helmet, and return back to your new lair in Heorot. Soon, Beowulf arrives in your lair with an army.')
                    grendel_chapter_4_helmet=input('\nDo you (a) fight Beowulf and his army with the helmet, (b) fight Beowulf with nothing but your bare hands, or (c) try to run away?')
                    if grendel_chapter_4_helmet=='a':
                        print('\n\nChapter 5: Unfortunately, the helmet is too small for you, so you go into battle with nothing but your bare hands. Unfortunately, Beowulf jumps out of nowhere and tears your arm off, forcing you to retreat. Later, you get decapitated for your crimes. You lose.')
                    if grendel_chapter_4_helmet=='b':
                        print('\n\nChapter 5: You try to fight the army with your bare hands, but out of nowhere, Beowulf jumps at your arm and tears it off. You are forced to retreat and quickly get beheaded. You lose.')
                    if grendel_chapter_4_helmet=='c':
                        print('\n\nChapter 5: You try to run away from Beowulf, but he catches you and captures you. You lose.')
                    elif grendel_chapter_4_helmet!='a' and grendel_chapter_4_helmet!='b' and grendel_chapter_4_helmet!='c':
                        bad_3()
                elif grendel_chapter_2_prepare=="c":
                    print('\n\nChapter 4: The broad war-shirt, woven by hand, cunningly made, had to test the mere-it knew well how to protect his bone-house so that a battle-grip might not hurt his breast nor an angry malicious clutch touch his life. (1443-1447)')
                    print('You steal the Scylding war-shirt, and return back to your new lair in Heorot. Soon, Beowulf arrives in your lair with an army.')
                    grendel_chapter_4_shirt=input('\nDo you (a) fight Beowulf and his army with the war-shirt, (b) fight Beowulf with nothing but your bare hands, or (c) try to run away?')
                    if grendel_chapter_4_shirt=='a':
                        print('\n\nChapter 5: Unfortunately, the war-shirt is too small for you, so you go into battle with nothing but your bare hands. Unfortunately, Beowulf quickly tears off your arm, forcing you to retreat back to your lair. Later, you get decapitated by Beowulf for your crimes. You lose. ')
                    if grendel_chapter_4_shirt=='b':
                        print('\n\nChapter 5: You try to fight the army with your bare hands, but out of nowhere, Beowulf jumps at your arm and tears it off. You are forced to retreat and quickly get beheaded. You lose.')    
                    if grendel_chapter_4_shirt=='c':
                        print('\n\nChapter 5: You try to run away from Beowulf, but he catches you and captures you. You lose.')
                    elif grendel_chapter_4_shirt!='a' and grendel_chapter_4_shirt!='b' and grendel_chapter_4_shirt!='c':
                        bad_3()
                elif grendel_chapter_2_prepare=="d":
                    print('\n\nChapter 4: You steal nothing, but once you return back to your new lair in Heorot, Beowolf arrives in your lair with an army.')
                    grendel_chapter_4_nothing=input('\nDo you (a) fight Beowulf with nothing but your bare hands or (b) try to run away?')
                    if grendel_chapter_4_nothing=='a':
                        print('\n\nChapter 5: You try to fight the army with your bare hands, but out of nowhere, Beowulf jumps at your arm and tears it off. You are forced to retreat and quickly get beheaded. You lose.')
                    if grendel_chapter_4_nothing=='b':
                        print('\n\nChapter 5: You try to run away from Beowulf, but he catches you and captures you. You lose.')
                    elif grendel_chapter_4_nothing!='a' and grendel_chapter_4_nothing!='b':
                        bad_3()
                elif grendel_chapter_2_prepare!='a' and grendel_chapter_2_prepare!='b' and grendel_chapter_2_prepare!='c' and grendel_chapter_2_prepare!='d':
                    bad_4()
            elif grendel_chapter_2=="b":
                print('\n\nChapter 3: You ignore the Scylding army as they prepare for battle. You get bored and want to wreak more havoc.')
                grendel_chapter_4_ignore=input('Do you (a) go back to the mead hall to eat more people, (b) wait for the army inside your lair, or (c) seek help from your mom?')
                if grendel_chapter_4_ignore=='a':
                    print('\n\nChapter 4: You go back to the mead hall to eat more people, but immediately gets swarmed by the army of Beowulf.')
                    grendel_chapter_5_ignore=input('Do you (a) try to fight back against the army, (b) surrender to the army, or (c) try to run away?')
                    if grendel_chapter_5_ignore=='a':
                        print('\n\nChapter 5: You try to fight the surrounding army, but out of nowhere, Beowulf jumps at your arm and tears it off. You are forced to retreat and quickly get beheaded. You lose.')
                    if grendel_chapter_5_ignore=='b':
                        print('\n\nChapter 5: You surrender to the Geatish people, who arrest you and throw you into their dungeon. You lose!')
                    if grendel_chapter_5_ignore=='c':
                        print('\n\nChapter 5: You try to run away from Beowulf, but he catches you and captures you. You lose.')
                    elif grendel_chapter_5_ignore!='a' and grendel_chapter_5_ignore!='b' and grendel_chapter_5_ignore!='c':
                        bad_3()
                if grendel_chapter_4_ignore=='b':
                    grendel_chapter_5_ignore_lair=input('\n\nChapter 4: The Scylding army eventually breaks into your lair and demands you surrender. Do you (a) try to fight the army, (b) surrender to the army, or (c) try to run away?')
                    if grendel_chapter_5_ignore_lair=='a':
                        print('\n\nChapter 5: You try to fight the surrounding army, but out of nowhere, Beowulf jumps at your arm and tears it off. You are quickly captured and beheaded. You lose.')
                    if grendel_chapter_5_ignore_lair=='b':
                        print('\n\nChapter 5: You surrender to the Geatish people, who arrest you and throw you into their dungeon. You lose.')
                    if grendel_chapter_5_ignore_lair=='c':
                        print('\n\nChapter 5: You try to run away from Beowulf, but he catches you and captures you. You lose.')
                    elif grendel_chapter_5_ignore_lair!='a' and grendel_chapter_5_ignore_lair!='b' and grendel_chapter_5_ignore_lair!='c':
                        bad_3()
                if grendel_chapter_4_ignore=='c':
                    mom_help=random.randrange(0,10)
                    if mom_help>2:
                        print('\n\nChapter 4: You enlist the help of your mom, who easily helps you destroy the Scylding army.')
                        print('congratulations! You win! Play again to try to find all the ways to beat the game!')
                    if mom_help<=2:
                        print('\n\nChapter 4: Unfortunately, your mom does not agree to help you, and the Scylding army is too powerful. They capture both you and your mom. You lose.')
                elif grendel_chapter_4_ignore!='a' and grendel_chapter_4_ignore!='b' and grendel_chapter_4_ignore!='c':
                    bad_3()
            elif grendel_chapter_2=="c":
                grendel_chapter_2_arrested=input('\n\nChapter 3: You apologize to the Geatish people, who point their cannons and spears at you. They tell you to stand down and surrender. Do you (a) surrender or (b) fight back? ')
                if grendel_chapter_2_arrested=='a':
                    print('\nChapter 4: You surrender to the Geatish people, who arrest you and throw you into their dungeon. You lose.')
                elif grendel_chapter_2_arrested=='b':
                    print('\nChapter 4: You hurriedly fight swarm after swarm of Geatish armies, deflecting all of the miniscule blows. But soon, Beowulf arrives. Although unprepared, he uses all of his might to smite you. You lose.')
                elif grendel_chapter_2_arrested!='a' and grendel_chapter_2_arrested!='b':
                    bad_2() 
            elif grendel_chapter_2!='a' and grendel_chapter_2!='b' and grendel_chapter_2!='c':
                bad_3()        
        if grendel_chapter_1=='c' and mom_counter==1:
            print('\n\nChapter 2: Your mom gets annoyed by you asking her for help. She forces you to the Geatish people and tell them how you feel, which ends with you getting captured. You lose.')
            mom_counter=0
        elif grendel_chapter_1=="b" and ignore_counter==3:
            print('\n\nChapter 2: By ignoring the partying that goes on every night, you become overly stressed and cannot live here anymore. You lose.')
            ignore_counter=0
        if grendel_chapter_1!='a' and grendel_chapter_1!='b' and grendel_chapter_1!='c':
            bad_3()
    elif character_choice=='b':
        print('\n\nChapter 1(background): You, the mother of Grendel, descended from the race of cains. Currently, you live in an underwater lair with your son. Your son has just ate some Scyldings and taken over Heorot. Unfortunately, the Scyldings want revenge.')
        mom_chapter_1=input('\nDo you (a) help protect your son or (b) ignore the problem and do nothing?')
        if mom_chapter_1=='a':
            print('\n\nChapter 2: You help protect your son by telling him to live with you for a while, but quickly, he gets bored of it. He wants to leave the lair and wreak some more havoc, no matter the consequences.')
            mom_chapter_2=input('\nDo you (a) let him leave your lair, (b) let him leave (but go with him), or (c) forbid him from leaving?')
            while mom_chapter_2=='c' and annoy_son_counter==0:
                print('\n\nYour son gets extremely annoyed that he cannot leave the lair. If he keeps asking and you keep refusing, something bad may happen. ')
                annoy_son_counter+=1
                mom_chapter_2=input('\nDo you (a) let him leave your lair, (b) let him leave (but go with him), or (c) continue to forbid him from leaving his lair?')
            if mom_chapter_2=='a':
                print('\n\nChapter 3: Grendel was forced to flee, fatally wounded, into the fen, seek a sorry abode; he knew quite surely that the end of his life had arrived, the sum of his days. (Beowulf 819-823)')
                print('Your son, Grendel, is critically injured after he leaves the lair on your advice. You are crushed by the guilt of not protecting your son and of the devastating news, and try to get revenge by attacking Beowulf, who captures you and beheads you. You lose.')
            if mom_chapter_2=='b':
                print('\n\nChapter 3: When you go with your son to talk to the Scylding army and Beowulf, they tell you to surrender.')
                mom_chapter_3_leave=input('\nDo you (a) fight the Scylding army with your son, (b) surrender and tell your son to do the same, or (c) try to run away?')
                if mom_chapter_3_leave=='a':
                    fight_luck=random.randrange(0,7)
                    if fight_luck>1:
                        print('\n\nChapter 4: You successfully beat the Scylding army with your son, and take out Beowulf.')
                        print('Congratulations! You win! Play again to try to find all the ways to beat the game!')
                    if fight_luck<=1:
                        print('\n\nChapter 4: Unfortunately, you and your son, Grendel, were overwhelemd by the Scylding army, and quickly captured. You lose.')
                if mom_chapter_3_leave=='b':
                    print('\n\nChapter 4: You surrender and tell your son to do the same, which he does. Unfortunately, you two are then thrown into a dungeon and remain there for an eternity. You lose.')
                if mom_chapter_3_leave=='c':
                    print('\n\nChapter 4: You try to run away with your son, but you two are quickly captured and beheaded by Beowulf and his army. You lose.')
                elif mom_chapter_3_leave!='a' and mom_chapter_3_leave!='b' and mom_chapter_3_leave!='c':
                    bad_3()            
            if mom_chapter_2=='c' and annoy_son_counter==1:
                print('\n\nChapter 3: Your son is fed up with being in your lair, and ends up fighting with you. The fight ends with your son pushing you to your doom. You lose.')
            elif mom_chapter_2!='a' and mom_chapter_2!='b' and mom_chapter_2!='c':
                bad_3()
        if mom_chapter_1=='b':
            print('\n\nChapter 2: Grendel was forced to flee, fatally wounded, into the fen, seek a sorry abode; he knew quite surely that the end of his life had arrived, the sum of his days. (Beowulf 819-823)')
            print('You are enraged that your son, Grendel gets badly hurt by the Scylding army. You want to take revenge against them.')
            mom_chapter_2_revenge=input('\nDo you (a) ambush the Geats at night, (b) try to find Beowulf and the main Scylding army to attack them, (c) attack them during now (during the day), (d) take care of your son and not worry about the Scylding army for now, or (e) do nothing?')
            while mom_chapter_2_revenge=='b' and look_counter<2:
                print('\nYou try to find Beowulf and the main Scylding army but to no avail, they are nowhere to be seen. You sense that if you keep looking, you will fall into a trap of somekind.')
                look_counter+=1
                mom_chapter_2_revenge=input('\nDo you (a) ambush the Geats for revenge, (b) keep looking for the army that attacked your son, (c) attack the Geats for revenge at broad daylight, (d) take care of your son, or (e) do nothing?')
            while mom_chapter_2_revenge=='e' and revenge_son_counter<2:
                print('\n\nYou do nothing, which makes your son extremely angry at you. Although he is about to die, he still shakes you and tells you to help take revenge for him.')
                revenge_son_counter+=1
                mom_chapter_2_revenge=input('\nDo you (a) ambush the Geats at night to take revenge, (b) try to find Beowulf and the main army to attack, (c) attack the Geats in broad daylight, (d) ignore your son and try to help him instead, or (e) ignore him altogether and continue to do nothing?')
            if mom_chapter_2_revenge=='a':
                print("\n\nChapter 3: [A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge, as it may seem to many a thane whose spirit groans for his treasure-giver, a hard heart's distress (Beowulf 1339-1343)")
                print('You successfully avenge your son by attacking the Geats at night, though Beowulf and his army find your actions going too far. They may come and attack for going too far in your revenge schemes.')
                mom_chapter_3_ambush=input('\nDo you (a) prepare for the ensuing battle, (b) wait for them in your lair, or (c) try to run away?')
                if mom_chapter_3_ambush=='a':
                    print('\n\nChapter 4: As you prepare for the ensuing battle, you gear up for battle. Quickly, Beowulf arrives at your lair.')
                    mom_chapter_4_prepare=input('\nDo you (a) fight Beowulf or (b) try to run away?')
                    if mom_chapter_4_prepare=='a':
                        prepare_luck=random.randrange(0,5)
                        if prepare_luck>3:
                            print('\n\nChapter 5: You successfully block all of the attacks that Beowulf throws at you, and you stab him to death.')
                            print('Congratulations! You have beaten the Beowulf adventure game! Play again to try to find all the ways to beat the game!')
                        if prepare_luck<=3:
                            print('\n\nChapter 5: Unfortunately, Beowulf finds a magical sword and stabs you with it. You lose.')
                    if mom_chapter_4_prepare=='b':
                        print('\n\nChapter 5: You try to run away, but unfortunately, Beowulf catches up to you, and stabs you. You lose.')
                if mom_chapter_3_ambush=='b':
                    print('\n\nChapter 4: You wait for Beowulf in your lair, and he arrives quickly. He ineffectively swings at you, and you block all his attacks. You notice that the sword on the floor of your lair can stab and kill you.')
                    mom_chapter_4_ambush_wait=input('\nDo you (a) move the sword away, (b) attack Beowulf, or (c) try to run away?')
                    if mom_chapter_4_ambush_wait=='a':
                        move_luck=random.randrange(0,59)
                        if move_luck>53:
                            print('\n\nChapter 5: Somehow, you successfully throw the sword far away, and Beowulf cannot get it. You end up stabbing Beowulf. You win!')
                        if move_luck<=53:
                            print('\n\nChapter 5: Unfortunately, you are not able to throw the sword far. Beowulf picks up the magical sword and stabs you. You lose.')
                    if mom_chapter_4_ambush_wait=='b':
                        print('\n\nChapter 5: You attack Beowulf, but he dodges it by a hair. He finds the magical sword on the floor and stabs you with it. You lose.')
                    if mom_chapter_4_ambush_wait=='c':
                        print('\n\nChapter 5: You try to run away, but get stabbed by Beowulf with the magical sword. You lose.')
                    elif mom_chapter_4_ambush_wait!='a' and mom_chapter_4_ambush_wait!='b' and mom_chapter_4_ambush_wait!='c':
                        bad_3()
                if mom_chapter_3_ambush=='c':
                    print('\n\nChapter 4: You try to run away, but unfortunately you are captured and beheaded by Beowulf. You lose.')
                elif mom_chapter_3_ambush!='a' and mom_chapter_3_ambush!='b' and mom_chapter_3_ambush!='c':
                    bad_3()            
            if mom_chapter_2_revenge=='b' and look_counter==2:
                print('\n\nChapter 3: You do not find the Scylding army, but instead fall into a trap that they made for you: a giant pit, big enough to contain a whole sea. They end up executing you for attempting to attack the army. You lose.')
            if mom_chapter_2_revenge=='c':
                print('\n\nChapter 3: You attack the Geats in broad daylight, which leads to your capture and arrest by the Geats. You end up getting executed for attacking the Geats. You lose.')
            if mom_chapter_2_revenge=='d':
                print('\n\nChapter 3: You take care of your son, who quickly passes away under your care. You feel crushed by the loss, and decide to take your own life. You lose.')
            if mom_chapter_2_revenge=='e' and revenge_son_counter==2:
                print('\n\nChapter 3: Your son is mad that you have not taken revenge, instead choosing to do nothing. He fights you, and somehow beats you, whacking you until you lose conciousness. You lose.')
                revenge_son_counter=0
            elif mom_chapter_2_revenge!='a' and mom_chapter_2_revenge!='b' and mom_chapter_2_revenge!='c' and mom_chapter_2_revenge!='d' and mom_chapter_2_revenge!='e':
                print('\n\nPlease choose a, b, c, d, or e! Because you did not choose a, b, c, d, or e, this attempt is cancelled.')
        if mom_chapter_1!='a' and mom_chapter_1!='b':
            bad_2()
    elif character_choice=='c':
        print('\nYou have selected Beowulf as your main character!')
        print('\nChapter 1(background): You, Beowulf, have defeated many enemies, and is a celebrated war hero. You celebrate your many victories, as a bold demon waits in darkness, his name is Grendel.')
        print('\n\nChapter 2: So he [Grendel] ruled, and strove against right, one against all, until empty stood the best of houses. And so it was for a great while-for twelve long winters the lord of the Scyldings suffered his grief (Beowulf 144-148)')
        print('Grendel has terrorized this town for 12 long years, and you want to do something about it.')
        beowulf_chapter_1=input('\nDo you (a) sail the sea to tell your enemy and neighboring tribe, the Danes, about your mission, (b) try to solving this problem and kill Grendel by yourself, or (c) cower in fear? ')
        if beowulf_chapter_1=='a':
            print('\n\nChapter 3: He commanded to be made a good wave-crosser, said that he would seek out that war-king over the swans-riding, the renowned prince who was in need of men. (Beowulf 198-201)')
            print('You find Hrothgar, who commands you by asking for your lineage. "Now I must know your lineage, lest you go hence as false spies, travel further into Danish territory. Now, you sea-travelers from a far-off land, listen to my simple thought- the sooner the better, you must make clear from whence you came from." (Beowulf 251-257)')
            beowulf_chapter_2_help=input('\nDo you (a) listen to his request, (b) denounce his threat, or (c) ignore his request altogether? ')
            while beowulf_chapter_2_help=='c' and warn_counter<3:
                print('\nYou ignore Hrothgar, who warns you again not to come further. If he needs to warn you more than a couple of times, it may end badly.')
                warn_counter+=1
                beowulf_chapter_2_help=input('\n\nDo you (a) listen to his request, (b) denounce his threat, or (c) continue to ignore his request? ')
            if beowulf_chapter_2_help=='a':
                print('\n\nChapter 4: You tell Hrothgar about your lineage, but explain that you are not here to fight, but instead here to end the common enemy, Grendel. ')
                print('Hrothgar praises your mission, but while Hrothgar asks you to enjoy a drink with him, an annoying servant of Hrothgar, Unferth asks if you were the one who lost a swimming competition.')
                print('He says that if you were not even able to win the competition, you surely could not slay Grendel. ')
                beowulf_chapter_3_help_nerves=input('\n Slowly, he gets more and more on your nerves. Do you (a) attack Unferth, (b) respond to Unferth, or (c) ignore Unferth? ')
                while beowulf_chapter_3_help_nerves=='c' and unferth_counter==0:
                    print('\n\nYou somehow ignore Unferth for the time being, but if you continue to ignore Unferth, your frustrations might be let out onto Unferth.')
                    unferth_counter+=1
                    beowulf_chapter_3_help_nerves=input('Do you (a) attack Unferth, (b) respond to Unferth, or (c) continue to ignore Unferth? ')
                if beowulf_chapter_3_help_nerves=='a':
                    print('\n\nChapter 5: You attack Unferth, despire pleas from Hrothgar to stop. Hrothgar ends up defending his servant, and your attacks ends in a bloody battle, where you are captured and executed. You lose.')
                if beowulf_chapter_3_help_nerves=='b':
                    print('\n\nChapter 5: You respond to Unferth by telling him what actually happened in the competition, telling him how you slayed the water beast while swimming. Unferth had nothing to respond, and you leave after Hrothgar thanks you for your bravery, and leaves you with some troops.')
                    beowulf_chapter_4_help=input('\nNow that you have returned home, do you (a) storm the lair of Grendel, (b) try to lure him out to the mead hall, or (c) wait for him outside his lair? ')                                     
                    if beowulf_chapter_4_help=='a':
                        print('\n\nChapter 6: You storm into the lair of Grendel, who gets distracted trying to defend himself from your army. He gets distracted from attacking your army, and you have an opportunity to attack him.')
                        beowulf_chapter_5_help=input('\nDo you (a) try to rip off his arm, (b) try to kick him, or (c) try to run away? ')
                        if beowulf_chapter_5_help=='a':
                            rip=random.randrange(0,9)
                            if rip<2:
                                print('\n\nChapter 7: [T]he courageous kinsman of Hygelac had him in hand-hateful to each was the life of the other. The loathsome creature felt a great pain in his body; a gaping wound opened in his shoulder-joint (Beowulf 814-817)')
                                print('You successfully rip off the arm of Grendel! As he runs away, you celebrate your victory back at in the mead-hall, and you are showered by gifts from the Scylding citizens.')
                                print("\n\nChapter 8: [A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge, as it may seem to many a thane whose spirit groans for his treasure-giver, a hard heart's distress (Beowulf 1339-1343)")
                                print('You successfully avenge your son by attacking the Geats at night, though Beowulf and his army find your actions going too far. They may come and attack for going too far in your revenge schemes.')
                                beowulf_chapter_6_help=input('\nDo you (a) prepare to slay the mother of Grendel, (b) cower in fear, or (c) do nothing about it? ')
                                if beowulf_chapter_6_help=='a':
                                    print('\n\nChapter 9: You prepare to slay the mother of Grendel by getting some of the strongest weapons and armour: a strong chainmail suit, a poison-striped sword, and more.')
                                    beowulf_chapter_7_help=input('\nNow that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory?')
                                    while beowulf_chapter_7_help=='b' and victory_wait_counter==0:
                                        print('\n\nYou wait for her to come out of her lair but she never does.........')
                                        victory_wait_counter+=1
                                        beowulf_chapter_7_help=input('\nDo you (a) swim to her lair, (b) keep waiting onshore for her to come out, or (c) return back home and lie about a victory? ')
                                    if beowulf_chapter_7_help=='a':
                                        print('\n\nChapter 10: [H]e gave a mighty blow with his battle-sword - he did not temper that stroke - so that the ring-etched blade rang out on her head a greedy battle-song. The guest discovered then that the battle-flame would not bite, or wound her fatally......It was the first time that the fame of that precious treasure had failed (Beowulf 1519-1524, & 1527-1528)')
                                        print("You swim to Grendel's mom's lair. You try to use your sword against her, but it is ineffective. She wrestles you to the ground and pulls out her knife.")
                                        beowulf_chapter_8_help=input("\nYour life is flashing before your eyes, do you (a) try to run away, (b) try to fight back using your bare hands, or (c) try to find something else to fight Grendel's mother with")
                                        if beowulf_chapter_8_help=='a':
                                            print('\n\nChapter 11: You try to run away, but soon you are captured and choked by the mother of Grendel. You lose.')
                                        if beowulf_chapter_8_help=='b':
                                            print("\n\nChapter 11: You try to fight Grendel's mom with your bare hands, but you are quickly defeated in battle. You lose.")
                                        if beowulf_chapter_8_help=='c':
                                            find_help_luck=random.randrange(0,9)
                                            if find_help_luck<8:
                                                print('\n\nChapter 11: He saw among the armor a victorious blade, ancient giant-sword strong in its edges, worthy in battles (Beowulf 1557-1560)')
                                                print("The Scyldings' champion seized its linked hilt, fierce and ferocious, drew the ring-marked sword despairing of his life, struck in fury so that it caught her hard in the neck, broke her bone-rings; the blade cut through the doomed flesh- she fell to the floor, the sword was bloody, the soldier rejoiced (Beowulf 1563-1569)")
                                                print("\nYou try to find something to attack Grendel's mom with, and you find a sword on her lair! You stab her with it, and successfully defeat Grendel's mom!")
                                                print('\n\nChapter 12: You celebrate another great victory, and Hrothgar visits you again. He showers you with even more gifts, even building some statues and buildings for you. You make peace with the Danes because of your victories.')
                                                print('\nChapter 13: He [Beowulf] held it well for fifty winters- he was then a wise king, old guarding of his homeland- until in the dark nights a dragon began his reign (Beowulf 2209-2211).') 
                                                print('You rule for 50 years, but unfortunately, a pesky thief wakes up and annoys a sleeping dragon, who terrorizes your town.')
                                                beowulf_chapter_9_help=input('Because you are extremely old now, you are advised to do nothing about the dragon, and hope it just disappears. Do you (a) listen to the advice and do nothing about the dragon or (b) prepare to attack the dragon? ')
                                                if beowulf_chapter_9_help=='a':
                                                    print('Chapter 14: You do nothing, which causes the dragon to burn down your town and country. You lose.')
                                                if beowulf_chapter_9_help=='b':                                            
                                                    beowulf_chapter_10_help=input('Chapter 14: You prepare to attack the dragon by gathering up all your equipment. Now do you (a) attack the dragon by storming the lair or (b) wait for the dragon to come out of the lair? ')
                                                    if beowulf_chapter_10_help=='a':
                                                        print("Chapter 15: You attack the dragon by storming the lair. But unfortunately, the dragon heard about the legend of you storming into Grendel's lair and expected you to storm in. The dragon quickly smashes the cave walls, causing the cave to crush you and your army. You lose.")
                                                    if beowulf_chapter_10_help=='b':
                                                        print('Chapter 15: You wait for the dragon, but the dragon never comes out. You and your army quickly starves to death. You lose.')
                                                    elif beowulf_chapter_10_help!='a' and beowulf_chapter_10_help!='b':
                                                        bad_2()     
                                                elif beowulf_chapter_9_help!='a' and beowulf_chapter_9_help!='b':
                                                    bad_2()
                                            if find_help_luck>=8:
                                                print("\n\nChapter 11: You try to find something to attack Grendel's mom with, but you can't find anything. Instead, you are quickly defeated. You lose.")
                                        elif beowulf_chapter_8_help!='a' and beowulf_chapter_8_help!='b' and beowulf_chapter_8_help!='c':
                                            bad_3()                                    
                                    if beowulf_chapter_7_help=='b' and victory_wait_counter==1:
                                        print('\n\nChapter 10: You wait for too long, and the people rebel against you. Quickly, you are executed. You lose.')
                                    if beowulf_chapter_7_help=='c':
                                        print('\n\nChapter 10: When you are lying about your victory, someone spots the mother of Grendel, who finds you and eats you. You lose.')
                                    elif beowulf_chapter_7_help!='a' and beowulf_chapter_7_help!='b' and beowulf_chapter_7_help!='c':
                                        bad_3()
                                if beowulf_chapter_6_help=='b':
                                    print('\n\nChapter 9: You cower in fear, which causes doubt amongst your population that you can lead. It leads to a rebellion and your execution. You lose.')
                                if beowulf_chapter_6_help=='c':
                                    print('\n\nChapter 9: You do nothing about the chaos done, which leads to the people hating you. Quickly, you are dethroned and executed. You lose.')
                                elif beowulf_chapter_6_help!='a' and beowulf_chapter_6_help!='b' and beowulf_chapter_6_help!='c':
                                    bad_3()
                            if rip>=2:
                                print('\n\nChapter 7: You unsuccessfully try to rip off the arm of Grendel, instead getting pushed away by Grendel, and knocked to the ground. You lose!')                
                        if beowulf_chapter_5_help=='b':
                            kick=random.randrange(0,4)
                            if kick<3:
                                print('\n\nChapter 7: You successfully kick Grendel in the chest, causing his chest to collapse! As he crawls away, you return back to the mead-hall as a hero and a legend, and you are showered by gifts from the Scylding citizens.')
                                print("\n\nChapter 8: [A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge, as it may seem to many a thane whose spirit groans for his treasure-giver, a hard heart's distress (Beowulf 1339-1343)")
                                print('You successfully avenge your son by attacking the Geats at night, though Beowulf and his army find your actions going too far. They may come and attack for going too far in your revenge schemes.')
                                beowulf_chapter_6_help_kick=input('\nDo you (a) prepare to slay the mother of Grendel, (b) cower in fear, or (c) do nothing about it? ')
                                if beowulf_chapter_6_help_kick=='a':
                                    print('\n\nChapter 9: You prepare to slay the mother of Grendel by getting some of the strongest weapons and armour: an underwater suit, a poison-striped sword, and more.')
                                    beowulf_chapter_7_help_kick=input('\nNow that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory? ')
                                    while beowulf_chapter_7_help_kick=='b' and victory_wait_counter==0:
                                        print('\n\nYou wait for her to come out of her lair but she never does.........')
                                        victory_wait_counter+=1
                                        beowulf_chapter_7_help_kick=input('\nDo you (a) swim to her lair, (b) keep waiting onshore for her to come out, or (c) return back home and lie about a victory? ')
                                    if beowulf_chapter_7_help_kick=='a':
                                        print("\n\nChapter 10: You swim to Grendel's mom's lair. You try to use your sword against her, but it is ineffective, especially because of the armor she is wearing. She starts grabbing you and preparing to stab you.")
                                        beowulf_chapter_8_help_kick=input("\nYour life is flashing before your eyes, do you (a) try to run away, (b) try to fight back using your bare hands, or (c) try to find something else to fight Grendel's mother with? ")
                                        if beowulf_chapter_8_help_kick=='a':
                                            print('\n\nChapter 11: You try to run away, but soon you are captured and choked by the mother of Grendel. You lose.')
                                        if beowulf_chapter_8_help_kick=='b':
                                            print("\n\nChapter 11: You try to fight Grendel's mom with your bare hands, but you are quickly defeated in battle. You lose.")
                                        if beowulf_chapter_8_help_kick=='c':
                                            find_luck=random.randrange(0,9)
                                            if find_luck<6:
                                                print("\n\nChapter 11: You try to find something to attack Grendel's mom with, and you find another sword on her lair floor! You stab her with it, but unfortunately it doesn't work. Since you defeated Grendel with a kick, she brought armor to protect herself against a kick. When you stab her, her armor protects her. She uses the opportunity to stab you. You lose.")                           
                                            if find_luck>=6:
                                                print("\n\nChapter 11: You try to find something to attack Grendel's mom with, but you can't find anything. Instead, you are quickly defeated. You lose.")
                                        elif beowulf_chapter_8_help_kick!='a' and beowulf_chapter_8_help_kick!='b' and beowulf_chapter_8_help_kick!='c':
                                            bad_3()                                    
                                    if beowulf_chapter_7_help_kick=='b' and victory_wait_counter==1:
                                        print('\n\nChapter 10: You wait for too long, and the people rebel against you. Quickly, you are executed. You lose.')
                                    if beowulf_chapter_7_help_kick=='c':
                                        print('\n\nChapter 10: When you are lying about your victory, someone spots the mother of Grendel, who finds you and eats you. You lose.')
                                    elif beowulf_chapter_7_help_kick!='a' and beowulf_chapter_7_help_kick!='b' and beowulf_chapter_5_no_help_kick_prepare!='c':
                                        bad_3()
                                if beowulf_chapter_6_help_kick=='b':
                                    print('Chapter 9: You cower in fear, which causes distrust among the Scylding citizens. They rebel against you. You are quickly executed. You lose.')
                                if beowulf_chapter_6_help_kick=='c':
                                    print('Chapter 9: You do nothing about the mother of Grendel, who keeps eating people, causing the Scylding citizens to rebel against you. You lose.')
                            if kick>=3:
                                print('\n\nChapter 7: As you try to kick Grendel in the chest, he blocks your kick and throws you to the ground. You lose.')
                        if beowulf_chapter_5_help=='c':
                            escape=random.randrange(0,2)
                            if escape<2:
                                print('\n\nChapter 7: You successfully escape the cave, but when the Scylding people find out that you are a coward, you are overthrown and executed. You lose.')
                            if escape==2:
                                print('\n\nChapter 7: You unsuccessfully leave the cave, as Grendel grabs you and eats you. You lose.')
                        elif beowulf_chapter_5_help!='a' and beowulf_chapter_5_help!='b' and beowulf_chapter_5_help!='c':
                            bad_3()
                    if beowulf_chapter_4_help=='b':
                        print('\n\nChapter 6: Then from the moor, in a blanket of mist, Grendel came stalking-he bore the anger of God; the evil marauder meant to ensnare some of human-kind in that high hall. (Beowulf 710-714)')
                        print('You successfully lure Grendel to the mead hall, and distract him with your army. You have an opportunity to attack him.')
                        beowulf_chapter_5_help_lure=input('\nDo you (a) try to rip off his arm, (b) try to tackle him to the ground, or (c) try to escape? ')
                        if beowulf_chapter_5_help_lure=='a':
                            rip_lure=random.randrange(0,7)
                            if rip_lure<5:
                                print('\n\nChapter 7: [T]he courageous kinsman of Hygelac had him in hand-hateful to each was the life of the other. The loathsome creature felt a great pain in his body; a gaping wound opened in his shoulder-joint (Beowulf 814-817)')
                                print('You successfully rip off the arm of Grendel! As he runs away, you celebrate your victory back at in the mead-hall, and you are showered by gifts from the Scylding citizens.')
                                print('\n\nChapter 8: After your victory, news spreads across the country, even Hrothgar, from the Danes, comes and gives you gifts!')
                                print ('[A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge (Beowulf 1339-1341)')
                                print('But soon, the celebrations are cut short. The mother of Grendel breaks into the mead hall and causing trouble, so Hrothgar comes to invite you to defeat her. He offers bountiful treasures to slay the mother of Grendel.')
                                beowulf_chapter_6_help_lure=input('\nDo you (a) prepare to slay the mother of Grendel, (b) cower in fear, or (c) do nothing about it? ')
                                if beowulf_chapter_6_help_lure=='a':
                                    print('Chapter 9: You prepare to slay the mother of Grendel by getting some of the strongest weapons and armour: an underwater suit, a poison-striped sword, and more.')
                                    beowulf_chapter_7_help_lure=input('\nNow that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory? ')
                                    while beowulf_chapter_7_help_lure=='b' and victory_wait_counter==0:
                                        print('\n\nYou wait for her to come out of her lair but she never does.........')
                                        victory_wait_counter+=1
                                        beowulf_chapter_7_help_lure=input('\nDo you (a) swim to her lair, (b) keep waiting onshore for her to come out, or (c) return back home and lie about a victory? ')
                                    if beowulf_chapter_7_help_lure=='a':
                                        print("\n\nChapter 10: You swim to Grendel's mom's lair.")
                                        print('[H]e gave a mighty blow with his battle-sword - he did not temper that stroke - so that the ring-etched blade rang out on her head a greedy battle-song. The guest discovered then that the battle-flame would not bite, or wound her fatally......It was the first time that the fame of that precious treasure had failed (Beowulf 1519-1524, & 1527-1528)')
                                        print("You try to use your sword against her, but it is ineffective. She starts grabbing you and choking you.")
                                        beowulf_chapter_8_help_lure=input("\nYour life is flashing before your eyes, do you (a) try to run away, (b) try to fight back using your bare hands, or (c) try to find something else to fight Grendel's mother with")
                                        if beowulf_chapter_8_help_lure=='a':
                                            print('\n\nChapter 11: You try to run away, but soon you are captured and choked by the mother of Grendel. You lose.')
                                        if beowulf_chapter_8_help_lure=='b':
                                            print("\n\nChapter 11: You try to fight Grendel's mom with your bare hands, but you are quickly defeated in battle. You lose.")
                                        if beowulf_chapter_8_help_lure=='c':
                                            find_luck=random.randrange(0,9)
                                            if find_luck<6:
                                                print('\n\nChapter 11: He saw among the armor a victorious blade, ancient giant-sword strong in its edges, worthy in battles (Beowulf 1557-1560)')
                                                print("The Scyldings' champion seized its linked hilt, fierce and ferocious, drew the ring-marked sword despairing of his life, struck in fury so that it caught her hard in the neck, broke her bone-rings; the blade cut through the doomed flesh- she fell to the floor, the sword was bloody, the soldier rejoiced (Beowulf 1563-1569)")
                                                print("\nYou try to find something to attack Grendel's mom with, and you find a sword on her lair! You stab her with it, and successfully defeat Grendel's mom!")
                                                print('\n\nChapter 12: You celebrate another great victory, and Hrothgar visits you again. He showers you with even more gifts, even building some statues and buildings for you. You make peace with the Danes because of your victories.')
                                                print('\nChapter 13: He [Beowulf] held it well for fifty winters- he was then a wise king, old guarding of his homeland- until in the dark nights a dragon began his reign (Beowulf 2209-2211).') 
                                                print('You rule for 50 years, but unfortunately, a pesky thief wakes up and annoys a sleeping dragon, who terrorizes your town.')
                                                beowulf_chapter_9_help_lure=input('\nBecause you are extremely old now, you are advised not to attack the dragon, instead hoping it disappears. Do you (a) listen to the advice and do nothing about the dragon or (b) prepare to attack the dragon?')
                                                if beowulf_chapter_9_help_lure=='a':
                                                    print('\n\nChapter 14: You do nothing, which causes the dragon to burn down your town and country. You lose.')
                                                if beowulf_chapter_9_help_lure=='b':  
                                                    beowulf_chapter_10_help_lure=input('\nChapter 15: You prepare to attack the dragon by gathering up all your equipment, including a fire-resistant shield. Now do you (a) attack the dragon by storming the lair or (b) wait for the dragon to come out of the lair?')                                       
                                                    if beowulf_chapter_10_help_lure=='a':
                                                        print("\n\nChapter 16: The good war-king had drawn his sword, its edges undulled, an ancient heirloom; each of the two hostile ones stood in horror of the other. (Beowulf 2562-2565)")
                                                        print("You storm the lair of the dragon, and meet the dragon standing directly opposite to you.")
                                                        beowulf_chapter_11_help=input('\nDo you (a) hold your shield up as you charge towards the dragon, (b) wait for the dragon to charge towards you, or (c) try to run away?')
                                                        if beowulf_chapter_11_help=='a':
                                                            print('\n\nChapter 17: You hold up your shield as you charge towards the dragon, but the dragon somehow burns you in an unprotected spot, causing you to burn to death. You lose.')
                                                        if beowulf_chapter_11_help=='b':
                                                            print("\n\nChapter 17: You block the dragon's flames with your shield. But when you try to counter by stabbing the dragon with your iron sword, it fails to do much. Suddenly, one of your fellow soldiers, joins to help you fight the dragon. Unfortunately, he does not have a fire-proof shield, and could easily get burned to a crisp.")
                                                            beowulf_chapter_12_help=input('\nAs the dragon charges towards you again, do you (a) tell your friend to move while you fight the dragon, (b) allow your friend to fight as you stab the dragon with your sword, (c) allow your friend to fight as you try to use your poison dagger to stab the dragon?')
                                                            if beowulf_chapter_12_help=='a':
                                                                print('As you get distracted telling your friend to move, the dragon charges at you, and burns you to a crisp. You lose.')
                                                            if beowulf_chapter_12_help=='b':
                                                                print("You allow your friend to work together with you to attack the dragon. The dragon gets distracted while fighting the two of you, which allows you to land a critical hit at the dragon's skull. Unfortunately, the dragon bites you in the neck after burning through your friend's shield.")
                                                                beowulf_chapter_13_help=input('As you approach your death, do you (a) accept your death, (b) try to fight back with your sword, or (c) try to fight back with your poison dagger.')
                                                                if beowulf_chapter_13_help=='a':
                                                                    print('You accept your death, which allows the dragon to easily beat your army and burn down your country. You lose.')
                                                                if beowulf_chapter_13_help=='b':
                                                                    print('You try to fight back with your iron sword, but it does not affect the dragon. The dragon survives the encounter and easily beats your army and burns down your country. You lose.')
                                                                if beowulf_chapter_13_help=='c':
                                                                    print('You fight back with your poison dagger, killing the dragon with your poison. You are honored by the Scylding citizens after your death, and your legacy lives on.')
                                                                    print('While you did not find the best ending, you still win! Try again to find all the ways to beat the game!')
                                                                elif beowulf_chapter_13_help!='a' and beowulf_chapter_13_help!='b' and beowulf_chapter_13_help!='c':
                                                                    bad_3()
                                                            if beowulf_chapter_12_help=='c':
                                                                print('\n\nAs the dragon gets distracted and attacks your friend, you slide beneath the dragon and stab the dragon in his midsection. Slowly, he dies from the poison.')
                                                                print('Everyone celebrates your victory and you leave behind a legendary legacy. Congratulations! You have owned up to the task, and beaten Beowulf the Adventure Game! Try again, and find all the ways to beat the game!')
                                                            elif beowulf_chapter_12_help!='a' and beowulf_chapter_12_help!='b' and beowulf_chapter_12_help!='c':
                                                                bad_3()
                                                        if beowulf_chapter_11_help=='c':
                                                            print('\n\nChapter 17: You try to run away, but the dragon burns you to a crisp as you try to run. You lose.')
                                                        elif beowulf_chapter_11_help!='a' and beowulf_chapter_11_help!='b' and beowulf_chapter_11_help!='c':
                                                            bad_3()
                                                    if beowulf_chapter_10_help_lure=='b':
                                                        print('Chapter 16: You wait for the dragon, but the dragon never comes out. You and your army quickly starves to death. You lose.')
                                                    elif beowulf_chapter_10_help_lure!='a' and beowulf_chapter_10_help_lure!='b':
                                                        bad_2()     
                                                elif beowulf_chapter_9_help_lure!='a' and beowulf_chapter_9_help_lure!='b':
                                                    bad_2()                              
                                            if find_luck>=6:
                                                print("\n\nChapter 11: You try to find something to attack Grendel's mom with, but you can't find anything. Instead, you are quickly defeated. You lose.")
                                        elif beowulf_chapter_8_help_lure!='a' and beowulf_chapter_8_help_lure!='b' and beowulf_chapter_8_help_lure!='c':
                                            bad_3()                                    
                                    if beowulf_chapter_7_help_lure=='b' and victory_wait_counter==1:
                                        print('\n\nChapter 10: You wait for too long, and the people rebel against you. Quickly, you are executed. You lose.')
                                    if beowulf_chapter_7_help_lure=='c':
                                        print('\n\nChapter 10: When you are lying about your victory, someone spots the mother of Grendel, who finds you and eats you. You lose.')
                                    elif beowulf_chapter_7_help_lure!='a' and beowulf_chapter_7_help_lure!='b' and beowulf_chapter_7_help_lure!='c':
                                        bad_3()
                                if beowulf_chapter_6_help_lure=='b':
                                    print('\n\nChapter 9: You cower in fear, which causes doubt amongst your population that you can lead. It leads to a rebellion and your execution. You lose.')
                                if beowulf_chapter_6_help_lure=='c':
                                    print('\n\nChapter 9: You do nothing about the chaos done, which leads to the people hating you. Quickly, you are dethroned and executed. You lose.')
                                elif beowulf_chapter_6_help_lure!='a' and beowulf_chapter_6_help_lure!='b' and beowulf_chapter_6_help_lure!='c':
                                    bad_3() 
                            if rip_lure>=5:
                                print('\n\nChapter 7: You unsuccesfully leap at Grendel, trying to rip off his arm. Instead, he swats you away, and you fall to your doom. You lose.')
                        if beowulf_chapter_5_help_lure=='b':                    
                            print('\n\nChapter 7: You try to tackle Grendel to the floor, but he is too big. Instead, when you lean towards him, he crushes you to the ground. You lose.')
                        if beowulf_chapter_5_help_lure=='c':
                            escape=random.randrange(0,4)
                            if escape<=1:
                                print('\n\nChapter 7: You successfully escape Grendel, but when the Scylding people find you that you ran from battle, you are executed. You lose.')
                            if escape==2:
                                print('\n\nChapter 7: As you try to escape, Grendel throws a massive boulder at you, crushing you underneath it. You lose.')
                            if escape>2:
                                print('\n\nChapter 7: While you try to run away, Grendel grabs you and eats you. You lose.')
                        elif beowulf_chapter_5_help_lure!='a' and beowulf_chapter_5_help_lure!='b' and beowulf_chapter_5_help_lure!='c':
                            bad_3()                    
                    while beowulf_chapter_4_help=='c' and wait_help_counter<2:
                        print('\n\nYou wait for him to come out but he never shows.......')
                        wait_help_counter+=1
                        beowulf_chapter_4_help=input('\nDo you (a) storm into the lair of Grendel, (b) try to lure him out, or (c) continue to wait for him')               
                    if beowulf_chapter_4_help=='c' and wait_help_counter==2:
                        print('\n\nChapter 6: You keep waiting. Slowly, you and your troops starve to death. You lose.')
                    if beowulf_chapter_4_help!='a' and beowulf_chapter_4_help!='b' and beowulf_chapter_4_help!='c':
                        bad_3()
                if beowulf_chapter_3_help_nerves=='c' and unferth_counter==1:
                    print("Chapter 5: You cannot control your anger towards Unferth's annoying remarks. You attack Unferth, which ends in a bloody battle after Hrothgar defends Unferth. You lose.")                       
            if beowulf_chapter_2_help=='b':
                print('\n\nChapter 4: You denounce Hrothgar, which causes him to attack you. It ends in a bloody battle, where all your men are killed. Quickly, you lose popularity and get dethroned. You lose.')
            if beowulf_chapter_2_help=='c' and warn_counter==3:
                print('\nChapter 4: Hrothgar warned you, and this is the final straw. His troops come to attack you, and you are defeated in battle. You lose!')
            if beowulf_chapter_2_help!='a' and beowulf_chapter_2_help!='b' and beowulf_chapter_2_help!='c':
                bad_3()
        if beowulf_chapter_1=='b':
            print('\n\nChapter 3: You try to solve the problem on your own, by summoning your own army without help from the Danes. You want to attack him now, but how?')
            beowulf_chapter_2=input('\nDo you (a) storm into the lair of Grendel, (b) try to lure him out to the mead hall, or (c) wait for him outside his lair?')
            while beowulf_chapter_2=='c' and wait_counter<2:
                print('\n\nYou wait for him to come out but he never shows.......')
                wait_counter+=1
                beowulf_chapter_2=input('\nDo you (a) storm into the lair of Grendel, (b) try to lure him out, or (c) continue to wait for him? ')
            if beowulf_chapter_2=='a':
                print('\n\nChapter 4: You storm into the lair of Grendel, who gets distracted trying to defend himself from your army. He gets distracted from attacking your army, and you have an opportunity to attack him.')
                beowulf_chapter_3_lair=input('\nDo you (a) try to rip off his arm, (b) try to kick him, or (c) try to run away?')
                if beowulf_chapter_3_lair=='a':
                    rip=random.randrange(0,9)
                    if rip<2:
                        print('\n\nChapter 5: [T]he courageous kinsman of Hygelac had him in hand-hateful to each was the life of the other. The loathsome creature felt a great pain in his body; a gaping wound opened in his shoulder-joint (Beowulf 814-817)')
                        print('You successfully rip off the arm of Grendel! As he runs away, you celebrate your victory back at in the mead-hall, and you are showered by gifts from the Scylding citizens.')
                        print("\n\nChapter 6: [A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge, as it may seem to many a thane whose spirit groans for his treasure-giver, a hard heart's distress (Beowulf 1339-1343)")
                        print('You successfully avenge your son by attacking the Geats at night, though Beowulf and his army find your actions going too far. They may come and attack for going too far in your revenge schemes.')
                        beowulf_chapter_4_no_help_rip=input('\nDo you (a) prepare to slay the mother of Grendel, (b) cower in fear, or (c) do nothing about it? ')
                        if beowulf_chapter_4_no_help_rip=='a':
                            print('\n\nChapter 7: You prepare to slay the mother of Grendel by getting some of the strongest weapons and armour: a strong chainmail suit, a poison-striped sword, and more.')
                            beowulf_chapter_5_no_help_rip_prepare=input('\nNow that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory?')
                            while beowulf_chapter_5_no_help_rip_prepare=='b' and victory_wait_counter==0:
                                print('\n\nYou wait for her to come out of her lair but she never does.........')
                                victory_wait_counter+=1
                                beowulf_chapter_5_no_help_rip_prepare=input('\nDo you (a) swim to her lair, (b) keep waiting onshore for her to come out, or (c) return back home and lie about a victory?')
                            if beowulf_chapter_5_no_help_rip_prepare=='a':
                                print('\n\nChapter 8: [H]e gave a mighty blow with his battle-sword - he did not temper that stroke - so that the ring-etched blade rang out on her head a greedy battle-song. The guest discovered then that the battle-flame would not bite, or wound her fatally......It was the first time that the fame of that precious treasure had failed (Beowulf 1519-1524, & 1527-1528)')
                                print("You swim to Grendel's mom's lair. You try to use your sword against her, but it is ineffective. She wrestles you to the ground and pulls out her knife.")
                                beowulf_chapter_6_swim=input("\nYour life is flashing before your eyes, do you (a) try to run away, (b) try to fight back using your bare hands, or (c) try to find something else to fight Grendel's mother with")
                                if beowulf_chapter_6_swim=='a':
                                    print('\n\nChapter 9: You try to run away, but soon you are captured and choked by the mother of Grendel. You lose.')
                                if beowulf_chapter_6_swim=='b':
                                    print("\n\nChapter 9: You try to fight Grendel's mom with your bare hands, but you are quickly defeated in battle. You lose.")
                                if beowulf_chapter_6_swim=='c':
                                    find_luck=random.randrange(0,9)
                                    if find_luck<6:
                                        print('\n\nChapter 9: He saw among the armor a victorious blade, ancient giant-sword strong in its edges, worthy in battles (Beowulf 1557-1560)')
                                        print("The Scyldings' champion seized its linked hilt, fierce and ferocious, drew the ring-marked sword despairing of his life, struck in fury so that it caught her hard in the neck, broke her bone-rings; the blade cut through the doomed flesh- she fell to the floor, the sword was bloody, the soldier rejoiced (Beowulf 1563-1569)")
                                        print("\nYou try to find something to attack Grendel's mom with, and you find a sword on her lair! You stab her with it, and successfully defeat Grendel's mom!")
                                        print('\n\nChapter 10: You celebrate another great victory, and Hrothgar visits you again. He showers you with even more gifts, even building some statues and buildings for you. You make peace with the Danes because of your victories.')
                                        print('\nChapter 11: He [Beowulf] held it well for fifty winters- he was then a wise king, old guarding of his homeland- until in the dark nights a dragon began his reign (Beowulf 2209-2211).') 
                                        print('You rule for 50 years, but unfortunately, a pesky thief wakes up and annoys a sleeping dragon, who terrorizes your town.')
                                        beowulf_chapter_7_no_help_rip_prepare_swim=input('Because you are extremely old now, you are advised to do nothing about the dragon, and hope it just disappears. Do you (a) listen to the advice and do nothing about the dragon or (b) prepare to attack the dragon?')
                                        if beowulf_chapter_7_no_help_rip_prepare_swim=='a':
                                            print('Chapter 12: You do nothing, which causes the dragon to burn down your town and country. You lose.')
                                        if beowulf_chapter_7_no_help_rip_prepare_swim=='b':                                            
                                            beowulf_chapter_8_no_help_prepare=input('Chapter 12: You prepare to attack the dragon by gathering up all your equipment. Now do you (a) attack the dragon by storming the lair or (b) wait for the dragon to come out of the lair?')
                                            if beowulf_chapter_8_no_help_prepare=='a':
                                                print("Chapter 13: You attack the dragon by storming the lair. But unfortunately, the dragon heard about the legend of you storming into Grendel's lair and expected you to storm in. The dragon quickly smashes the cave walls, causing the cave to crush you and your army. You lose.")
                                            if beowulf_chapter_8_no_help_prepare=='b':
                                                print('Chapter 13: You wait for the dragon, but the dragon never comes out. You and your army quickly starves to death. You lose.')
                                            elif beowulf_chapter_8_no_help_prepare!='a' and beowulf_chapter_8_no_help_prepare!='b':
                                                bad_2()     
                                        elif beowulf_chapter_7_no_help_rip_prepare_swim!='a' and beowulf_chapter_7_no_help_rip_prepare_swim!='b':
                                            bad_2()
                                    if find_luck>=6:
                                        print("\n\nChapter 9: You try to find something to attack Grendel's mom with, but you can't find anything. Instead, you are quickly defeated. You lose.")
                                elif beowulf_chapter_6_swim!='a' and beowulf_chapter_6_swim!='b' and beowulf_chapter_6_swim!='c':
                                    bad_3()                            
                            if beowulf_chapter_5_no_help_rip_prepare=='b' and victory_wait_counter==1:
                                print('\n\nChapter 8: You wait for too long, and the people rebel against you. Quickly, you are executed. You lose.')
                            if beowulf_chapter_5_no_help_rip_prepare=='c':
                                print('\n\nChapter 8: When you are lying about your victory, someone spots the mother of Grendel, who finds you and eats you. You lose.')
                            elif beowulf_chapter_5_no_help_rip_prepare!='a' and beowulf_chapter_5_no_help_rip_prepare!='b' and beowulf_chapter_5_no_help_rip_prepare!='c':
                                bad_3()
                        if beowulf_chapter_4_no_help_rip=='b':
                            print('\n\nChapter 7: You cower in fear, which causes doubt amongst your population that you can lead. It leads to a rebellion and your execution. You lose.')
                        if beowulf_chapter_4_no_help_rip=='c':
                            print('\n\nChapter 7: You do nothing about the chaos done, which leads to the people hating you. Quickly, you are dethroned and executed. You lose.')
                        elif beowulf_chapter_4_no_help_rip!='a' and beowulf_chapter_4_no_help_rip!='b' and beowulf_chapter_4_no_help_rip!='c':
                            bad_3()
                    if rip>=2:
                        print('\n\nChapter 5: You unsuccessfully try to rip off the arm of Grendel, instead getting pushed away by Grendel, and knocked to the ground. You lose!')                
                if beowulf_chapter_3_lair=='b':
                    kick=random.randrange(0,4)
                    if kick<2:
                        print('\n\nChapter 5: You successfully kick Grendel in the chest, causing his chest to collapse! As he crawls away, you return back to the mead-hall as a hero and a legend, and you are showered by gifts from the Scylding citizens.')
                        print("\n\nChapter 6: [A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge, as it may seem to many a thane whose spirit groans for his treasure-giver, a hard heart's distress (Beowulf 1339-1343)")
                        print('You successfully avenge your son by attacking the Geats at night, though Beowulf and his army find your actions going too far. They may come and attack for going too far in your revenge schemes.')
                        beowulf_chapter_4_no_help_kick=input('\nDo you (a) prepare to slay the mother of Grendel, (b) cower in fear, or (c) do nothing about it? ')
                        if beowulf_chapter_4_no_help_kick=='a':
                            print('\n\nChapter 7: You prepare to slay the mother of Grendel by getting some of the strongest weapons and armour: an underwater suit, a poison-striped sword, and more.')
                            beowulf_chapter_5_no_help_kick_prepare=input('\nNow that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory?')
                            while beowulf_chapter_5_no_help_kick_prepare=='b' and victory_wait_counter==0:
                                print('\n\nYou wait for her to come out of her lair but she never does.........')
                                victory_wait_counter+=1
                                beowulf_chapter_5_no_help_kick_prepare=input('\nDo you (a) swim to her lair, (b) keep waiting onshore for her to come out, or (c) return back home and lie about a victory?')
                            if beowulf_chapter_5_no_help_kick_prepare=='a':
                                print("\n\nChapter 8: You swim to Grendel's mom's lair. You try to use your sword against her, but it is ineffective, especially because of the armor she is wearing. She starts grabbing you and preparing to stab you.")
                                beowulf_chapter_6_kick_swim=input("\nYour life is flashing before your eyes, do you (a) try to run away, (b) try to fight back using your bare hands, or (c) try to find something else to fight Grendel's mother with")
                                if beowulf_chapter_6_kick_swim=='a':
                                    print('\n\nChapter 9: You try to run away, but soon you are captured and choked by the mother of Grendel. You lose.')
                                if beowulf_chapter_6_kick_swim=='b':
                                    print("\n\nChapter 9: You try to fight Grendel's mom with your bare hands, but you are quickly defeated in battle. You lose.")
                                if beowulf_chapter_6_kick_swim=='c':
                                    find_luck=random.randrange(0,9)
                                    if find_luck<6:
                                        print("\n\nChapter 9: You try to find something to attack Grendel's mom with, and you find another sword on her lair floor! You stab her with it, but unfortunately it doesn't work. Since you defeated Grendel with a kick, she brought armor to protect herself against a kick. When you stab her, her armor protects her. She uses the opportunity to stab you. You lose.")                           
                                    if find_luck>=6:
                                        print("\n\nChapter 9: You try to find something to attack Grendel's mom with, but you can't find anything. Instead, you are quickly defeated. You lose.")
                                elif beowulf_chapter_6_kick_swim!='a' and beowulf_chapter_6_kick_swim!='b' and beowulf_chapter_6_kick_swim!='c':
                                    bad_3()                            
                            if beowulf_chapter_5_no_help_kick_prepare=='b' and victory_wait_counter==1:
                                print('\n\nChapter 8: You wait for too long, and the people rebel against you. Quickly, you are executed. You lose.')
                            if beowulf_chapter_5_no_help_kick_prepare=='c':
                                print('\n\nChapter 8: When you are lying about your victory, someone spots the mother of Grendel, who finds you and eats you. You lose.')
                            elif beowulf_chapter_5_no_help_kick_prepare!='a' and beowulf_chapter_5_no_help_kick_prepare!='b' and beowulf_chapter_5_no_help_kick_prepare!='c':
                                bad_3()
                        if beowulf_chapter_4_no_help_kick=='b':
                            print('\n\nChapter 7: You cower in fear, which causes the citizens do doubt your ability to lead. Quickly, you are overthrown and executed. You lose.')
                        if beowulf_chapter_4_no_help_kick=='c':
                            print("\n\nChapter 7: You do nothing about Grendel's mother, who continues to terrorize the country. Quickly, you are overthrown and beheaded. You lose.")
                        elif beowulf_chapter_4_no_help_kick!='a' and beowulf_chapter_4_no_help_kick!='b' and beowulf_chapter_4_no_help_kick!='c':
                            bad_3()
                    if kick>=2:
                        print('\n\nChapter 5: As you try to kick Grendel in the chest, he blocks your kick and throws you to the ground. You lose.')
                if beowulf_chapter_3_lair=='c':
                    escape=random.randrange(0,2)
                    if escape<2:
                        print('\n\nChapter 5: You successfully escape the cave, but when the Scylding people find out that you are a coward, you are overthrown and executed. You lose.')
                    if escape==2:
                        print('\n\nChapter 5: You unsuccessfully leave the cave, as Grendel grabs you and eats you. You lose.')
                elif beowulf_chapter_3_lair!='a' and beowulf_chapter_3_lair!='b' and beowulf_chapter_3_lair!='c':
                    bad_3()
            if beowulf_chapter_2=='b':
                print('\n\nChapter 4: Then from the moor, in a blanket of mist, Grendel came stalking-he bore the anger of God; the evil marauder meant to ensnare some of human-kind in that high hall. (Beowulf 710-714)')
                print('You successfully lure Grendel to the mead hall, and distract him with your army. You have an opportunity to attack him.')
                beowulf_chapter_3_lure=input('\nDo you (a) try to rip off his arm, (b) try to tackle him to the ground, or (c) try to escape?')
                if beowulf_chapter_3_lure=='a':
                    rip_lure=random.randrange(0,7)
                    if rip_lure<2:
                        print('\n\nChapter 5: [T]he courageous kinsman of Hygelac had him in hand-hateful to each was the life of the other. The loathsome creature felt a great pain in his body; a gaping wound opened in his shoulder-joint (Beowulf 814-817)')
                        print('You successfully rip off the arm of Grendel! As he runs away, you celebrate your victory back at in the mead-hall, and you are showered by gifts from the Scylding citizens.')
                        print('\n\nChapter 6: After your victory, news spreads across the country, even Hrothgar, from the Danes, comes and gives you gifts!')
                        print ('[A] mighty evil marauder who means to avenge her kin, and too far has carried out her revenge (Beowulf 1339-1341)')
                        print('But soon, the celebrations are cut short. The mother of Grendel breaks into the mead hall and causing trouble, so Hrothgar comes to invite you to defeat her. He offers bountiful treasures to slay the mother of Grendel.')
                        beowulf_chapter_4_no_help_rip=input('\nDo you (a) prepare to slay the mother of Grendel, (b) cower in fear, or (c) do nothing about it? ')
                        if beowulf_chapter_4_no_help_rip=='a':
                            print('Chapter 7: You prepare to slay the mother of Grendel by getting some of the strongest weapons and armour: an underwater suit, a poison-striped sword, and more.')
                            print('Now that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory?')
                            beowulf_chapter_5_no_help_rip_prepare=input('\nNow that you have all your equipment ready, do you (a) swim to her lair, (b) wait for her to come out, or (c) return back home and lie about a victory?')
                            while beowulf_chapter_5_no_help_rip_prepare=='b' and victory_wait_counter==0:
                                print('\n\nYou wait for her to come out of her lair but she never does.........')
                                victory_wait_counter+=1
                                beowulf_chapter_5_no_help_rip_prepare=input('\nDo you (a) swim to her lair, (b) keep waiting onshore for her to come out, or (c) return back home and lie about a victory?')
                            if beowulf_chapter_5_no_help_rip_prepare=='a':
                                print('\n\nChapter 8: [H]e gave a mighty blow with his battle-sword - he did not temper that stroke - so that the ring-etched blade rang out on her head a greedy battle-song. The guest discovered then that the battle-flame would not bite, or wound her fatally......It was the first time that the fame of that precious treasure had failed (Beowulf 1519-1524, & 1527-1528)')
                                print("You swim to Grendel's mom's lair. You try to use your sword against her, but it is ineffective. She starts grabbing you and choking you.")
                                beowulf_chapter_6_swim=input("\nYour life is flashing before your eyes, do you (a) try to run away, (b) try to fight back using your bare hands, or (c) try to find something else to fight Grendel's mother with")
                                if beowulf_chapter_6_swim=='a':
                                    print('\n\nChapter 9: You try to run away, but soon you are captured and choked by the mother of Grendel. You lose.')
                                if beowulf_chapter_6_swim=='b':
                                    print("\n\nChapter 9: You try to fight Grendel's mom with your bare hands, but you are quickly defeated in battle. You lose.")
                                if beowulf_chapter_6_swim=='c':
                                    find_luck=random.randrange(0,9)
                                    if find_luck<6:
                                        print('\n\nChapter 9: He saw among the armor a victorious blade, ancient giant-sword strong in its edges, worthy in battles (Beowulf 1557-1560)')
                                        print("The Scyldings' champion seized its linked hilt, fierce and ferocious, drew the ring-marked sword despairing of his life, struck in fury so that it caught her hard in the neck, broke her bone-rings; the blade cut through the doomed flesh- she fell to the floor, the sword was bloody, the soldier rejoiced (Beowulf 1563-1569)")
                                        print("\nYou try to find something to attack Grendel's mom with, and you find a sword on her lair! You stab her with it, and successfully defeat Grendel's mom!")
                                        print("\n\nChapter 10: You celebrate another great victory, but Hrothgar does not come celebrate with you, as he does not care about the fight between you and Grendel's mom.")
                                        print('You feel offended by Hrothgar not celebrating this victory, and attack him, ending in you getting killed in a bloody battle. You lose. ')
                                    if find_luck>=6:
                                        print("\n\nChapter 9: You try to find something to attack Grendel's mom with, but you can't find anything. Instead, you are quickly defeated. You lose.")
                                elif beowulf_chapter_6_swim!='a' and beowulf_chapter_6_swim!='b' and beowulf_chapter_6_swim!='c':
                                    bad_3()
                            if beowulf_chapter_5_no_help_rip_prepare=='b' and victory_wait_counter==1:
                                print('\n\nChapter 8: You wait for too long, and the people rebel against you. Quickly, you are executed. You lose.')
                            if beowulf_chapter_5_no_help_rip_prepare=='c':
                                print('\n\nChapter 8: When you are lying about your victory, someone spots the mother of Grendel, who finds you and eats you. You lose.')
                            elif beowulf_chapter_5_no_help_rip_prepare!='a' and beowulf_chapter_5_no_help_rip_prepare!='b' and beowulf_chapter_5_no_help_rip_prepare!='c':
                                bad_3()
                        if beowulf_chapter_4_no_help_rip=='b':
                            print('\n\nChapter 7: You cower in fear, which causes doubt amongst your population that you can lead. It leads to a rebellion and your execution. You lose.')
                        if beowulf_chapter_4_no_help_rip=='c':
                            print('\n\nChapter 7: You do nothing about the chaos done, which leads to the people hating you. Quickly, you are dethroned and executed. You lose.')
                        elif beowulf_chapter_4_no_help_rip!='a' and beowulf_chapter_4_no_help_rip!='b' and beowulf_chapter_4_no_help_rip!='c':
                            bad_3()                
                    if rip_lure>=2:
                        print('\n\nChapter 5: You unsuccesfully leap at Grendel, trying to rip off his arm. Instead, he swats you away, and you fall to your doom. You lose.')
                if beowulf_chapter_3_lure=='b':                    
                    print('\n\nChapter 5: You try to tackle Grendel to the floor, but he is too big. Instead, when you lean towards him, he crushes you to the ground. You lose.')
                if beowulf_chapter_3_lure=='c':
                    escape=random.randrange(0,4)
                    if escape<=1:
                        print('\n\nChapter 5: You successfully escape Grendel, but when the Scylding people find you that you ran from battle, you are executed. You lose.')
                    if escape==2:
                        print('\n\nChapter 5: As you try to escape, Grendel throws a massive boulder at you, crushing you underneath it. You lose.')
                    if escape>2:
                        print('\n\nChapter 5: While you try to run away, Grendel grabs you and eats you. You lose.')
                elif beowulf_chapter_3_lure!='a' and beowulf_chapter_3_lure!='b' and beowulf_chapter_3_lure!='c':
                    bad_3()                          
            if beowulf_chapter_2=='c' and wait_counter==2:
                print('\n\nChapter 4: You keep waiting. Slowly, you and your troops starve to death. You lose.')
            if beowulf_chapter_2!='a' and beowulf_chapter_2!='b' and beowulf_chapter_2!='c':
                bad_3()
        if beowulf_chapter_1=='c':
            print('\n\nChapter 3: You cower in fear, which leads to the people not believing in you anymore. Quickly, you are overthrown and executed. You lose.')
        elif beowulf_chapter_1!='a' and beowulf_chapter_1!='b' and beowulf_chapter_1!='c':
            bad_3()
    elif character_choice!='a' and character_choice!='b' and character_choice!='c':
        bad_3()
    loop_count+=1
    print('\nYou have played',loop_count,'times. Your maximum number of attempts is 3.')
    ignore_counter=0
    warn_counter=0
    nerves_counter=0
    wait_counter=0
    mom_counter=0
    annoy_son_counter=0
    revenge_son_counter=0
    look_counter=0
    victory_wait_counter=0
    unferth_counter=0
    wait_help_counter=0
    loop=input('Would you like to play again? ')
else:
    print('\nThanks for playing the Beowulf adventure game, goodbye!')