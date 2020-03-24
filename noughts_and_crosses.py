# Gra "Kółko i krzyżyk"

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
  print(
  """
  Instrukcja do gry \"Kółko i krzyżyk\"
  Swoje posunięcia wskażesz poprzez wprowadzenie liczby z zakresu 1 do 9.
  Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
  """  
  )

def ask_yes_no(question):
    """Pytanie, na które można odopowiedzieć tak lubi nie."""
    
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Popros o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range (low+1, high+1):
        response = int(input(question))
    return response

def pieces():
    """Ustalamy czy pierwszy ruch należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("A więc pierwszy ruch należy do Ciebie.")
        human = X
        computer = O
    else:
        print("Komputer wykonuje pierwszy ruch")
        computer = X
        human = O 
       
    return computer, human

def new_board():
    """Tworzymy nowa plansze do gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Wyswietl plansze gry na ekranie"""
    print("\n\t", board[0] ,"|" , board[1] , "|" , board[2])
    print ("\n\t", "---------" )
    print("\n\t", board[3] ,"|" , board[4] , "|" , board[5])
    print ("\n\t", "---------" )
    print("\n\t", board[6] ,"|" , board[7] , "|" , board[8])
    print ("\n\t", "---------" )

def legal_moves(board):
    """Tworzymy listę prawidłowych ruchów"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Ustal zwycięscę gry"""
    WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
    
    for row in WAYS_TO_WIN: 
        if board[row[0]] == board[row[1]] == board [row[2]] != EMPTY:
            winner = board[row[0]]
            return winner        
    
    if EMPTY not in board:
        return TIE
    
    return None   

def human_move(board, human):
   """Oczyt ruchu człowieka"""
   legal = legal_moves(board)
   move = None
   while move not in legal:
        move = (ask_number("Jaki będzie twój ruch ( 1 - 9):", 0, NUM_SQUARES))-1
        if move not in legal:
            print("\nTo pole jest już zajęte, wybierz inne. \n")
    
   print("Świetnie ...")
   return move 

def computer_move(board, computer, human):
    """Spowoduje wykonanie ruchu przez komputer."""
    #tworzymy kopię roboczą ponieważ funkcja będzie zmieniać listę
    board = board[:]
    
    #najlepsza pozycja do zajęcia wg. kolejnosci
    
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7) 
    
    
    print("Wybieram pole numer:", end="")
    
    #jesli komputer może wygrać wykonaj ten ruch

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
                print(move)
                return move
        #ten ruch zostal sprawdzony wycofaj go
        board[move]=EMPTY

    #jesli człowiek może wygrać, zablokuj ten ruch:
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # poniewaz nikt nie moze wygrac w nastepnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print (move+1)
            return move
 
def next_turn(turn):
    """Zmień wykonawcę ruchu."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwycięzcy"""
    if the_winner != TIE:
        if the_winner == None:
            print("Brak zwycięscy\n")    
        else:    
            print (the_winner, "jest zwycięscą!\n")
    else:
        print("Remis\n")
    
    if the_winner == computer:
        print ("Tym razem wygrał komputer\n")
    elif the_winner == human:
        print ("Tym razem wygrał człowiek\n")
    elif the_winner == TIE:
        print ("Doszło do remisu\n")
    
            
    
    

    
    
def main():
  
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board) 
    
    while not winner(board):
        if turn == human:
            move = human_move(board, human) 
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        
        the_winner = winner(board)
        congrat_winner(the_winner, computer, human)
        
        
#rozpoczecie programu
main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")