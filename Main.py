"""This is a demo of a basic adventure game to show off my Python skills."""
__author__ = "Vasil Ivanov III"

import random


def main():
    print_intro()
    valid_character = False
    while not valid_character:
        name_first = input("Please tell me your first name. ")
        while name_first == "":
            name_first = input("\nLet me ask you again.\n"
                               "Please tell me your first name. ")
        if name_first == "admin" or name_first == "Admin":
            name_first = "Vasil"
            name_last = "Ivanov"
            age = 18
            hometown = "Naples"
        else:
            name_last = input("\nAnd your last name? ")
            while name_last == "":
                name_last = input("\nLet me ask you again.\n"
                                  "Please tell me your last name. ")
            age = input("\nHow old are you? ")
            while age == "":
                age = input("\nLet me ask you again.\n"
                            "How old are you? ")
            age_test = age.isnumeric()
            while not age_test:
                age = input("\nPlease provide a real number."
                            "\nHow old are you? ")
                age_test = age.isnumeric()
            hometown = input("\nWhere are you from? ")
            while hometown == "":
                hometown = input("\nLet me ask you again.\n"
                                 "Where are you from? ")
        # Prof. Vanselow: Define variables in main, use as arguments in calls
        # to functions.
        # Variables get received as parameters in headers of functions.
        valid_character = check_character(name_first, name_last, age, hometown)
    print_backstory(name_first, name_last)
    valid_stats = False
    while not valid_stats:
        stats_answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                         "admin", "Admin"]
        print("\nAnswer based on a scale of 1 to 10 for each question.")
        atk = input("\nIf 1 = Twig limbs and 10 = Arnold Schwarzenegger,"
                    "\nHow strong are you? ")
        while atk == "" or atk not in stats_answers:
            atk = input("\nLet me ask you again.\n"
                        "If 1 = Twig limbs and 10 = Arnold Schwarzenegger,"
                        "\nHow strong are you? ")
        if atk == "admin" or atk == "Admin":
            atk = 10
            defense = 10
            speed = 10
            intel = 10
            magic = 10
        else:
            atk_test = atk.isnumeric()
            while not atk_test:
                atk = input("\nPlease provide a real number."
                            "\nIf 1 = Twig limbs and 10 = Arnold"
                            "Schwarzenegger,\nHow strong are you? ")
                atk_test = atk.isnumeric()
            defense = input("\nIf 1 = Paper and 10 = Titanium,"
                            "\nHow durable are you? ")
            while defense == "" or defense not in stats_answers:
                defense = input("\nLet me ask you again.\n"
                                "If 1 = Paper and 10 = Titanium,"
                                "\nHow durable are you? ")
            defense_test = defense.isnumeric()
            while not defense_test:
                defense = input("\nPlease provide a real number."
                                "\nIf 1 = Paper and 10 = Titanium,"
                                "\nHow durable are you? ")
                defense_test = defense.isnumeric()
            speed = input("\nIf 1 = A snail and 10 = Usain Bolt,"
                          "\nHow fast are you? ")
            while speed == "" or speed not in stats_answers:
                speed = input("\nLet me ask you again.\n"
                              "If 1 = A snail and 10 = Usain Bolt,"
                              "\nHow fast are you? ")
            speed_test = speed.isnumeric()
            while not speed_test:
                speed = input("\nPlease provide a real number."
                              "\nIf 1 = A snail and 10 = Usain Bolt,"
                              "\nHow fast are you? ")
                speed_test = speed.isnumeric()
            intel = input("\nIf 1 = Rocks for Brains and 10 = Super-Mega-Ultra"
                          " Nerd,\nHow smart are you? ")
            while intel == "" or intel not in stats_answers:
                intel = input("\nLet me ask you again.\n"
                              "If 1 = Rocks for Brains and 10 = Super-Mega-"
                              "Ultra Nerd,\nHow smart are you? ")
            intel_test = intel.isnumeric()
            while not intel_test:
                intel = input("\nPlease provide a real number."
                              "\nIf 1 = Rocks for Brains and 10 = Super-Mega-"
                              "Ultra Nerd,\nHow smart are you? ")
                intel_test = intel.isnumeric()
            magic = input("\nIf 1 = Another sheep in the herd and 10 = Having "
                          "a lion as a house pet,\nHow weird are you? ")
            while magic == "" or magic not in stats_answers:
                magic = input("\nLet me ask you again.\n"
                              "If 1 = Another sheep in the herd and 10 = "
                              "Having a lion as a house pet,\nHow weird are "
                              "you? ")
            magic_test = magic.isnumeric()
            while not magic_test:
                magic = input("\nPlease provide a real number."
                              "\nIf 1 = Another sheep in the herd and 10 = Hav"
                              "ing a lion as a house pet,"
                              "\nHow weird are you? ")
                magic_test = magic.isnumeric()
        valid_stats = check_stats(atk, defense, speed, intel, magic)
    m_hp = int(defense) * 20
    m_hp += m_hp % 17
    c_hp = m_hp
    m_mp = int(magic) * 10
    c_mp = m_mp
    atk = int(atk) ** 2
    defense = int(defense) * 5
    agility = (int(speed) * 5) / 2
    smarts = (int(intel) + int(age)) // 2 - (int(age) // 5)
    print_stats(m_hp, m_mp, atk, defense, agility, smarts)
    list_stats_short = ["HP", "MP", "Atk", "Def", "Spd", "Per"]
    list_stats = [str(c_hp) + "/" + str(m_hp), str(c_mp) + "/" + str(m_mp),
                  str(atk), str(defense), str(agility), str(smarts)]
    list_battle = ["Attack", "Guard", "Use Item", "Check Stats", "Run"]
    list_attack = ["Go Back", "Fists", "Magic"]
    list_magic = ["Fire", "Ice", "Lightning", "Earth", "Void"]
    battle(list_battle, list_attack, list_stats_short, list_stats, atk,
           agility, list_magic, c_mp, m_mp, defense, c_hp, m_hp)
    print("\nThank you so much for playing my demo,", name_first + "!")


