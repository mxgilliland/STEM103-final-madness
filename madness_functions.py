import random

# sheriff - .38 mag 2d4

def weapon_reminder():
    print("Remember, you must have at least one weapon to proceed to the end.")

def weapon_choice():
    print("You are under attack! What weapon will you pick?")
    print()

def katana():
    print("You pull out the katana and lunge forward.")
    katana_attack = random.randint(1, 12)
    if katana_attack <= 2:
        print("You stumble as you land your attack, making clumsy work with your katana. You deal " + str(katana_attack) + " damage.")

def ninemm():
    print("You pull out your 9mm and do your best to aim and fire.")
    ninemm_attack = random.randint(1, 8)
    if ninemm_attack <= 4:
        print("")

def deagle():
    print("You pull out a pistol, aim, and fire at the Sheriff.")
    deagle_attack = random.randint(1, 12)
    if deagle_attack <= 2:
        print("")

def randomized_weapon():
    random.choice([katana, ninemm, deagle])
    if katana:
        katana()
    if ninemm:
        ninemm()
    if deagle:
        deagle()

def sheriff():
    print("The Sheriff pulls out his dual .38 magnums, and tries to aim and shoot at you.")
    sheriff_attack = random.randint(1, 4) + random.randint(1, 4)
    if sheriff_attack <= 2:
        print("He fires his guns in your direction, and the bullets graze your arm, but don't hit anywhere vital. You take " + str(sheriff_attack) + " damage.")


#def damage():
#    damage_taken = random.randint(1, 4) + random.randint(1, 4)
#    print("You take " + str(damage_taken) + " damage and recoil as you make your next move.")