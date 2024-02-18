import Abkürzungen as A
import savestate
import time
import random

NormTime = time.time() / 1000000

field = ["","",
         "",""]
IN = ["","",""]
tempInv = []
game_on = True
consoleList = ["help","field.show","seed index","player.data","plant","hartvest","exit"]

class Field:
    def __init__(self,coord,type,grown,stage,value,mutation,startT):
        self.coord = coord
        self.type = type
        self.grown = grown
        self.stage = stage
        self.value = value
        self.mutation = mutation
        self.startT = startT
    
    def grow(self):
        if self.stage == 0 and self.type != "/":
            self.stage += 1
        if self.stage == 3:
            if random.randint(1,10) == 10 and self.mutation == 0:
                self.matuation = random.randint(1,10)
            self.grown == True
        else:
            self.stage += 1
    
    def shown(self):
        print("Coordinate: " + str(self.coord))
        print("Plant-Type: " + str(self.type))
        print("grown: " + str(self.grown))
        print("grow-stage: " + str(self.stage))
        print("value: " + str(self.value))
        print("mutation: " + str(self.mutation) + "\n")
        
        
        
fieldA = Field("A","/",False,0,0,0,9999999)
fieldB = Field("B","/",False,0,0,0,9999999)
fieldC = Field("C","/",False,0,0,0,9999999)
fieldD = Field("D","/",False,0,0,0,9999999)

# for i in range(int(len(savestate.fielddata)/4)):
#     field[i] = savestate.fielddata[i*4] + savestate.fielddata[i*4+1] + savestate.fielddata[i*4+2] + savestate.fielddata[i*4+3]


legend = {"A" : "FieldCoordinate", "/" : "Seed-type", "0":"Seed-Stage", "1" : "FieldLevel"}
seedsindex = {"/":"No Seed", "w/W":"Wheat-seeds/Wheat"}

def error(i):
    A.p(f'input error >>> {i} <<<',"italic")

def getIn(t : str,i : int):
    IN[i] = input(t + "\n<player> : ")
    if IN[i] in  consoleList:
        checkIn(i)
    else:
        error(IN[i])
        getIn(t,i)

def checkIn(i : int):
    global game_on
    global tempInv
    
    try:
        if fieldA.startT <= NormTime + 5: 
            fieldA.grow()
    except Exception:
        pass
    try:
        if fieldB.startT <= NormTime + 5: 
            fieldB.grow()
    except Exception:
        pass
    try:
        if fieldC.startT <= NormTime + 5: 
            fieldC.grow()
    except Exception:
        pass
    try:
        if fieldD.startT <= NormTime + 5: 
            fieldD.grow()
    except Exception:
        pass
    
    
    if IN[i] == consoleList[1]:
        print(fieldA.shown())
        print(fieldB.shown())
        print(fieldC.shown())
        print(fieldD.shown())
    if IN[i] == consoleList[2]:
        print(seedsindex)
    if IN[i] == consoleList[3]:
        print("Inventory: " + str(savestate.inv))
        print("Money: " + str(savestate.moneydata) + "€")
    if IN[i] == consoleList[4]:
        for t in range(len(savestate.inv)):
            try:
                tempInv.append(savestate.inv[t])
                int(savestate.inv[t])
                                
            except Exception:
                pass
            
        if  len(tempInv) > 0:
            print("")
            print(tempInv)
            IN[1] = input("Which crop do you want to plant?\nplant-index: ")
        if len(tempInv)  <= 0:
            print("You don't have any crops in your inventory.")
            
        if IN[1] == "w":
            for i in range(len(tempInv)):
                    for k in range(len(tempInv[i])):
                        if "w" in tempInv[i][k]:
                            if int(tempInv[i][k-1]) == 4:
                                if fieldA.type == "/":
                                    fieldA.type = "w"
                                    #field[0][1] = "w"
                                    fieldA.startT = NormTime
                                if fieldB.type == "/":
                                    fieldB.type = "w"
                                    #field[1][1] = "w"
                                    fieldB.startT = NormTime
                                if fieldC.type == "/":
                                    fieldC.type = "w"
                                    #field[2][1] = "w"
                                    fieldC.startT = NormTime
                                if fieldD.type == "/":
                                    fieldD.type = "w"
                                    #field[3][1] = "w"
                                    fieldD.startT = NormTime
                            if tempInv[i] == "3":
                                if fieldA.type == "/":
                                    fieldA.type = "w"
                                    #field[0][1] = "w"
                                    fieldA.startT = NormTime
                                if fieldB.type == "/":
                                    fieldB.type = "w"
                                    #field[1][1] = "w"
                                    fieldB.startT = NormTime
                                if fieldC.type == "/":
                                    fieldC.type = "w"
                                    #field[2][1] = "w"
                                    fieldC.startT = NormTime
                                else:
                                    if fieldD.type == "/":
                                        fieldD.type = "w"
                                        #field[3][1] = "w"
                                        fieldD.startT = NormTime
                            if tempInv[i] == "2":
                                if fieldA.type == "/":
                                    fieldA.type = "w"
                                    #field[0][1] = "w"
                                    fieldA.startT = NormTime
                                if fieldB.type == "/":
                                    fieldB.type = "w"
                                    #field[1][1] = "w"
                                    fieldB.startT = NormTime
                                else:
                                    if fieldC.type == "/":
                                        fieldC.type = "w"
                                        #field[2][1] = "w"
                                        fieldC.startT = NormTime
                                    if fieldD.type == "/":
                                        fieldD.type = "w"
                                        #field[3][1] = "w"
                                        fieldD.startT = NormTime
                            if tempInv[i] == "1":
                                if fieldA.type == "/":
                                    fieldA.type = "w"
                                    #field[0][1] = "w"
                                    fieldA.startT = NormTime
                                else:
                                    if fieldB.type == "/":
                                        fieldB.type = "w"
                                        #field[1][1] = "w"
                                        fieldB.startT = NormTime
                                    if fieldC.type == "/":
                                        fieldC.type = "w"
                                        #field[2][1] = "w"
                                        fieldC.startT = NormTime
                                    if fieldD.type == "/":
                                        fieldD.type = "w"
                                        #field[3][1] = "w"
                                        fieldD.startT = NormTime
                            print("Wheat planted!")
                                
        tempInv = []
        IN[2] = ""
    if IN[i] == consoleList[-1]:
        game_on = False

    if IN[i] == consoleList[0]:
        print(f'{consoleList[0]}        -> Lists all available commands')
        print(f'{consoleList[1]}  -> Shows the current field layout')
        print(f'{consoleList[2]}  -> Displays a list with all seeds')
        print(f'{consoleList[3]} -> shows data about the player')
        print(f'{consoleList[4]}       -> plants crops on the fields')
        print(f'#{consoleList[5]}    -> harvests all the grown plants from your fields')
        print(f'{consoleList[-1]}        -> exits the game')
