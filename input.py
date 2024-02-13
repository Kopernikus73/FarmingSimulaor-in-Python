import Abkürzungen as A
import savestate


field = ["","",
         "",""]
IN = ["","",""]
game = True
consoleList = ["help","field.show","legend","exit"]


legend = {"A" : "FieldCoordinate", "a" : "FieldType", "0" : "FieldLevel"}

def error(i):
    A.p(f'invalid Input >>>{i}<<<',"italic")

def getIn(t : str,i : int):
    IN[i] = input(t + "\n<player> : ")
    if IN[i] in  consoleList:
        checkIn(i)
    else:
        error(IN[i])
        getIn(t,i)

def checkIn(i : int):
    global game

    if IN[i] == consoleList[1]:
        A.p(fieldLayout())
    if IN[i] == consoleList[2]:
        print('for "Aa0" : ')
        print(legend)
    if IN[i] == consoleList[3]:
        game = False

    if IN[i] == consoleList[0]:
        print(f'{consoleList[0]}        -> Lists all available commands')
        print(f'{consoleList[1]}  -> Shows the current field layout')
        print(f'{consoleList[2]}      -> Shows the meaning of the symbols on the field')
        print(f'{consoleList[3]}        -> exits the game')



def fieldLayout():
    for i in range(int(len(savestate.fielddata)/3)):
        field[i] = savestate.fielddata[i*3] + savestate.fielddata[i*3+1] + savestate.fielddata[i*3+2]
    return field