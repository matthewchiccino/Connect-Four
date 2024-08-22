from board_class import Board
from player_class import Player

def main():
    # Initialize the board and players
    board = Board(6, 7)  # Create a 6x7 board
    player1 = Player('X')  # Player 1 with X
    player2 = Player('O')  # Player 2 with O
    
    # Start the game loop
    current_player = player1
    while True:
        print(board)  # Display the current board
        
        # Get the current player's move
        col = current_player.next_move(board)
        board.add_checker(current_player.checker, col)
        
        # Check for win or draw
        if board.is_win_for(current_player.checker):
            print(board)
            print(f"Player {current_player.checker} wins!")
            break
        elif board.is_full():
            print(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = player1 if current_player == player2 else player2

if __name__ == "__main__":
    main()