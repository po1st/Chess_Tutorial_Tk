import tkinter as tk

# Create list to store information about square.
selected = [' ', 0, 0]

# Create a list of the board and its pieces by using lists inside a main
# list to specify rows and then can positions by using board[row][column].
board = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
]

# Lists for recognizing colors of pieces.
white = ['♙', '♖', '♘', '♗', '♕', '♔']
black = ['♟', '♜', '♞', '♝', '♛', '♚']

def draw_board(window):
    # Main board setup

    def update_board():
        # My chosen way of making the board (the whole window) update any
        # time something happens by destroying (removing) all of the objects in
        # the window and replacing them with the new ones.
        for widget in window.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()  # Remove only the canvases (chess squares), not labels or buttons
        draw_board(window)

    def move_piece(start_row, start_col, end_row, end_col):
        # A check function that listens for two squares to be clicked then calls
        # is_valid_move to check if it is a valid move, then moves the value stored
        # in the first clicked square to the second clicked square it.
        piece = board[start_row][start_col]
        target_piece = board[end_row][end_col]
        
        if piece in black:
            pcolor = "b"
        else:
            pcolor = "w"
            
        if target_piece in black:
            tcolor = "b"
        else:
            tcolor = "w"
        
        cas = 0

        if piece != ' ':
            if is_valid_move(piece, start_row, start_col, end_row, end_col):
                if target_piece == ' ' or (tcolor != pcolor):
                    if board[7][6] == ' ' and board[7][5] == ' ' and piece == '♔' and start_row == 7 and end_row == 7 and start_col == 4 and end_col == 6 and board[7][7] == '♖':
                        board[7][7] = ' '
                        board[7][5] = '♖'
                    elif board[7][1] == ' ' and board[7][2] == ' ' and board[7][3] == ' ' and piece == '♔' and start_row == 7 and end_row == 7 and start_col == 4 and end_col == 2 and board[7][0] == '♖':
                        board[7][0] = ' '
                        board[7][3] = '♖'
                    elif board[0][6] == ' ' and board[0][5] == ' ' and piece == '♚' and start_row == 0 and end_row == 0 and start_col == 4 and end_col == 6 and board[0][7] == '♜':
                        board[0][7] = ' '
                        board[0][5] = '♜'
                    elif board[0][1] == ' ' and board[0][2] == ' ' and board[0][3] == ' ' and piece == '♚' and start_row == 0 and end_row == 0 and start_col == 4 and end_col == 2 and board[0][0] == '♜':
                        board[0][0] = ' '
                        board[0][3] = '♜'
                    elif piece == '♙' and end_row == 0:
                        piece = '♕'
                    elif piece == '♟' and end_row == 7:
                        piece = '♛'
                    board[end_row][end_col] = piece
                    board[start_row][start_col] = ' '
                    update_board()

    def is_valid_move(piece, start_row, start_col, end_row, end_col):
        # This is a function used by move_piece that checks using various if rules to
        # see if the movement of a piece on the first clicked square is valid to the
        # second clicked square.
        if piece == '♟' or piece == '♙':
            # Pawn logic without jumping
            if piece == '♟':  # Black pawn
                if start_col == end_col:
                    if start_row + 1 == end_row and board[end_row][end_col] == ' ':
                        return True
                    elif start_row == 1 and start_row + 2 == end_row and board[end_row][end_col] == ' ':
                        return True
                elif abs(start_col - end_col) == 1 and start_row + 1 == end_row and board[end_row][end_col] != ' ':
                    return True
            else:  # White pawn
                if start_col == end_col:
                    if start_row - 1 == end_row and board[end_row][end_col] == ' ':
                        return True
                    elif start_row == 6 and start_row - 2 == end_row and board[end_row][end_col] == ' ':
                        return True
                elif abs(start_col - end_col) == 1 and start_row - 1 == end_row and board[end_row][end_col] != ' ':
                    return True
                
        elif piece == '♜' or piece == '♖':
            # Rook logic without jumping
            if start_row == end_row or start_col == end_col:
                if start_row == end_row:
                    for col in range(min(start_col, end_col) + 1, max(start_col, end_col)):
                        if board[start_row][col] != ' ':
                            return False
                elif start_col == end_col:
                    for row in range(min(start_row, end_row) + 1, max(start_row, end_row)):
                        if board[row][start_col] != ' ':
                            return False
                if board[end_row][end_col] == ' ' or \
                   (board[end_row][end_col] != ' ' and \
                    (piece in black and board[end_row][end_col] in white) or \
                    (piece in white and board[end_row][end_col] in black)):
                    return True
                
        elif piece == '♞' or piece == '♘':
            # Knight logic with the ability to jump over pieces
            if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
               (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
                if board[end_row][end_col] == ' ' or \
                   (board[end_row][end_col] != ' ' and \
                    (piece in black and board[end_row][end_col] in white) or \
                    (piece in white and board[end_row][end_col] in black)):
                    return True
                
        elif piece == '♝' or piece == '♗':
            # Bishop logic without jumping
            if abs(start_row - end_row) == abs(start_col - end_col):
                if start_row < end_row:
                    row_step = 1
                else:
                    row_step = -1
                if start_col < end_col:
                    col_step = 1
                else:
                    col_step = -1
                row, col = start_row + row_step, start_col + col_step
                while row != end_row and col != end_col:
                    if board[row][col] != ' ':
                        return False
                    row += row_step
                    col += col_step
                if board[end_row][end_col] == ' ' or \
                   (board[end_row][end_col] != ' ' and \
                    (piece in black and board[end_row][end_col] in white) or \
                    (piece in white and board[end_row][end_col] in black)):
                    return True
                
        elif piece == '♛' or piece == '♕':
            # Queen logic without jumping
            if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):
                if start_row == end_row:
                    for col in range(min(start_col, end_col) + 1, max(start_col, end_col)):
                        if board[start_row][col] != ' ':
                            return False
                elif start_col == end_col:
                    for row in range(min(start_row, end_row) + 1, max(start_row, end_row)):
                        if board[row][start_col] != ' ':
                            return False
                else:
                    row_step = 1 if start_row < end_row else -1
                    col_step = 1 if start_col < end_col else -1
                    row, col = start_row + row_step, start_col + col_step
                    while row != end_row and col != end_col:
                        if board[row][col] != ' ':
                            return False
                        row += row_step
                        col += col_step
                if board[end_row][end_col] == ' ' or \
                   (board[end_row][end_col] != ' ' and \
                    (piece in black and board[end_row][end_col] in white) or \
                    (piece in white and board[end_row][end_col] in black)):
                    return True
                
        elif piece == '♚' or piece == '♔':
            print("King")
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
                return True
            elif board[7][6] == ' ' and board[7][5] == ' ' and piece == '♔' and start_row == 7 and end_row == 7 and start_col == 4 and end_col == 6 and board[7][7] == '♖':
                return True
            elif board[7][1] == ' ' and board[7][2] == ' ' and board[7][3] == ' ' and piece == '♔' and start_row == 7 and end_row == 7 and start_col == 4 and end_col == 2 and board[7][0] == '♖':
                return True
            elif board[0][6] == ' ' and board[0][5] == ' ' and piece == '♚' and start_row == 0 and end_row == 0 and start_col == 4 and end_col == 6 and board[0][7] == '♜':
                return True
            elif board[0][1] == ' ' and board[0][2] == ' ' and board[0][3] == ' ' and piece == '♚' and start_row == 0 and end_row == 0 and start_col == 4 and end_col == 2 and board[0][0] == '♜':
                return True
        return False


    def on_square_clicked(event, row, col, board):
        # This is a function used to store information on what square was clicked on by the player.
        global selected 
        piece = board[row][col]
        
        if selected[0] != ' ':
            move_piece(selected[1], selected[2], row, col)
            selected[:] = [' ', 0, 0]  # Reset selected
        else:
            selected[:] = [piece, row, col]  # Update the global selected variable

    for row in range(8): # creating the board grid
        for col in range(8):
            color = '#D3D3D3' if (row + col) % 2 == 0 else '#999999'
            square = tk.Canvas(window, width=75, height=75, bg=color, highlightthickness=0)
            square.grid(row=row, column=col)
            piece = board[row][col]
            if piece != ' ':
                square.create_text(38, 38, text=piece, font=('Arial', 60), fill='black')
            square.bind("<Button-1>", lambda event, row=row, col=col, board=board: on_square_clicked(event, row, col, board))

