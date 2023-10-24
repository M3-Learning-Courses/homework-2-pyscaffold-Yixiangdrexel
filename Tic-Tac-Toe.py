# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Print a row of the board
        print("-" * 9)  # Print a horizontal line separating rows

# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):  # Check each row for a win
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):  # Check each column for a win
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        # Check both diagonals for a win
        return True

    return False

# Function to check if the board is full, indicating a draw
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# The main game logic
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize an empty 3x3 board
    player = "X"  # Start with player X

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)  # Print the initial empty board

    while True:
        row, col = -1, -1  # Initialize row and column for the player's move
        while row not in [0, 1, 2] or col not in [0, 1, 2] or board[row][col] != " ":
            # Keep asking for valid input until a valid move is entered
            try:
                row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        board[row][col] = player  # Update the board with the player's move
        print_board(board)  # Print the updated board

        if check_winner(board, player):
            print(f"Player {player} wins!")  # If the current player wins, print a win message
            break
        elif is_board_full(board):
            print("It's a draw!")  # If the board is full and no one won, it's a draw
            break

        player = "O" if player == "X" else "X"  # Switch to the other player for the next turn

if __name__ == "__main__":
    main()  # Start the game when the script is run
