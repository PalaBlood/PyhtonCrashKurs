field = ["",
             "1", "2", "3", 
             "4", "5", "6",
             "7", "8", "9"]

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3] + "\n" + 
          field[4] + "|" + field[5] + "|" + field[6] + "\n" + 
          field[7] + "|" + field[8] + "|" + field[9] )





def spiel_gewonnen():
    if field[1] == field[2] == field[3]: 
        return True
    elif field[4] == field[5] == field[6]:
        return True
    elif field[7] == field[8] == field[9]:
        return True
    elif field[1] == field[4] == field[7]: 
        return True
    elif field[2] == field[5] == field[8]: 
        return True
    elif field[3] == field[6] == field[9]: 
        return True
    elif field[1] == field[5] == field[9]: 
        return True
    elif field[3] == field[5] == field[7]: 
        return True
    else: 
        return False




def start_game():
    while not spiel_gewonnen():
        print_field()
        response = input("Spieler1: Wähle ein Feld zwischen 1 und 9 aus: ")
        if response in field: 
            field[int(response)] = "x"
        else: 
            print("Bitte wähle einen gültigen Bereich aus")
            
        print_field()
        response2 = input("Spieler2: Wähle ein Feld zwischen 1 und 9 aus: ")
        if response2 in field: 
            field[int(response2)] = "O"
        else: 
            print("Bitte wähle einen gültigen Bereich aus")
            
    print("Spiel vorbei!")
    print_field()
      
                    
start_game()