def print_intro():
    """This function prints the introduction text for the game, introducing
    the player to the game."""
    input("\nHello, and welcome to The Quest!  This adventure is very simple"
          "\nand straight-forward, but you will face combat!\n"
          "\n(Whenever you see this icon (*) at the end of a sentence,"
          "\nmake sure the cursor is next to it and press the Enter key"
          "\nto advance the text.  Try it with this line here!) *")
    input("\n(Perfect!  Now, do it once more to advance the story.) *")
    input("\nNow then, for there to be an adventure, there"
          "\nmust be an adventurer.  Let's create the adventurer now... *")
    print("")


def check_character(name_first, name_last, age, hometown):
    """This function tells the player to confirm and lock in their character
    information."""
    print("\nLet me make sure I got this right...")
    print("Your first name is", name_first + ".")
    print("Your last name is", name_last + ".")
    print("You are", age, "years old.")
    print("You are from", hometown + ".\n")
    c_check_answers = ["Yes", "yes", "YES", "y", "Y",
                       "N", "n", "NO", "no", "No"]
    c_check = input("Is this correct? ")
    if c_check in c_check_answers:
        if c_check == "Yes" or c_check == "yes" or c_check == "YES" or c_check\
                == "y" or c_check == "Y":
            input("\nGreat!  Let me tell you about the setting, then. *")
            return True
        elif c_check == "No" or c_check == "no" or c_check == "NO" or c_check \
                == "n" or c_check == "N":
            print("\n*sigh* Let's try this again...\n")
            return False
    while c_check not in c_check_answers:
        c_check = input("\nLet me ask you again.\n"
                        "Is this information correct? ")


def print_backstory(name_first, name_last):
    """This function prints the backstory text for the story.
    It uses the character's first and last name as arguments and parameters."""
    print("\nOne morning, you received a strange letter from the postman:\n")
    print("~" * 71)
    print("    Dear", name_first, "of House", name_last + ",")
    print("\n       If this letter reaches you, I ask for your aid.")
    print("    The evil brute Taniks has taken over the land of Europa.  Our")
    print("    people are in grave danger.  I know not how much longer we can")
    print("    last.  If the legends are true, I know you will answer our call"
          )
    print("    for help.  Please tell me they are true...\n")
    print("    Please help us, Sir", name_first + "!\n")
    print("    ~ Princess Roselia\n")
    print("~" * 71)
    input("\nAfter reading the letter, you clutch your fist with determination"
          ".\nYou know what must be done.  You set off for Europa!\n"
          "\n   The Quest awaits... *")
    input("\nNow, before we go any further, your adventurer needs "
          "combat stats.\nLet's get you equipped. *")


