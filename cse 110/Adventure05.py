# Create a text-based advneture game with 3 levels of choice scenarios.
# Week 05 only needs the first level of scenarios.

print("Welcome to Dungeon Adventure!\n")
print("---Type ENTER to play---")
enter = input("--> ")
if enter.upper() == "ENTER":
        print("Good luck adventurer!!")
        print("\nYou enter the first room of the dungeon,")
        print("and you see 3 doorways. Do you go LEFT, RIGHT, or STRAIGHT?")
#Start with the first room and hit has 3 options
        first_choice = input("--> ").lower()


        # If LEFT was chosen
        if first_choice == "left":
            print("You go through the left doorway....")
            print("\nYou see a locked door and another open gateway leading to a forest.")
            print("You also see an wood table in front of you.")
            print("On the table is a SWORD and a KEY.")
            print("You can take the key and unlock the door, or grab the sword and enter the forest.")
            left = input("\nWhich do you do? ").lower()

            # If SWORD was chosen
            if left == "sword":
                print("\nYou grab the sword and head into the forest...")
                print("\nYou walk for a bit and suddenly enter a clearing.")
                print("Upon entering the clearing you see a shadowy figure across from you.")
                print('The figure yells to you very angrily, "That is my sword!!"')
                sword = input("Do you GIVE him the sword or RUN away from him? ").lower()

                # Options are GIVE and RUN
                if sword == "give":
                     print("\nYou offer to give him the sword.")
                     print("\nThe figure walks towards you and in the moonlight you see that this man is wearing armour.")
                     print("He takes the sword and reveals himself as King Arthur.")
                     print("He had lost his sword and thanks you kindly for returning it.")
                     print("To reward you for this gracious act he invites you to join him")
                     print("as a knight of the round table.")
                     print("\n\nCongrats!!! Thanks for playing!")
                elif sword == "run":
                    print("\nYou take of running away from the crazy man.")
                    print("\nYou're sprinting through the forest and you can hear the man chasing after you.")
                    print("You misplace your footing and trip and hit your head on a rock.")
                    print("As your vision starts the blur and blacken, you see the man walk up to you and")
                    print("pick up the sword and say: 'You should've given up when you had the chance.'")
                    print("You vision fades to black.")
                    print("\n\nSorry! Thanks for playing!")
                else:
                    print("Sorry, you made gave a false decision. Try again.")
                    exit()

            # If KEY was chosen
            elif left == "key":
                print("\nYou grab the key and unlock the door...")
                print("\nThe massive wooden door swings open and a bright light shines through the doorway.")
                print("You see a small pedestal in front of you with two cups with water in them.")
                print("An inscription on the pedestal says 'One of these cups is posoined and one grants immortality'")
                cup = input("Do you choose the LEFT cup or the RIGHT cup?").lower()

                # Options are LEFT and RIGHT
                if cup == "left":
                    print("\nYou drink the cup on the left and  feel refreshened.")
                    print("You feel yourself growing younger again and feel stronger already.")
                    print("\n\nCongrats!!! Thanks for playing!")
                elif cup == "right":
                    print("\nYou take a drink of the cup on the right.")
                    print("You immediately feel a pain in your gut.")
                    print("You fall to the floor as your vision fades to black from the poison.")
                    print("Sorry! Thanks for playing!")
                else:
                    print("Sorry, you made gave a false decision. Try again.")
                    exit()
            else:
                print("Sorry, you made gave a false decision. Try again.")
                exit()

        # If RIGHT was chosen
        elif first_choice == "right":
            print("You go through the right doorway....")
            print("\nYou enter the room and see a big pit in front of you.")
            right = input("Do you JUMP over it or find a way AROUND it? ").lower()

            # If JUMP was chosen
            if right == "jump":
                print("\nYou jump over the pit and land safely on the other side.")
                print("You continue on your adventure and enter a room full of traps and pitfalls.")
                jump = input("Do you try to get around the traps to EXPLORE further, or turn around a LEAVE? ").lower()

                # Options are EXPLORE and LEAVE
                if jump == "explore":
                    print("\nYou carefully avoid each trap that was set and walk down a long hallway.")
                    print("You enter a room filled with treasure galore.")
                    print("\n\nCongrats!!! Thanks for playing!")
                elif jump == "leave":
                    print("AS you turn to leave you feel the tension of a tripwire on you leg.")
                    print("The doors slam shut and you are now trapped forever in this stone room.")
                    print("\n\nSorry! Thanks for playing!")
                else:
                    print("Sorry, you made gave a false decision. Try again.")
                    exit()

            # If AROUND was chosen
            elif right == "around":
                print("\nYou try to go around and fall in...")
                print("You fall into an underground river and you startflowing down stream.")
                around = input("Do you continue to FLOAT down stream or try to grab onto an EDGE? ").lower()

                # Options are FLOAT and EDGE
                if around == "float":
                    print("\nAs you float down the river it starts to pick up and suddenly you are swept underwater.")
                    print("Grasping for air you can't find the strength to stay above water.")
                    print("\n\nSorry! Thanks for playing!")
                elif around == "edge":
                    print("\nYou see a branch hanging over the edge and you grab ahold of it.")
                    print("You pull yourself up and see a staircase leading up towards the surface.")
                    print("You make it out and start heading towards the nearest village.")
                    print("\n\nCongrats!!! Thanks for playing!")
                else:
                    print("Sorry, you made gave a false decision. Try again.")
                    exit()
            else:
                print("Sorry, you made gave a false decision. Try again.")
                exit()

        # If STRAIGHT was chosen
        elif first_choice == "straight":
            print("You go through the straight doorway....")
            print("\nYou walk into the next room and see a dark passageway.")
            straight = input("Do you LIGHT a torch and go down it or continue WITHOUT a light? ").lower()

            # If LIGHT was chosen
            if straight == "light":
                print("\nYou grab an old stick on the ground and light it and venture down the hallway...")
                print("You come across a large stone door at the end of the hallway.")
                light = input("Do you EXAMINE the door closely or LOOK for a hidden entrance? ").lower()
                
                # The options are EXAMINE and LOOK
                if light == "examine":
                    print("\nYou look closely at the door and see a keyhole and decide to start looking on the ground for a key.")
                    print("You find a rusty key and turn the lock on the door.")
                    print("The door opens and you find yourself standing in a big castle. The gaurds seize you and")
                    print("bring you before the king. He calls you a theif and imprisons you in the highest tower.")
                    print("\n\nSorry! Thanks for playing!")
                elif light == "look":
                    print("\nYou start looking around for a hidden entrance and find a lever behind some vines.")
                    print("You pull it and a cutaway of the wall opens. You go down the stairs and find yourself")
                    print("Surrounded by mounds of gold and jewels. You realize you are standing in King Arthur's treasure room!")
                    print("\n\nCongrats!!! Thanks for playing!")
                else:
                    print("Sorry, you made gave a false decision. Try again.")
                    exit()
            
            # If WITHOUT was chosen
            elif straight == "without":
                print("\nYou start your way down the hallway, feeling the cold stone wall on your hands.")
                print("As you are making your way down the hallway, you suddenly feel a couple stones get pushed in")
                print("and an opening appears. When you go down it you enter a room with a sleeping dragon.")
                print("The dragon is sleeping in front of a door leading outside, but you see a steel axe on the ground.")
                without = input("Do you SNEAK around the dragon and escape or try to take the AXE and attack? ").lower()
                
                # Options are SNEAK and AXE
                if without == "sneak":
                    print("\nYou carefully sneak around the sleeping dragon and make it to the exit.")
                    print("Once you make it outside, you take off sprinting away from the dragon.")
                    print("\n\nCongrats!!! Thanks for playing!")
                elif without == "axe":
                    print("\nYou go and pick up the axe.")
                    print("The scraping of metal against the stone awakes the dragon and you charge right at it.")
                    print("Just before you slash at the dragon with the axe, you get swept off your feet by its tail.")
                    print("You just became the dragon's next meal.")
                    print("\n\nSorry! Thanks for playing!")
                else:
                    print("Sorry, you made gave a false decision. Try again.")
                    exit()
            else:
                print("Sorry, you made gave a false decision. Try again.")
                exit()
        else:
            print("Sorry, you made gave a false decision. Try again.")
            exit()
else:
    print("Sorry, you made gave a false decision. Try again.")
    exit()