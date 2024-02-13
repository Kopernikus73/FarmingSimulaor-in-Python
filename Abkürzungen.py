textDic = {"": 0,"italic" : 3,"bold": 1,"underscored" : 4,"dunderscored" : 21}

def p(txt, textart: str = "") -> None:
    print(f"\033[{textDic[textart]}m{txt}\033[0m")