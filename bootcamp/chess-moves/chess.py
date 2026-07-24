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

board = parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")[-1]
# print(board)


def generate_moves(board):
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")

# Return True if the piece is white
# Return False if the piece is black
# Otherwise return None when empty 
def is_white(piece):
    if piece == ".":
        return None
    return piece.isupper()
 
# Return True if the piece is black
# Return False if the piece is white
# Otherwise return None when empty 
def is_black(piece):
    if piece == '.':
        return None
    return piece.islower()

# Check if position is within bounds   
def is_within(row, col):
    return 0 <= row <= 7 and 0 <= col <= 7

# This function governs the movement of the knight piece
def knight_moves(board, row, col):
        moves = []
        is_white_piece = is_white(board[6][6])
        
        # Knight L-shaped moves
        knight_movement = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for r, c in knight_movement:
            new_r = row + r
            new_c = col + c
            
            if is_within(new_r, new_c):
                target = board[new_r][new_c]
                # Move to empty square 
                # Or capture opponent's piece
                if target == '.' or is_white_piece != is_white(target):
                    moves.append(((row, col), (new_r, new_c)))
    
        return moves

# This function governs the movement of the king piece    
def king_moves(board, row, col):
    moves = []
    piece = board[row][col]
    is_white_piece = is_white(piece)
    
    # The king moves in 8 directions
    king_movement = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0), (1, 1)]
    
    for r, c in king_movement:
        new_row = row + r
        new_col = col + c
        
        if is_within(new_row, new_col):
            target = board[new_row][new_col]
            if target == '.' or is_white_piece != is_white(target):
                moves.append(((row, col), (new_row, new_col)))
    
    return moves

# This function governs the movement of the pawn piece 
def pawn_moves(board, row, col):
    moves = []
    piece = board[row][col]
    
    if is_white(piece):
        # White pawns move up
        #  Decreasing row, hence a direction of -1
        direction = -1
        start_row = 6
        enemy_color = is_black
    else:
        # Black pawns move down 
        # Increasing row, hence a direction of 1
        direction = 1
        start_row = 1
        enemy_color = is_white
        
        # Move forward one square
    if is_within(row + direction, col) and board[row + direction][col] == '.':
        moves.append(((row, col), (row + direction, col)))
        
        # Move forward two squares from starting position
        if row == start_row and board[row + 2 * direction][col] == '.':
            moves.append(((row, col), (row + 2 * direction, col)))
            
     # Diagonal captures
    for c in [-1, 1]:  # Left and right diagonals
        new_row = row + direction
        new_col = col + c
        if is_within(new_row, new_col):
            target = board[new_row][new_col]
            if target != '.' and enemy_color(target):
                moves.append(((row, col), (new_row, new_col)))
    
    return moves
    
# print(pawn_moves(board, -1, 2))

 # This function governs the movement of the pieces that can only move in the sliding pattern
 # These are the rook, bishop, and the queen
def generate_sliding_moves(board, row, col, directions):
    moves = []
    piece = board[row][col]
    is_white_piece = is_white(piece)
    
    for dr, dc in directions:
        for step in range(1, 8):
            new_row, new_col = row + dr * step, col + dc * step
            if not is_within(new_row, new_col):
                break
                
            target = board[new_row][new_col]
            if target == '.':
                moves.append(((row, col), (new_row, new_col)))
            elif is_white_piece != is_white(target):
                # Can capture enemy piece
                moves.append(((row, col), (new_row, new_col)))
                break  # Can't move past a piece
            else:
                break  # Blocked by own piece
    
    return moves

# print(generate_sliding_moves(board, -1, 2, [(1,2), (-1,2)]))

# This function displays the chess board as a tw-dimensional grid
def display_chess_board(board):
    length_of_row = len(board[0])
    
    for row in board:
        print(length_of_row, end=" ")
        length_of_row -= 1
        for piece in row:
            print(piece, end=" ")
        print()
        
    print("\n a b c d e f g h")
    
# display_chess_board(board)
    