def check_stats(attack, defense, speed, intelligence, magic):
    """This function asks the player to confirm and lock in their answers for
    their stats."""
    print("\nLet me make sure I got this right...")
    print("For how strong you are, you put", str(attack) + ".")
    print("For how durable you are, you put", str(defense) + ".")
    print("For how fast you are, you put", str(speed) + ".")
    print("For how smart you are, you put", str(intelligence) + ".")
    print("For how weird you are, you put", str(magic) + ".")
    s_check_answers = ["Yes", "yes", "YES", "y", "Y",
                       "N", "n", "NO", "no", "No"]
    s_check = input("\nAre you happy with these? ")
    if s_check in s_check_answers:
        if s_check == "Yes" or s_check == "yes" or s_check == "YES" or s_check\
                == "y" or s_check == "Y":
            input("\nGreat!  Let me calculate your stats... *")
            return True
        elif s_check == "No" or s_check == "no" or s_check == "NO" or s_check \
                == "n" or s_check == "N":
            print("\n*sigh* Let's try this again...\n")
            return False
    while s_check not in s_check_answers:
        print("\nLet me ask you again.")
        s_check = input("Are you happy with your responses? ")
        if s_check == "Yes" or s_check == "yes" or s_check == "YES" or s_check\
                == "y" or s_check == "Y":
            input("\nGreat!  Let me calculate your stats... *")
            return True
        elif s_check == "No" or s_check == "no" or s_check == "NO" or s_check \
                == "n" or s_check == "N":
            print("\n*sigh* Let's try this again...\n")
            return False


def print_stats(max_hp, max_mp, attack, defense, agility, smarts):
    """This function prints the player's stats for the first time."""
    input(". *")
    input(".. *")
    input("... *")
    print("\nYour stats are as follows:\n")
    print("Max HP (Health Points):  " + str(max_hp))
    print("Max MP (Magic Points):   " + str(max_mp))
    print("Attack:  " + str(attack))
    print("Defense: " + str(defense))
    print("Speed: " + str(agility))
    print("Perception:  " + str(smarts))


def print_menu(menu):
    """This function is used for printing the menus for player choices."""
    for index in range(len(menu)):
        print(str(index + 1) + ".  ", menu[index])


def print_sub_menu(menu):
    """This function is basically the same as print_menu, but it leaves the 0
    in for going back to the previous menu."""
    for index in range(len(menu)):
        print(str(index) + ".  ", menu[index])


def print_menu_stats(short, stats):
    """This function is called when the player wants to see their stats.
    It prints their stats in a short, simplified list."""
    print("\nStats")
    print("-" * 17)
    for index in range(len(stats)):
        print(short[index] + ":   " + stats[index])
    print("-" * 17, "\n")
    input("*")


def calculate_damage(attack, defense):
    """This function calculates the damage of an attack."""
    damage = int(abs((2 * attack) - (2 * defense)))
    damage *= random.random()
    damage = round(damage)
    return damage


