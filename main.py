import random
import time
from madness_functions import *

# NOTES TO SELF
# FIND A WAY TO TRACK HEALTH. some sort of loop is good for this i imagine
# Create a list for the weapon "inventory", won't actually be a proper inventory but will be called upon
# Figure out health stats for Hank + the Sheriff
# Time.sleep will be used

weapon_list = [] # will eventually contain a katana, deagle, and 9mm
hank_health = 54 # Pulled from the MADNESS: Project Nexus wiki for Hank's health stats
sheriff_health = 75 # Pulled from the MADNESS: Project Nexus wiki for Sheriff's health stats

# The way the game starts is with Hank waking up in a dream
# When they wake up, they get up off the ground, look around
look_around = input("Would you like to look around? ")
# this is botched, fix this later and reference the program with if homework to find the solution
# can also reference the elif solutions, there is a picture on your phone to look at
if look_around == "Yes":
    print("You get up and look around. On the table nearby, you see a katana lying around.")
    weapon_reminder()
    katana_pick_up = input("Would you like to pick up the katana? ")
    if katana_pick_up == "Yes":
        print("You pick up the katana, and tuck it into your pocket.")
        weapon_list.append("Katana")
        print(weapon_list)
    else:
        print("You leave the katana behind, you'll find something else, you're sure.")
else:
    print("You decide not to look around.")
# input an else statement that passes over the katana options, don't forget to include this above

# Here, there will be a pause after they take in their surroundings
time.sleep (1.5)
# After this, they will have an opportunity to move around and explore
print("After you finish looking around, you see that there's two different ways that you can go, forward or left.")
cross_roads_one = input("Would you like to go forward or left? ")
# this is botched, fix this later and reference the program with if homework to find the solution
# can also reference the elif solutions, there is a picture on your phone to look at
if cross_roads_one == "Forward" or "Left":
    if cross_roads_one == "Forward":
        print("You proceed forward, and find a small room tucked away.")
        # deagle found in this room
        time.sleep(1)
        print("As you enter the room, you notice a deagle lying around on the floor.")
        weapon_reminder()
        deagle_pick_up = input("Would you like to pick up the deagle? ")
        if deagle_pick_up == "Yes":
            print("You pick up the deagle, and tuck it away into your holster.")
            weapon_list.append("Deagle")
            print(weapon_list)
        else:
            print("You leave the deagle behind, you'll find something else, you're sure.")
        # if the user proceeds forward, they will need to turn around to leave and proceed
    else:
        if cross_roads_one == "Left":
            print("You proceed to the room to the left.")
        else:
            print("Invalid direction.")
    # no weapons found here, but will have an opportunity to spy on the sheriff
    # next room is forward from here
    # 3rd room will contain 9mm
    # weapon_reminder()
    # 4th room is to the right of 3rd room
    # 5th room is forward of 4th room + where the boss fight will occur
# This is where they will have the chance to pick up weapons as they explore
# They will have to move through a few rooms, stalking to follow the Sheriff stealthily through a building.
# This will consist of a decent amount of story lines explaining what the Sheriff is doing and how Hank is watching him

# What the boss fight will look like
# When you enter the final room, it will trigger an encounter with the Sheriff
# The Sheriff will start monologuing, Hank won't care much
    # print statements of sheriff's monologuing
# Once the Sheriff's monologue is over, the fight begins
# This is where loops and the RNG will come into play
    # while loop will go here
# There will also be an option to select a weapon from the user's inventory, this will be a list
    # weapon_choice()
# The weapon chosen will have a specific range for a number to be generated, which will be the damage done to the Sheriff
# The Sheriff will also have specific RNG for his weapon.
# There is a chance that the player can lose based on the RNG. It will not always happen that the player will win.
# Because the game is turnbased, there will also be a little bit of strategy involved.