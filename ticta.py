import random

class TicTacToe:
    def __init__(self):
        self.board = []
        self.create_board()
    
    def create_board(self):
        for i in range (3):
            row = []
            for j in range (3):
                row.append('-')
            self.board.append(row)
    
    def display_board(self):
        for row in self.board:
            print(row)


    def checkwin(self,player):
        n = len(self.board)

        for i in range(n):
            row_win = True
            for j in range (n):
                if self.board[i][j] != player:
                    row_win = False
                    break
            if row_win:
                return True
            
        for j in range(n):
            col_win = True
            for i in range(n):
                if self.board[j][i] != player:
                    col_win = False
                    break
            if col_win:
                return True
            
        for i in range(n):
            dia1_win = True
            for i in range (n):
                if self.board[i][i] != player:
                    dia1_win = False
                    break
            if dia1_win:
                return True
        for i in range(n):
            dia2_win = True
            for i in range (n):
                if self.board[i][n-1-i] != player:
                    dia2_win = False
                    break
            if dia2_win:
                return True
    

    def computer_move(self):
        possible_moves = [index for index, value in enumerate(value in enumerate(self.board)) if value == '-']
        for player in ['O', 'X']:
            for move in possible_moves:
                board_copy = self.board[:]
                board_copy[move] = player
                if self.checkwin(player):
                    return move
        corners = [0, 2, 6, 8]
        corner_moves = [move for move in possible_moves if move in corners]
        if len(corner_moves) > 0:
            return random.choice(corner_moves)
        if 4 in possible_moves:
            return 4
        edges = [1, 3, 5, 7]
        edge_moves = [move for move in possible_moves if move in edges]
        if len(edge_moves) > 0:
            return random.choice(edge_moves)

    def play_game(self):
        self.display_board()
        while True:
            player_move = int(input("Enter a number between 1 and 9:")) - 1
            if self.board[player_move] != '-':
                print("Invalid move.")
                continue
            self.board[player_move] = 'X'
            if self.checkwin('X'):
                self.display_board()
                print("You won!")
                break
            if '-' not in self.board:
                self.display_board()
                print("Tie!")
                break

            computer_move = self.computer_move()
            self.board[computer_move] = 'O'
            self.display_board()
            if self.checkwin('O'):
                print("Computer won!")
                break
            if '-' not in self.board:
                print("Tie!")
                break

tic_tac_toe = TicTacToe()
tic_tac_toe.play_game()
        








