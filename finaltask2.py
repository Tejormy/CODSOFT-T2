import math
AI = 'O'
EMPTY = ' '

def create_board():
    return [EMPTY] * 9

def print_board(board):
    print(f'''
      {board[0]} | {board[1]} | {board[2]} 
     -----------
      {board[3]} | {board[4]} | {board[5]} 
     -----------
      {board[6]} | {board[7]} | {board[8]} 
    ''')

def is_winner(board, player_marker):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],                                                                                                                                               
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]          ]
    return any(all(board[i] == player_marker for i in combo) for combo in win_conditions)

def is_board_full(board):
    return all(spot != EMPTY for spot in board)

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]

def minimax(board, depth, is_maximizing, alpha, beta, player_marker, ai_marker):
    if is_winner(board, ai_marker):
        return 10 - depth
    elif is_winner(board, player_marker):
        return depth - 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = ai_marker
            eval = minimax(board, depth + 1, False, alpha, beta, player_marker, ai_marker)
            board[move] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = player_marker
            eval = minimax(board, depth + 1, True, alpha, beta, player_marker, ai_marker)
            board[move] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, player_marker, ai_marker):
    best_value = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = ai_marker
        move_value = minimax(board, 0, False, -math.inf, math.inf, player_marker, ai_marker)
        board[i] = EMPTY
        if move_value > best_value:
            best_value = move_value
            move = i
    return move

def play_game():
    board = create_board()
    
    player_name = input("Enter your name: ")
    player_marker = 'X'
    
    print(f"Welcome to Tic-Tac-Toe, {player_name}!")
    print_board(board)

    while True:
        move = int(input(f"{player_name}, enter your move (1-9): ")) - 1
        if board[move] != EMPTY:
            print("Invalid move! Try again.")
            continue

        board[move] = player_marker
        print_board(board)

        if is_winner(board, player_marker):
            print(f"Congratulations, {player_name}! You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        ai_move = best_move(board, player_marker, AI)
        board[ai_move] = AI
        print("AI move:")
        print_board(board)

        if is_winner(board, AI):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
