import datetime
import random

def time_diff(time1, time2):
    '''
    Returns difference between two times as an integer in seconds

    Parameters
    ----------
    time1 : datetime
        The first time.
    time2 : datetime
        The second time.

    Returns
    -------
    output : int
        Time difference in seconds
    '''
    timediff = time1 - time2

    output = timediff.seconds
    return output

game_list = ["rock", "paper", "scissors"]

def mini_game(opponent):
    '''rock, paper, scissor style mini game.

    Parameters
    ----------
    opponent : str
        Name of opponent

    Returns
    -------
    status : int
        Number of points gained'''

    # start game, ask for input
    while True:
        print("Pick between rock, paper, or scissors")
        user_choice = input(">")
        if user_choice in game_list or user_choice == "gun":
            break
        else:
            print("That's not allowed idiot")
            continue
    pyma_choice = random.choice(game_list)
    # print opponent choice
    print(opponent + " picked: " + pyma_choice)
    if user_choice == "gun":
        print("You cheated but Won!!!")
        status = 3

    # win condition
    if ((user_choice == "rock" and pyma_choice == "scissors")
            or (user_choice == "scissors" and pyma_choice == "paper")
            or (user_choice == "paper" and pyma_choice == "rock")):
        status = 3
        print("You Won!!!")
    # tie condition
    if ((user_choice == "rock" and pyma_choice == "rock")
            or (user_choice == "scissors" and pyma_choice == "scissors")
            or (user_choice == "paper" and pyma_choice == "paper")):
        status = 2
        print("It's a Tie")
    # lose condition
    if ((user_choice == "rock" and pyma_choice == "paper")
            or (user_choice == "scissors" and pyma_choice == "rock")
            or (user_choice == "paper" and pyma_choice == "scissors")):
        status = 1
        print("Aw, You Lose")
    # return number of points
    return status


class Pet():
    '''The pet to play with'''
    def __init__(self):
        self.name = ''
        self.health = 100
        self.last_updated = datetime.datetime.now()
        self.alive = True
        self.happiness = 5


    def update_health(self, last_update_time):
        '''Updates the health of the pet based on current time

        Parameters
        ----------
        last_update_time : datetime
            Time to update from.
        '''
        # Calculate change in health since last update
        timediff_s = time_diff(datetime.datetime.now(), last_update_time)
        health_lost = int(round(timediff_s/20))
        health_change = self.health - health_lost

        # If new health is above 10 set pet's health to new health
        if health_change > 0:
            self.health = health_change
        # If new health is below zero set health to zero and declare pet is 
        #dead
        elif health_change <= 0:
            self.health = 0
            self.alive = False
            print("Oh no " + self.name + " has died. R.I.P")

    def update_happiness(self, last_update_time):
        '''Updates the happiness of the pet based on current time

        Parameters
        ----------
        last_update_time : datetime
            Time to update from.
        '''
        #Calculate change in happiness
        timediff_s = time_diff(datetime.datetime.now(), last_update_time)
        happ_lost = int(round(timediff_s/200))
        happ_change = self.happiness - happ_lost

        if happ_change > 0:
            self.happiness = happ_change
        # If new happiness is below zero set health to zero 
        elif happ_change <= 0:
            self.happiness = 0


    def update_status(self, last_update_time):
        '''Updates health and happiness and updates last update time

        Parameters
        ----------
        last_update_time : datetime
            Time to update from.
        '''
        self.update_health(last_update_time)
        if self.alive:
            self.update_happiness(last_update_time)

        self.last_updated = datetime.datetime.now()


    def feed_pet(self):
        '''Adds health to pet'''
        food_health = 10

        health_increase = self.health + food_health

        # if new health is more than hundred cap health at 100
        if health_increase < 100:
            self.health = health_increase
            # dip]splay point gain
            print(self.name + " has gained " + str(food_health) + 
                  " points of health")
            print(self.name + "\'s new health: " + str(self.health))
        elif health_increase >= 100:
            difference = 100 - self.health
            self.health = 100
            print(self.name + " is full!!!")
            print(self.name + " has gained " + str(difference) +
                  " points of health")
            print(self.name + "\'s new health: " + str(self.health))


    def name_pet(self, pet_name):
        '''Sets a pet's name

        Parameters
        ----------
        pet_name : str
            Name of pet.
        '''
        self.name = pet_name

 
    def display_status(self):
        '''Prints health and happiness plus any thing that needs
        attention of pet'''
        print("=================================================")
        if self.happiness == 0:
            print(self.name + " is really sad")
        #If health is very low warn player
        if self.health <= 10:
            print(self.name + " is starving!!!")
        print(self.name + '\n health: ' + str(self.health) +
              "/100\n happiness: " + str(self.happiness) + "/10")
        print("=================================================\n")


    def play_game(self):
        '''Starts happiness game'''
        # increase happiness based on result
        result = mini_game(self.name)
        original_happiness = self.happiness
        new_happ = self.happiness + result

        if new_happ < 10:
            self.happiness = new_happ
            #display point gain
            print(self.name + " gained " + str(result) +
                  " points of happiness")
            print(self.name + "\'s new happiness: " + str(self.happiness))

        elif new_happ >= 10:
            self.happiness = 10
            difference = 10 - original_happiness
            print(self.name + "is very happy!!!")
            print(self.name + " gained " + str(difference) +
                  " points of happiness")
            print(self.name + "\'s new happiness: " + str(self.happiness))


    def kill_pet(self):
        '''Kills the pet'''
        self.health = 0
        self.happiness = 0
        self.alive = False
        print("You heartlessly killed " + self.name + "\nI hope you're happy"
            + "\nYOU MONSTER")


    def punch_pet(self):
        '''punches the pet'''
        punch_health = 10
        punch_happiness = 2

        health_decrease = self.health - punch_health
        happiness_decrease = self.happiness - punch_happiness

        print("Yikes! You punched " + self.name + "\n They don't like that\n")

        # if new health is less than 0 cap health at 0
        if health_decrease > 0:
            self.health = health_decrease
            # display point loss
            print(self.name + " has lost " + str(punch_health) +
                " points of health")
            print(self.name + "\'s new health: " + str(self.health))
        elif health_decrease <= 0:
            difference = self.health
            print(self.name + " has lost " + str(difference) +
                " points of health")
            self.kill_pet()
            return

        # cap happiness at 0
        if happiness_decrease > 0:
            self.happiness = happiness_decrease
            #display point gain
            print(self.name + " lost " + str(punch_happiness) +
                 " points of happiness")
            print(self.name + "\'s new happiness: " + str(self.happiness))
        elif happiness_decrease <= 0:
            difference = self.happiness
            self.happiness = 0
            print(self.name + " is very sad!!!")
            print(self.name + " lost " + str(difference) +
                " points of happiness")
            print(self.name + "\'s new happiness: " + str(self.happiness))









        





