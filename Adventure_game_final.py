import time
import random
######################

line_delay = 2

def print_pause(message_to_print, time_to_wait=3):
    print(message_to_print)
    time.sleep(time_to_wait)


################################################################

def would_you_like_to_exit_the_game():
    print(      "--------------------------------------------")
    print_pause("Game Over...", line_delay)
    print_pause("Would you like to play again ?",line_delay)
    print_pause("Enter 1 to play again",line_delay)
    print_pause("Enter 2 to Exit", line_delay)
    response = verify_user_input("1", "2")
    return response == "2"

###################################################################


def verify_user_input(option1,option2):
    while True:
        #Capturing the user input
        response = input(">> ").lower()

        #Validating the User Input
        if option1.lower() in response:
            break
        elif option2.lower() in response:
            break
        else:
            print_pause("sorry, I don't understand. please enter " + option1 + " or " + option2, line_delay)

    return response

###########################
def story_intro():
    print(      "#################################################################################################")
    print_pause("A doctor who was on a mission to deliver malaria vaccines to children is missing in the jungle.\n"
                "It is up to you to find her and deliver the medicine.", line_delay)
    print_pause("There are two ways to go... Walk through the jungle or walk along the river.", line_delay)
    print_pause("Which way would you like to go?", line_delay)
    print(      "------------------------------")
    print_pause("Enter 1 to go the Jungle Route", line_delay*0.5)
    print_pause("Enter 2 to go the River Route",  line_delay*0.5)
    return verify_user_input("1", "2")

############################################################################
# JUNGLE ROUTE FUNCTIONS
############################################################################

def jr_follow_the_monkey():
    if random.randint(0,1) == 1:
        print_pause("You disturbed the monkey and they started to attack you!", line_delay)
        print_pause("You had to run away!", line_delay)
        print_pause("You did not find the doctor. You Lose!", line_delay)
    else:
        print_pause("The Monkeys are quite friendly and were owned by the doctor!", line_delay)
        print_pause("The Monkeys led you to the doctor!", line_delay)
        print_pause("You Win!", line_delay)


def jr_climb_the_three():

    print_pause("You climbed to the top of the tree and got a better view of the jungle.", line_delay)
    print_pause("You saw some smoke in the distance and decided to walk toward it.", line_delay)
    print_pause("Congratulations! You found the campsite and the doctor! You Win!", line_delay)



############################################################################

def jungle_route():
    print_pause("You entered the jungle but got lost,\n"
                "You heard strange monkey noises and you also see a tall tree.", line_delay)
    print_pause("You can follow the monkey noise or climb the tree for a better view of the jungle.", line_delay)
    print("------------------------------")
    print_pause("Enter 1 to follow the monkey noises", line_delay*0.5)
    print_pause("Enter 2 to climb the tree", line_delay*0.5)
    selection = verify_user_input("1", "2")

    if selection == "1":
        jr_follow_the_monkey()
    else:
        jr_climb_the_three()

############################################################################
# RIVER ROUTE FUNCTIONS
############################################################################

def rr_walk_away():
    print_pause("You walked away and did not find the doctor. You Lose!", line_delay)

def rr_sling_shot():
    print_pause("You scared the crocodile and it swam away.", line_delay)
    print_pause("You continued walking along the river", line_delay)
    print_pause("Congratulations! You found the campsite and the doctor!You Win!", line_delay)

###########################################################################
def river_route():
    print_pause("You started walking along the river.", line_delay)
    print_pause("After a while, you see a crocodile floating in the river.", line_delay)
    print_pause("You can walk away from the crocodile or use your sling shot to scare it away.", line_delay)
    print("------------------------------")
    print_pause("Enter 1 to walk away", line_delay*0.5)
    print_pause("Enter 2 to use your sling shot", line_delay*0.5)
    selection = verify_user_input("1", "2")

    if selection == "1":
        rr_walk_away()
    else:
        rr_sling_shot()

############################################################
def play_game():
    while True:
        selection = story_intro()
        if selection == "1":
            jungle_route()
        else:
            river_route()

        if would_you_like_to_exit_the_game():
            break

    print("Thank you for playing ... Goodbye... ")


#########################################################
play_game()