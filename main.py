import random
import time
from madness_functions import *

# NOTES TO SELF
# FIND A WAY TO TRACK HEALTH. some sort of loop is good for this i imagine
# the health tracker will probably be a for loop. don't forget to implement this

# Create a list for the weapon "inventory", won't actually be a proper inventory but will be called upon
# Figure out health stats for Hank + the Sheriff
weapon_list = [] # will eventually contain a katana, deagle, and 9mm
hank_health = 54 # Pulled from the MADNESS: Project Nexus wiki for Hank's health stats
sheriff_health = 75 # Pulled from the MADNESS: Project Nexus wiki for Sheriff's health stats

# The way the game starts is with Hank waking up in a dream
# When they wake up, they get up off the ground, look around
print("There's a loud bang outside as you open your eyes.")
time.sleep(.5)
print("You shake off sleep with ease, and look down at your hands.")
time.sleep(.5)
print("Your hands are gloved, though your gloves have been long stained with blood.")
time.sleep(1)
look_around = input("Would you like to look around? ")
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
# Here, there will be a pause after they take in their surroundings
time.sleep (1.5)
# After this, they will have an opportunity to move around and explore
print("After you finish looking around, you see that there's a room tucked away in front of you. You decide to check it out.")
print("You proceed forward, and enter the storage room.")
# deagle found in this room
time.sleep(1)
print("As you enter the room, you notice a deagle lying around on the floor.")
weapon_reminder()
deagle_pick_up = input("Would you like to pick up the deagle? ")
if deagle_pick_up == "Yes":
    print("You pick up the deagle, and tuck it away into your holster.")
    weapon_list.append("Deagle")
    print(weapon_list)
    print("After you pick up the deagle, you smile to yourself. Your power grows.")
else:
    print("You leave the deagle behind, you'll find something else, you're sure.")
print("After you're done exploring, you turn around and return to the room you started in.")
print("There's another room to your left as you return to the room you started in. You decide it would be best to check out this next room.")
    # no weapons found here, but will have an opportunity to spy on the sheriff
print("There's nothing that catches your eye as you enter this room. You let out an irritated sigh.")
time.sleep(1)
print("However...")
print("As you look around, you notice a window. This window exposes a room nearby.")
print("The exposed room reveals your target, the Sheriff. You would grin if you could.")
print("You decide to spy on him for a bit before continuing through the rooms.")
print("You make your way to the next room, and look around.")
print("As you're looking around, something catches your eye.")
weapon_reminder()
ninemm_pickup = input("It's a 9mm! Would you like to pick it up? ")
if ninemm_pickup == "Yes":
    print("You pick up the 9mm, and tuck it away into your other holster.")
    weapon_list.append("9mm")
    print(weapon_list)
    print("After you pick up the pistol, you continue looking around.")
else:
    print("You leave the 9mm behind. Hopefully you've already picked something else up by now.")
print("After you finish looking around, a vent catches your eye.")
print("You take the grate off of the vent, and pull yourself up into it.")
time.sleep(1)
# They will have to move through a few rooms, stalking to follow the Sheriff stealthily through a building.
print("You peer below as you make your way through the vent system, seeing the Sheriff talking to two people.")
print("You can't quite make out what they're saying, but it's not like you care in the first place.")
time.sleep(1)
print("You roll your eyes, and carry on with your mission. You're almost there, you're sure of it.")
time.sleep(3)
print("The ventilation system leads into another room, and you peer through the grate to see what's below.")
print("There he is.")
print("Your target. The Sheriff.")
time.sleep(2)
# When you enter the final room, it will trigger an encounter with the Sheriff
print("As you drop into the room from the vents, the Sheriff looks like he's about to jump out of his skin as you startle him.")
print("The Sheriff takes a moment to collect himself, and takes a deep breath.")
# The Sheriff will start monologuing, Hank won't care much
print("After having done so, the Sheriff looks in your direction, and starts speaking.")
time.sleep(3)
print("As the Sheriff goes on about his monologue, you roll your eyes impatiently. You just want him to be done talking already.")
# Once the Sheriff's monologue is over, the fight begins
# This is where loops and the RNG will come into play
while (sheriff_health > 0) or (hank_health > 0):
    # There will also be an option to select a weapon from the user's inventory, this will be a list
    weapon_choice()
    time.sleep(1)
    sheriff()
    if sheriff_health <= 0:
        print("The Sheriff staggers to the ground, trying to get in enough oxygen. You tower over him. You've won.")
    if hank_health <= 0:
        print("The Sheriff shoots you down. Game over.")
# The weapon chosen will have a specific range for a number to be generated, which will be the damage done to the Sheriff
# The Sheriff will also have specific RNG for his weapon.
# There is a chance that the player can lose based on the RNG. It will not always happen that the player will win.
# Because the game is turnbased, there will also be a little bit of strategy involved.