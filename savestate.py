import Abkürzungen as A

IN = ["","",""]
inv = []
money = 0
orgText = ["A/01B/01C/01D/01","4w2p","0"]

def insertCharacter(file_path : str, position : int, character : int):
    with open(file_path, 'r') as f:
        indata = list(f.read())

    indata.insert(position, character)

    with open(file_path, 'w') as f:
        f.write(''.join(indata))
        
def readData(file_path : str, file_path2 : str,file_path3 : str):
    global fielddata
    global invdata
    global moneydata
    IN[0] = input('Load savestate? //broken//   y/n\n : ')
    
    
    if IN[0] == "y":
        A.p("savestate could not be loaded")
        with open(file_path,'w') as f:
            f.write(orgText[0])
            fielddata = orgText[0]
        with open(file_path2,'w') as f:
            f.write(orgText[1])
            invdata = orgText[1]
            for i in range(int(len(invdata)/2)):
                inv.append(invdata[i*2] + invdata[i*2+1])
        with open(file_path3,'w') as f:
            f.write(orgText[2])
            moneydata = orgText[2]
            
        #A.p("Savestate deleted!\n","italic")
        # with open(file_path,'r') as f:
        #     fielddata = str(f.read())
        # with open(file_path2,'r') as f:
        #     invdata = str(f.read())
        #     for i in range(int(len(invdata)/2)):
        #         inv.append(invdata[i*2] + invdata[i*2+1])
        # with open(file_path3,'r') as f:
        #         moneydata = str(f.read())
        # A.p("Savestate loaded`!\n","italic")
        
        #Strg+K  +  Strg+U -> Kommentar entfernen
    
    elif IN[0] == "n":
        with open(file_path,'w') as f:
            f.write(orgText[0])
            fielddata = orgText[0]
        with open(file_path2,'w') as f:
            f.write(orgText[1])
            invdata = orgText[1]
            for i in range(int(len(invdata)/2)):
                inv.append(invdata[i*2] + invdata[i*2+1])
        with open(file_path3,'w') as f:
            f.write(orgText[2])
            moneydata = orgText[2]
            
        A.p("Savestate deleted!\n","italic")
            
    elif IN[0] != "y" or IN[0] != "n":
        error(IN[0])
        readData(file_path,file_path2,file_path3)
    
def error(i):
    A.p(f'input error >>> {i} <<<\n',"italic")
