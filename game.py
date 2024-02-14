import savestate
import input

import Abkürzungen as A



def Game():
    A.p("Welcome to Farming Simulator!\n","bold")
    input.getIn('Type "help" to get and overview of all commands',0)
    while input.game_on:
        input.getIn("",0)


if __name__ == "__main__":
    savestate.readData(r'saves\fieldsave.txt',r'saves\invsave.txt',r'saves\moneysave.txt')
    Game()
