from my_packages import *
from datetime import date
import random

welcome_text = "                Welcome to the Oregon Trail! The year is 1850 and Americans are headed\n\
                out West to populate the frontier. Your goal is to travel by wagon train \n\
                from Independence, MO to Oregon(2000 miles). You start on March 1st, and \n\
                your goal is to reach Oregon by December 31st. The trail is arduous.\n\
                Each day costs you food and health. You can hunt and rest, but you have\n\
                to get there before winter!\n"

good_luck_text = "                Good luck, and see you in Oregon!"
playing = True
help_text = "\n"
miles_traveled = 0
food_remaining = 500
food_eaten = 0
health_level = 5
month = 3
day = 1
day_count = 0
sicknesses_suffered_this_month = 0
sicknesses_suffered_on_trip = 0
chance_of_sickness = 2
player_name = None
loss_text = ""


# Constants -- parameters that define the rules of the game,
# but which don't change.
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MAX_CHANCE_SICK_MONTH = 2
MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
MILES_TO_OREGON = 2000

month_name = ['omit', 'january', 'february', 'march', 'april', 'may',
              'june', 'july', 'august', 'september', 'october', 'november', 'december']

month_with_31 = [1, 3, 5, 7, 8, 10, 12]
month_with_28_29 = [2]
month_with_30 = [4, 6, 9, 11]

total_distance = 2000


def is_leap_year(year):
    leap_year = False
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        leap_year = True

    return leap_year


def february_month_count(todays_date=date.today().year):
    count = 28
    if is_leap_year(todays_date):
        count = 29
    return count

# gives the date


def date_as_string(month, day):
    print("Today is {} {}".format(month_name[month].capitalize(), str(day)))

# prints out miles remaining


def miles_remaining():
    global miles_traveled
    print("You have traveled {} miles on the trail. You have {} miles to go.  ".format(
        str(miles_traveled), str(MILES_TO_OREGON - miles_traveled)))

# return integer days in month


def days_in_month(num_of_mon):
    if num_of_mon in month_with_31:
        return 31
    elif num_of_mon in month_with_30:
        return 30
    elif num_of_mon in month_with_28_29:
        return february_month_count()
    else:
        # only correct months have days
        return 0


def random_sickness_occurs():
    global day, month, health_level, sicknesses_suffered_this_month, sicknesses_suffered_on_trip, chance_of_sickness
    if month == len(month_name):
        print("Winter has come!!")
        
    else:
        days_left = days_in_month(month) - day
        random_number = random.randint(chance_of_sickness, days_left)
        if random_number <= MAX_DAYS_PER_TRAVEL and sicknesses_suffered_this_month != MAX_CHANCE_SICK_MONTH:
            chance_of_sickness -= HEALTH_CHANGE_PER_REST
            print("You got sick!!")
            health_level -= HEALTH_CHANGE_PER_REST
            sicknesses_suffered_this_month += 1
            sicknesses_suffered_on_trip += 1


def food_consumed(number_of_days):
    global food_remaining, food_eaten
    food_remaining -= number_of_days * FOOD_EATEN_PER_DAY
    food_eaten += number_of_days * FOOD_EATEN_PER_DAY


def maybe_rollover_month():
    global day, month, chance_of_sickness,sicknesses_suffered_this_month
    if day > days_in_month(month):
        day -= days_in_month(month) 
        month += 1
        chance_of_sickness = 1
        sicknesses_suffered_this_month = 0
    
# travel: randomly moves you between 30-60 miles and randomly takes 3-7 days


def handle_travel():
    global day, miles_traveled, day_count
    dist_traveled = random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)
    days_traveled = random.randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)
    day += days_traveled
    day_count += days_traveled
    miles_traveled += dist_traveled
    print("You have traveled {} miles in {} days. You averaged {} miles each day".format(
        str(dist_traveled), str(days_traveled), str(round(dist_traveled/days_traveled, 2))))
    
    miles_remaining()
    food_consumed(days_traveled)
    maybe_rollover_month()
    random_sickness_occurs()
    

# rest: increases health 1 level with a maximum level of 5 and randomly takes 2-5 days


def handle_rest():
    global day, health_level, day_count
    days_rested = random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)
    day += days_rested
    day_count += days_rested
    if health_level != MAX_HEALTH:
        health_level += HEALTH_CHANGE_PER_REST
        print("You have rested for {} days.".format(str(days_rested)))
    else:
        print("You have rested for {} days but you are waisting time!".format(str(days_rested)))
        print("You are already at maximum health. No health added.")
    food_consumed(days_rested)
    maybe_rollover_month()
    random_sickness_occurs()
    

