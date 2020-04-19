"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def main():
    EMPTY = None
    board = [["X", "O", "X"],
             ["O", None, "O"],
             ["O", "X", "X"]]

    """
    board = [["O", "EMPTY", "EMPTY"],
             ["O", "X", "X"],
             ["X", "X", "EMPTY"]]
    """

    resultado = actions(board)

    print(resultado)


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    CounterX = 0
    CounterZero = 0
    ToReturn = "X"

    """
    Proceso iterativo por todas las casillas del tablero
    Recordatorio: índices van de 0 a 2
    Compuesto por los dos whiles, se puede reaprovechar para otras funciones cambiando lo específico
    """
    i = 0
    j = 0
    while i <= 2:
        while j <= 2:
            if board[i][j] == "X":
                CounterX = CounterX + 1
            elif board[i][j] == "O":
                CounterZero = CounterZero + 1
            j = j + 1


        i = i + 1
        j=0

    if CounterX > CounterZero:
        ToReturn = "O"

    """
    Fin de la iteración
    """




    return (ToReturn)



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Iteraremos por las posiciones del tablero, que van de 0 a 2 en ambas direcciones.
    Si la casilla está vacía añadiremos la posición a la casilla
    """

    ToReturn=set()
    i = 0
    j = 0
    while i <= 2:
        while j <= 2:
            if board[i][j] == None:
                ToReturn.add((i,j))
            j = j + 1

        i = i + 1
        j = 0


    return(ToReturn)



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Para calcular el nuevo tablero, empezaremos con un tablero que contenga en todas las posiciones el valor de Empty
    Empty está definido al principio como None.
    Es decir, creamos un tablero vacío.
    A continuación iteraremos por todas las posiciones y vamos a ponerle el mismo valor que tiene board[i][j]
    """



    newboard= [[None, None, None],[None, None, None],[None, None, None]]
    i = 0
    j = 0
    while i <= 2:
        while j <= 2:
            newboard[i][j] = board[i][j]
            j = j + 1

        i = i + 1
        j = 0




    """
    Tras esto, podemos asignarle un nuevo valor a la casilla de la acción.
    Por ello obtenemos:
        i: el valor de i es la fila de la acción --> posición con índice 0.
        j: el valor de la j es la columna de la acción --> posición con índice 1
        jugador: para saber qué jugador corresponde podemos usar la acción player con el board de entrada
        Todo esto lo haremos si la acción introducida es válida, es decir, que la casilla esté vacía
        """
    j=action[1]
    i=action[0]

    if i >=0 and i<=2 and j>=0 and j <= 2 and board[i][j]==None:
        newboard[action[0]][action[1]]=player(board)
    else:
        raise Exception ("Action is not valid. Position might be already assigned to X or O, or not even exist.")


    return(newboard)

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    i=0
    j=0
    winnerfound=False
    winner= None

    while i<=2:
        if (board[i][0] == board[i][1]) and (board[i][0] == board[i][2]) and board[i][0] != None:
            winner=board[i][0]
            found=True
            break
        i = i +1

    while j<=2 and not winnerfound:
        if board[0][j]==board[1][j] and board[0][j]==board[2][j] and board[0][j] != None:
            winner=board[0][j]
            found = True
            break

        j = j +1

    if (not winnerfound):
        if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0] != None:
            winner = board[0][0]
            found = True

        if board[2][0]==board[1][1] and board[0][2]==board[1][1] and board[0][2] != None:
            winner = board[2][0]
            found = True

    return(winner)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    terminal = False
    WinnerFound = winner(board)
    PossibleActions = actions(board)

    if (WinnerFound=="O") or (WinnerFound=="X") or (len(PossibleActions)==0):
        terminal = True
    return terminal

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    WinnerFound = winner(board)
    if WinnerFound == "X":
        ResultIs=1
    elif WinnerFound == "O":
        ResultIs=-1
    else:
        ResultIs=0

    return(ResultIs)


def minimax(board):
    if terminal(board):
        resultIs=None

    else:

        if player(board)=="X":
            ReferenceValue=-5

            for Action in actions(board):
                print(Action)
                print(result(board,Action))
                if Min_Value(result(board,Action))>ReferenceValue:
                    ReferenceValue=Min_Value(result(board,Action))
                    resultIs=Action

        if player(board)=="O":
             ReferenceValue=5
             for Action in actions(board):
                 print(Action)
                 if Max_Value(result(board,Action))<ReferenceValue:
                     ReferenceValue = Max_Value(result(board, Action))
                     resultIs=Action


    return(resultIs)







def Max_Value(board):
    if terminal(board):
        resultIs = utility(board)

    else:
        resultIs = -5
        print(actions(board))
        for Action in actions(board):
            resultIs = max(resultIs,Min_Value(result(board,Action)))


    return(resultIs)

def Min_Value(board):
    if terminal(board):
        resultIs = utility(board)

    else:
        resultIs = 5
        print(actions(board))
        for Action in actions(board):
            resultIs = min(resultIs, Max_Value(result(board, Action)))

    return(resultIs)

main()
