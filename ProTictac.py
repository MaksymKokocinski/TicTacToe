#------TicTacToe------
def startgra():
    tablica()
    print("Kto zaczyna?")
    wejscie2 = input()
    if wejscie2 =="info":
        info()
    elif wejscie2 =="kolko":
        kolko()
    elif wejscie2 =="krzyzyk":
        krzyzyk()
    else:
        print("Wpisz kolko lub krzyzyk lub info")
        startgra()


def tablica():
    print("",t[0],"|",t[1],"|",t[2],"\n"
    ,t[3],"|",t[4],"|",t[5],"\n"
    ,t[6],"|",t[7],"|",t[8])

def info():
        print("Na poczatku wybierasz wpisujac: kolko lub krzyzyk")
        print("A pole wybierasz wpisujac kolejno: gl gs gp sl ss sp dl ds dp")
        startgra()
def infokolko():
        print("Na poczatku wybierasz wpisujac: kolko lub krzyzyk")
        print("A pole wybierasz wpisujac kolejno: gl gs gp sl ss sp dl ds dp")
def infokrzyzyk():
        print("Na poczatku wybierasz wpisujac: kolko lub krzyzyk")
        print("A pole wybierasz wpisujac kolejno: gl gs gp sl ss sp dl ds dp")
 
def kolko():
    if checkwygrana():
        return
    if checkremis():
        return
    checkwygrana()
    wejscie3 = input("Kolej O: ")
    if wejscie3 =="gl":
        if t[0] =="-":
            t[0]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="gs":
        if t[1] =="-":
            t[1]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="gp":
        if t[2] =="-":
            t[2]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="sl":
        if t[3] =="-":
            t[3]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="ss":
        if t[4] =="-":
            t[4]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="sp":
        if t[5] =="-":
            t[5]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="dl":
        if t[6] =="-":
            t[6]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="ds":
        if t[7] =="-":
            t[7]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="dp":
        if t[8] =="-":
            t[8]="O"
            tablica()
            krzyzyk()
        else:
            print("To pole jest juz zajete")
            kolko()
    elif wejscie3 =="info":
        infokolko()
        kolko()
    elif wejscie3 =="koniec":
        return
    else:
        print("Zle wpisales pole, zobacz info jak nie wiesz co wpisac")
        kolko()

def krzyzyk():
    if checkwygrana():
        return
    if checkremis():
        return
    checkwygrana()
    wejscie3 = input("Kolej X: ")
    if wejscie3 =="gl":
        if t[0] =="-":
            t[0]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="gs":
        if t[1] =="-":
            t[1]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="gp":
        if t[2] =="-":
            t[2]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="sl":
        if t[3] =="-":
            t[3]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="ss":
        if t[4] =="-":
            t[4]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="sp":
        if t[5] =="-":
            t[5]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="dl":
        if t[6] =="-":
            t[6]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="ds":
        if t[7] =="-":
            t[7]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="dp":
        if t[8] =="-":
            t[8]="X"
            tablica()
            kolko()
        else:
            print("To pole jest juz zajete")
            krzyzyk()
    elif wejscie3 =="info":
        infokrzyzyk()
        krzyzyk()
    elif wejscie3 =="koniec":
        return

    else:
        print("Zle wpisales pole, zobacz info jak nie wiesz co wpisac")
        krzyzyk()

def checkwygrana():
    #poziom X
    if t[0] =="X" and t[1] =="X" and t[2]=="X":
        print("Wygral X ")
        return True
    elif t[3] =="X" and t[4] =="X" and t[5]=="X":
        print("Wygral X ")
        return True
    elif t[6] =="X" and t[7] =="X" and t[8]=="X":
        print("Wygral X ")
        return True
    #pion X
    elif t[0] =="X" and t[3] =="X" and t[6]=="X":
        print("Wygral X ")
        return True
    elif t[1] =="X" and t[4] =="X" and t[7]=="X":
        print("Wygral X ")
        return True
    elif t[2] =="X" and t[5] =="X" and t[8]=="X":
        print("Wygral X ")
        return True
    #krzyzyk X
    elif t[0] =="X" and t[4] =="X" and t[8]=="X":
        print("Wygral X ")
        return True
    elif t[2] =="X" and t[4] =="X" and t[6]=="X":
        print("Wygral X ")
        return True
    #poziom O
    if t[0] =="O" and t[1] =="O" and t[2]=="O":
        print("Wygral O ")
        return True
    elif t[3] =="O" and t[4] =="O" and t[5]=="O":
        print("Wygral O ")
        return True
    elif t[6] =="O" and t[7] =="O" and t[8]=="O":
        print("Wygral O ")
        return True
    #pion O
    elif t[0] =="O" and t[3] =="O" and t[6]=="O":
        print("Wygral O ")
        return True
    elif t[1] =="O" and t[4] =="O" and t[7]=="O":
        print("Wygral O ")
        return True
    elif t[2] =="O" and t[5] =="O" and t[8]=="O":
        print("Wygral O ")
        return True
    #krzyzyk O
    elif t[0] =="O" and t[4] =="O" and t[8]=="O":
        print("Wygral O ")
        return True
    elif t[2] =="O" and t[4] =="O" and t[6]=="O":
        print("Wygral O ")
        return True
    else:
        return 

def checkremis():
    if (t[0]=="X"or t[0]=="O") and (t[1]=="X"or t[1]=="O") and (t[2]=="X"or t[2]=="O") and (t[3]=="X"or t[3]=="O") and (t[4]=="X"or t[4]=="O") and (t[5]=="X"or t[5]=="O") and (t[6]=="X"or t[6]=="O") and (t[7]=="X"or t[7]=="O") and (t[8]=="X"or t[8]=="O"):
        print("Remis")
        return True



def replay():
    print("Chcesz zagrac jeszcze raz?")
    wejscie4 = input()
    if wejscie4=="tak":
        startgra()
    elif wejscie4=="nie":
        return True
    else:
        print("Wpisz tak lub nie")
        return

def start():
    print("Chcesz zagrac w tictactoe?")
    wejscie = input()

    if wejscie =="tak":
        print("Jesli grasz pierwszy raz to napisz: info")
        startgra()
        return True
    elif wejscie =="nie":
        print("Jak nie to eloo")
        return False    
    
    else:
        print("Wpisz tak lub nie")
        
      
t = list("---------")
x = 1

#start()
if start():
    while x != 0:
        t = list("---------")
        #replay()
        if replay():
            break
    