def main():
    window = tk.Tk()
    window.title("Chess Tutorial")
    window.geometry("600x800")
    
    def done():
        title.config(text="Complete")
        text.config(text="Congrats you have completed this chess tutorial.\nThanks for playing!\n\n\n")
        button.config(command=exit, text="Close")
    
    def promotion():
        title.config(text="Pawn Promotion ♟ -> ♛")
        text.config(text="When a pawn reaches the other side of the board it is converted \ninto a queen and can be used as a queen for the rest of the \ngame or until it is taken.\n\n")
        button.config(command=done)
    
    def check():
        title.config(text="Check and Checkmate")
        text.config(text="In chess the aim of the game is to put your opponent's king in \ncheckmate. This can be accomplished by 'trapping' the king in \na position where it cannot move out of a position where it is in an \narea where a piece can take it. The term check is used to warn \nthe player that their king is in the line of fire of an opponent's piece.")
        button.config(command=promotion)
    
    def castling():
        title.config(text="Movement - Castling ♚ -> ♜")
        text.config(text="Castling is a special move available to the king and rook,\nonce the area between the rook and king's beginning\npositions are clear the player can move the king next to \nthe rook and move the rook to the other side of the king.\n")
        button.config(command=check)
    
    def movement_king():
        title.config(text="Movement - King ♚")
        text.config(text="The king can move in all directions for only 1 square, it is \nthe piece you must protect from being taken.\nIn some versions of chess the king also can't capture.\n\n")
        button.config(command=castling)
    
    def movement_queen():
        title.config(text="Movement - Queen ♛")
        text.config(text="The queen can move in all directions although it cannot move in \nL's like the knight nor can it jump over others.\n\n\n")
        button.config(command=movement_king)
    
    def movement_bishop():
        title.config(text="Movement - Bishop ♝")
        text.config(text="The bishop can only move in diagonals for example: \nFrom one corner of the board to the other.\n\n\n")
        button.config(command=movement_queen)
    
    def movement_knight():
        title.config(text="Movement - Knight ♞")
        text.config(text="The knight can only move in L shapes, for example: \nThe knight can be moved to the square 2 squares forward and \n1 left. It is also the only piece able to jump over others.\n\n")
        button.config(command=movement_bishop)
    
    def movement_rook():
        title.config(text="Movement - Rook ♜")
        text.config(text="The rook can move in only straight lines. For example: \nFrom the bottom of the board to the top, or from side to side.\n\n\n")
        button.config(command=movement_knight)
    
    def movement_pawn():
        title.config(text="Movement - Pawn ♟")
        text.config(text="The pawn can only move forward away from their side. When the \ngame starts all pawns start 2 rows away from their side, in this \nposition they can be moved forward 2 spaces. the pawn can only \ncapture in the front diagonal square from itself\n")
        button.config(command=movement_rook)

    # Create title label
    title = tk.Label(window, text="Welcome to Chess!", font=('Arial', 30), anchor="e", justify="left")
    title.grid(row=8, columnspan=8)
    
    # Create text label
    text = tk.Label(window, text="This tutorial will cover some of the basics of chess such as: \n-    Basic movement rules\n-    Castling\n-    Basic Openings\nAnd more!", font=('Arial', 20), anchor="e", justify="left")
    text.grid(row=9, columnspan=8)
    
    # Create continue button
    button = tk.Button(window, text="Continue", command=movement_pawn)
    button.grid(row=10, columnspan=8)

    draw_board(window)
    window.mainloop() # The main window loop

# This code is not a library \/
if __name__ == "__main__": 
    main()
