import unittest

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

class TestTicTacToe(unittest.TestCase):
    def test_player_x_win(self):
        board = [["X", "X", "X"],
                 ["O", "O", " ",],
                 [" ", " ", " ",]]
        self.assertTrue(is_winner(board, "X"))

    def test_player_o_win(self):
        board = [["X", "X", " ",],
                 ["O", "O", "O"],
                 [" ", " ", "X",]]
        self.assertTrue(is_winner(board, "O"))

    def test_game_ongoing(self):
        board = [["X", "O", "X"],
                 ["O", "X", "O"],
                 [" ", " ", " "]]
        self.assertFalse(is_winner(board, "X"))
        self.assertFalse(is_winner(board, "O"))
        self.assertFalse(is_board_full(board))

    def test_full_board(self):
        board = [["X", "O", "X"],
                 ["O", "X", "O"],
                 ["O", "X", "O"]]
        self.assertTrue(is_board_full(board))

if __name__ == "__main__":
    unittest.main()
