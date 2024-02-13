import Abkürzungen as A

IN = ["","",""]
orgText = "Aa0Ba0Ca0Da0"

def insertCharacter(file_path : str, position : int, character : int):
    with open(file_path, 'r') as f:
        indata = list(f.read())

    indata.insert(position, character)

    with open(file_path, 'w') as f:
        f.write(''.join(indata))
        
def readData(file_path : str):
    global fielddata
    IN[0] = input("Spielstand laden?\n y/n\n : ")
    
    
    if IN[0] == "y":
        with open(file_path,'r') as f:
            fielddata = str(f.read())
        A.p("Spielstand geladen!\n","italic")
    
    elif IN[0] == "n":
        with open(file_path,'w') as f:
            f.write(orgText)
            fielddata = orgText
        A.p("Spielstand gelöscht!\n","italic")
            
    elif IN[0] != "y" or IN[0] != "n":
        error(IN[0])
        readData(file_path)
    
def error(i):
    A.p(f'ungültige Eingabe >>> {i} <<<\n',"italic")