def battle(list_battle, list_attack, stats_short, stats_menu, atk, agility,
           list_magic, c_mp, m_mp, defense, c_hp, m_hp):
    """This function is the battle sequence the player encounters."""
    input("\nNow that your stats are defined, your quest can finally begin!\n"
          "\nAdvance this text to begin The Quest. *")
    input("\nYou arrive in Europa with nothing but the clothes on you back,"
          "\nyour bare fists, and your trusty satchel.\n"
          "\nAs you cross over the hill, you see a vast, birch forest"
          "\nblocking your path to the local town.  The only way to the town"
          "\nis through the trees, so you head into the forest. *")
    input("\nYou creep through the forest as the forest itself creeps you"
          "\nout.  You hear the rustling of leaves, the chirping of bugs, and"
          "\nthe distant cries of deer.  You continue to walk through...\n"
          "\nWhen suddenly... *")
    input("\nROAR!\n"
          "\nA wild black bear blindsides you!\n\nIts hungry eyes glare at you"
          " as it ponders what piece of you to eat first. *")
    e_name = "black bear"
    e_hp = 500
    e_atk = 3
    e_def = 20
    e_speed = 10
    input("\nWhat will you do? *")
    print("\nWill you... \n"
          "(For menus like this, write the number of the action after the "
          "> and press Enter)\n")
    battle_over = 1
    while battle_over == 1:
        print_menu(list_battle)
        battle_input = input("\n> ")
        if battle_input == "1":
            print("Attack with what?")
            print_sub_menu(list_attack)
            attack_input = input("\n> ")
            if attack_input == "0":
                battle_over = 1
                print("\nWill you...\n")
            elif attack_input == "1":
                print("You throw a strong jab at the enemy", e_name + ".")
                dmg = calculate_damage(atk, e_def)
                e_hp = e_hp - dmg
                if e_hp <= 0:
                    print("\nKnockout!\n"
                          "\nThe enemy", e_name, "is dead!")
                    battle_over = 0
                else:
                    print("You dealt", dmg, "damage to the enemy", e_name + "."
                          )
                    input("\n*")
                    battle_over = 1
                    print("\nWill you...\n")
            elif attack_input == "2":
                # Run magic attack function
                print("What spell will you use?")
                print_menu(list_magic)
                magic_input = input("\n> ")
                if magic_input == "1":
                    print("You cast a fireball and throw it at the enemy",
                          e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 4
                    stats_menu[1] = str(c_mp) + '/' + str(m_mp)
                    if e_hp <= 0:
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("\nWill you...\n")
                elif magic_input == "2":
                    print("You cast a large icicle and throw it like a spear a"
                          "t the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 4
                    stats_menu[1] = str(c_mp) + '/' + str(m_mp)
                    if e_hp <= 0:
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("\nWill you...\n")
                elif magic_input == "3":
                    print("You channel electricity though your hand and shoot "
                          "it at the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 5
                    stats_menu[1] = str(c_mp) + '/' + str(m_mp)
                    if e_hp <= 0:
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("\nWill you...\n")
                elif magic_input == "4":
                    print("Razor-sharp leaves form in-between your fingers, an"
                          "d you throw them at the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 3
                    stats_menu[1] = str(c_mp) + '/' + str(m_mp)
                    if e_hp <= 0:
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("\nWill you...\n")
                elif magic_input == "5":
                    print("You cast a dark ball of chaotic energy and hurl it "
                          "at the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 6
                    stats_menu[1] = str(c_mp) + '/' + str(m_mp)
                    if e_hp <= 0:
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("\nWill you...\n")
            else:
                battle_over = 1
        elif battle_input == "2":
            print("You guard your face with your arms as "
                  "the", e_name, "swings its paws at you.")
            dmg = calculate_damage(e_atk, defense)
            c_hp = c_hp - dmg
            stats_menu[0] = str(c_hp) + '/' + str(m_hp)
            if c_hp <= 0:
                print("\nThe blow was too much for you to take!"
                      "\nYou fall to the ground in defeat...\n"
                      "\nYou died.\n\nGame Over\n")
                battle_over = 0
            else:
                print("You took", dmg, "damage from the enemy", e_name + ".")
                input("\n*")
                battle_over = 1
                print("\nWill you...\n")
        elif battle_input == "3":
            print("You don't have any items.\n"
                  "\nWill you...\n")
        elif battle_input == "4":
            print_menu_stats(stats_short, stats_menu)
            battle_over = 1
            print("\nWill you...\n")
        elif battle_input == "5":
            if agility >= e_speed:
                print("\nSuccess!\n"
                      "\nYou run away from the enemy", e_name + "!")
                battle_over = 0
            else:
                print("You couldn't escape the enemy", e_name + ".")
                print("\nWill you...\n")
        else:
            print("\nChoose a valid number from the list.\n")
            battle_over = 1
            print("\nWill you...\n")
    input("\nBattle over! *")


main()
