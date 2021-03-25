import project_module.pyma_module
from project_module.pyma_module import Pet
import cmd

game_active = True
Pymagotchy = Pet()

def refresh_game():
    '''after every player move refresh stauts and display on screen'''
    Pymagotchy.update_status(Pymagotchy.last_updated)
    Pymagotchy.display_status()
    if not Pymagotchy.alive:
        return True


class PymagotchyCmd(cmd.Cmd):
    ''' Cmd class that starts a cmd loop. From cmd module'''
    prompt = "\n>"
    def default(self, arg):
        print("I do not understand that command." +
              "\nType \"help\" for a list of commands.")

    def do_feed(self, arg):
        '''feeds the pet if alive'''
        life = refresh_game()
        if not life:
            Pymagotchy.feed_pet()

        return life


    def do_hi(self, arg):
        '''say hi to pet and way for player to check status'''
        life = refresh_game()
        if not life:
            if Pymagotchy.happiness != 10:
                print(Pymagotchy.name + " says hi")
            elif Pymagotchy.happiness == 10:
                print(Pymagotchy.name + " is very happy to see you")
                print(Pymagotchy.name + " says hi")

        return life


    def do_kill(self, arg):
        '''kill your pet'''
        while True:
            print("Are you sure you want to kill " + Pymagotchy.name +
                  "?\n y: yes n: no")
            y_or_n = input(">")

            if y_or_n == "y":
                Pymagotchy.kill_pet()
                return True
            elif y_or_n == "n":
                break
            else:
                print("Please try again")
                continue


    def do_play(self, arg):
        '''starts mini game'''
        life = refresh_game()
        if not life:
            Pymagotchy.play_game()

        return life


    def do_punch(self, arg):
        '''punches pet'''
        life = refresh_game()
        if not life:
            Pymagotchy.punch_pet()
        if Pymagotchy.alive == False:
            return True
        return life

    def help_play(self):
        '''gives description of play command'''
        print("Play with your pet.\n Pick between rock, paper or scissors " +
              "Makes your pet happy. Your pet becomes more happy if you win")

    def help_feed(self):
        '''gives description of feed command'''
        print("Feed your pet. \n Gives your pet 10 health points")

    def help_hi(self):
        '''gives description of hi command'''
        print("Say hi to your pet.\n Allows you to check your pet's status")

    def help_kill(self):
        '''gives description of kill command'''
        print("Kill your pet.")

    def help_punch(self):
        '''gives description of punch command'''
        print("Punch your pet.\n Leads to decrease in health and happiness")

while game_active == True:
    # start script
    print("\n\n\n______                                  _       _     _" +
          "\n| ___ \\                                | |     | |   (_)" 
          "\n| |_/ /   _ _ __ ___   __ _  __ _  ___ | |_ ___| |__  _ " 
          "\n|  __/ | | | '_ ` _ \\ / _` |/ _` |/ _ \\| __/ __| '_ \\| |" 
          "\n| |  | |_| | | | | | | (_| | (_| | (_) | || (__| | | | |" 
          "\n\\_|   \\__, |_| |_| |_|\\__,_|\\__, |\\___/ \\__\\___|_| |_|_|" 
          "\n      __/ |                 __/ |                       "
          "\n      |___/                 |___/                        ")
    print("=================================================")
    print("WELCOME TO PYMAGOTCHY")
    print("=================================================\n\n")
    Pymagotchy.name = ''
    while Pymagotchy.name == '':
        print("Enter a name for your Pymagotchy: ")
        Pymagotchy.name = input('>')

    print("\nHello " + Pymagotchy.name)
    print(" .^._.^."
          "\n | . . |"
          "\n(  ---  )"
          "\n.'     '."
          "\n|/     \\|"
          "\n \\ /-\\ /"
          "\n  V   V")
    print("\nType help for a list of commands")
    print("=================================================")
    # command loop
    PymagotchyCmd().cmdloop()

    while True:
        print("\nDo you want to restart the game? \n y: yes n: no")
        y_or_n = input(">")
        if y_or_n == "y":
            # initialize new Pet before restart
            Pymagotchy = Pet()
            break
        elif y_or_n == "n":
            game_active = False
            break
        else:
            # keep looping till yes or no
            print("Please try again")
            continue

print("\nGoodbye, I hope you had fun!")
