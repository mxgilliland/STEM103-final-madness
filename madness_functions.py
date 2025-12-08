import random

# Provide a reminder that the user needs a weapon to proceed to the end
def weapon_reminder():
    print("Remember, you must have at least one weapon to proceed to the end.")

# Provide a weapon choice for fights
def weapon_choice():
    print("You are under attack!")
    print(["Katana", "9mm", "Deagle", "Random Attack"])
    weapon_choice_input = input("What weapon will you pick? ")
    if weapon_choice_input == "katana":
        katana()
    else:
        if weapon_choice_input == "9mm":
            ninemm()
        else:
            if weapon_choice_input == "deagle":
                deagle()
            else:
                if weapon_choice_input == "random attack":
                    randomized_weapon()
                else:
                    print("Invalid option.")

# Give the user a katana option, 1d12
def katana():
    print("You pull out the katana and lunge forward.")
    katana_attack = random.randint(1, 12)
    if katana_attack <= 2:
        print("You stumble as you land your attack, making clumsy work with your katana. You deal " + str(katana_attack) + " damage.")
    else:
        if katana_attack <= 6:
            print("You manage to land your attack, slicing your opponent through the arm. You deal " + str(katana_attack) + " damage.")
        else:
            if katana_attack <= 10:
                print("You land a critical hit! You deal " + str(katana_attack) + " damage.")

# Give the user a 9mm option, 1d8
def ninemm():
    print("You pull out your 9mm and do your best to aim and fire.")
    ninemm_attack = random.randint(1, 8)
    if ninemm_attack <= 2:
        print("You fire your 9mm, but the bullet barely grazes him. You deal " + str(ninemm_attack) + " damage.")
    else:
        if ninemm_attack <= 4:
            print("Neutral hit "+ str(ninemm_attack) + " damage.")
        else:
            if ninemm_attack <= 6:
                print("Critical hit "+ str(ninemm_attack) + " damage.")

# Give the user a deagle option, 1d12
def deagle():
    print("You pull out a pistol, aim, and fire at the Sheriff.")
    deagle_attack = random.randint(1, 12)
    if deagle_attack <= 2:
        print("Barely hit " + str(deagle_attack) + " damage.")
    else:
        if deagle_attack <= 6:
            print("Neutral hit " + str(deagle_attack) + " damage.")
        else:
            if deagle_attack <= 10:
                print("Critical hit " + str(deagle_attack) + " damage.")

# Provide the user with a randomize option, these filter through the other attack options and will do damage accordingly
def randomized_weapon():
    randomized_weapon_choice = random.choice([katana, ninemm, deagle])
    if randomized_weapon_choice == katana:
        katana()
    if randomized_weapon_choice == ninemm:
        ninemm()
    if randomized_weapon_choice == deagle:
        deagle()

# Sheriff's attack is 2d4 defined below
def sheriff():
    print("The Sheriff pulls out his dual .38 magnums, and tries to aim and shoot at you.")
    sheriff_attack = random.randint(1, 4) + random.randint(1, 4)
    if sheriff_attack <= 2:
        print("He fires his guns in your direction, and the bullets graze your arm, but don't hit anywhere vital. You take " + str(sheriff_attack) + " damage.")
    else:
        if sheriff_attack <= 4:
            print("He fires his guns at you, and the bullets graze your torso. You take " + str(sheriff_attack) + " damage.")
        else:
            if sheriff_attack <= 6:
                print("He fires his guns, and the bullets hit your chest. You take " + str(sheriff_attack) + " damage.")