# hunt: adds 100 lbs of food and randomly takes 2-5 days


def handle_hunt():
    global day, food_remaining, day_count
    days_hunted = random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)
    day += days_hunted
    day_count += days_hunted
    food_remaining += FOOD_PER_HUNT
    print("You have hunted for {} days.".format(str(days_hunted)))
    food_consumed(days_hunted)
    maybe_rollover_month()
    random_sickness_occurs()
    


def handle_quit():
    global playing
    playing = False


def handle_help():
    selection = "The commands are not case sensitive. \n\
                 status or s - lists food, health, distance traveled, and day.\n\
                 travel or t - moves you between 30 - 60 miles and can use 3 - 7 days\n\
                 rest or r - increases your health by 1 and can use 2 - 5 days\n\
                 hunt or h - adds 100 lbs of food and can use 2 - 5 days\n\
                 quit or q - ends the game\n\
                 help or ? - displays the help menu\n\
        "
    print(selection)


def handle_status():
    #date_as_string(month, day)
    global month

    print('=============Status=============')
    print('Food Remaining:      \t{} lbs'.format(str(food_remaining)))
    print('Food Consumed:       \t{} lbs'.format(str(food_eaten)))
    print('Health:              \t{}/{}'.format(str(health_level),str(MAX_HEALTH))) 
    print('Distance Left:       \t{} miles'.format(
        str(MILES_TO_OREGON - miles_traveled)))
    print('Distance Traveled:   \t{} miles'.format(str(miles_traveled)))
    if day_count == 0:
        print('Avg Miles Per Day:   \t0 miles')
    else:
        print('Avg Miles Per Day:   \t{} miles'.format(str(round(miles_traveled/day_count,2))))
    print('Days Sick (Month):   \t{}'.format(str(sicknesses_suffered_this_month)))
    print('Days Sick (Total):   \t{}'.format(str(sicknesses_suffered_on_trip)))
    if month != 13:
        print('Date:                \t{} {}  ({} days on your journey)'.format(
        month_name[month].capitalize(), str(day), str(day_count)))
    else:
        print('Date:                \t{} {}  ({} days on your journey)'.format(
            month_name[1].capitalize(), str(day), str(day_count)))
    print('================================')
    


def handle_invalid_input(response):
    print("'{0}' is not a valid command. Try again.".format(response))
    print("Valid Commands: Status - s, Travel - t, Rest - r, Hunt - h, Quit - q, or Help - ?")


def game_is_over():
    global health_level, food_remaining, loss_text, month, MILES_TO_OREGON
    if health_level == 0:
        loss_text = "You have depleted your health!!"
        return True
    elif food_remaining == 0:
        loss_text = "You have run out of food!!"
        return True
    elif month >= len(month_name):
        loss_text = "Winter has come and you failed to reach Oregon!!"
        return True
    elif miles_traveled >= MILES_TO_OREGON:
        return True
    return False


def player_wins():

    if miles_traveled >= MILES_TO_OREGON:
        return True


def loss_report():
    
    print(loss_text)
    pass


clr_print()


#date_as_string(2, 13)

# handle_travel()
#print("This year is not a leap year {}, but this year is {}".format(february_month_count(),february_month_count(2028)))

#print(welcome_text + help_text + good_luck_text)
#player_name = input("\nWhat is your name, player?")

def play_game():
    global playing
    print(welcome_text + help_text + good_luck_text)
    player_name = input("\nWhat is your name, player? ")
    selection = "\n                     status or s - lists food, health, distance traveled, and day.\n\
                     help or ? - lists all the commands.\n\
                     quit or q  - will end the game.\n"
    print(selection)
    # handle_status()
    while playing:
        print()
        
        action = input("Choose an action, {0} -->".format(player_name)).lower()
        if action == "travel" or action == "t":
            handle_travel()
            handle_status()
        elif action == "rest" or action == "r":
            handle_rest()
            handle_status()
        elif action == "hunt" or action == "h":
            handle_hunt()
            handle_status()
        elif action == "quit" or action == "q":
            handle_quit()

        elif action == "help" or action == "?":
            handle_help()

        elif action == "status" or action == "s":
            handle_status()

        else:
            handle_invalid_input(action)
            pass
        if game_is_over():
            playing = False
            pass

    if player_wins():
        print("\n\nCongratulations you made it to Oregon alive!")
        handle_status()
    else:
        print("\n\nAlas! You lose.")
        loss_report()
        handle_status()
        


clr_print()
play_game()
