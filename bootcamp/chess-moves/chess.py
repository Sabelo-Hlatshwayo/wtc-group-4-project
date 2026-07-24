def parse_fen(fen):
    # List unpacking. Unpacking the elements from the list and storing them in individual varoable
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ") 
   
    # This our data model. A list of lists. Each inner list represents a row of the chess board, so we have 8 inner lists
    pieces = [[]] 
    
    # This logic creates the chess board
    for char in fen_pieces:
        if char.isdigit():
            pieces[-1].extend(["*"] * int(char))
        elif char == "/":
            pieces.append([])
        else:
            # Place the pieces on the board
            pieces[-1].append(char)
        
    return fen_pieces, to_move, castling_rights, ep, int(hm), int(fm), pieces

board = parse_fen("rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1")[-1]
# print(board)


def generate_moves(board):
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")

def display_chess_board(board):
    length_of_row = len(board[0])
    
    for row in board:
        print(length_of_row, end=" ")
        length_of_row -= 1
        for piece in row:
            print(piece, end=" ")
        print()
        
    print("\n a b c d e f g h")
    
display_chess_board(board)
    
