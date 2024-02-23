

# Some things we might want to create a connect four game
# Allowing each player to make a move
# Some sort of display (after each move perhaps?)
# Determining whether a player won the game

# Note: could extend this in the future, I suppose
class ConnectFour:
    def __init__(self, rows = 6, cols = 7):
        self.board = [[0] * cols for _ in range(rows)]
        self.board.append(['-']*cols)
        self.board.append([i for i in range(1,cols+1)])
        
        print('The board is set!', '\n')
        for i, row in enumerate(self.board):
            for col in self.board[i]:
                print(col, end=' ')
            print('\n')
    
    # Check whether an individual square is a valid square
    def valid_square(self, r, c):
        # A bit manual, but recall that there are two junk rows at the bottom
        return 0 <= r < len(self.board)-2 and 0 <= c < len(self.board[0])

    
    def check_win(self):
        # Will use this (or some form of this) to evaluate whether or not a player has won
        # Should return either 0 (no one has won), 1 (player a has won), or 2 (player b has won)
        # In the future, could extend to n players (parameter of n checking for each player)
        rows = self.check_rows()
        cols = self.check_cols()
        diagonal_right = self.check_diagonals('right')
        diagonal_left = self.check_diagonals('left')

        if rows != 0:
            return rows
        elif cols != 0:
            return cols
        elif diagonal_right != 0:
            return diagonal_right
        return diagonal_left

    def check_rows(self):
        for i in range(len(self.board)):
            cur = 0
            streak = 0
            for j in range(len(self.board[0])):
                if self.board[i][j] in (1,2):
                    if cur != self.board[i][j]:
                        cur = self.board[i][j]
                        streak = 1
                    else:
                        streak += 1
                if streak >= 4:
                    return cur
        # No one wins
        return 0
    
    # Lingering: need to fix the check diagonals function
    # Need to check all of the diagonals beginning in the top right and progressing to the bottom left
    # Top left -> bottom right for other direction
    # direction can be left (up points to left) or right (up points to right)
    def check_diagonals(self, direction):
        # Probably a less manual way to do this
        for i in range(len(self.board)-2):
            cur = 0
            streak = 0
            j = 0
            while self.valid_square(i, j):
                #print(i,j)
                #print(self.valid_square(i,j))
                if self.board[i][j] in (1,2):
                    if cur != self.board[i][j]:
                        cur = self.board[i][j]
                        streak = 1
                    else:
                        streak += 1
                if streak >= 4:
                    return cur
                if direction == 'right':
                    i -= 1
                else:
                    i += 1
                j += 1
        for j in range(len(self.board[0])):
            cur = 0
            streak = 0
            i = len(self.board)-3
            while self.valid_square(i, j):
                #print(i,j)
                #print(self.valid_square(i,j))
                if self.board[i][j] in (1,2):
                    if cur != self.board[i][j]:
                        cur = self.board[i][j]
                        streak = 1
                    else:
                        streak += 1
                if streak >= 4:
                    return cur
                if direction == 'right':
                    i += 1
                else:
                    i -= 1
                j -= 1
        return 0

    
    def check_cols(self):
        for j in range(len(self.board[0])):
            cur = 0
            streak = 0
            for i in range(len(self.board)-2):
                if self.board[i][j] in (1,2):
                    if cur != self.board[i][j]:
                        cur = self.board[i][j]
                        streak = 1
                    else:
                        streak += 1
                if streak >= 4:
                    return cur
        # No one wins
        return 0


    
    # We'll include some kind of overall 'play' function, which will control the play of game (through prompts)
    def play(self):
        game = True
        player = 1
        while game:
            valid_turn = False
            val = int(input("Make your move: "))

            # val needs to be adjusted by 1 due to 0-index
            valid_turn = self.turn(val-1, player)
            if valid_turn:
                result = self.check_win()
                if result != 0:
                    print('Player', result, 'has won the game!')
                    return result
                # Switch players
                if player == 1:
                    player = 2
                else:
                    player = 1
                
                print('Heres the games status: ', '\n')
                self.print_board()
            else:
                print('Player must find a different column')

    def print_board(self):
        for k, row in enumerate(self.board):
            for col in self.board[k]:
                print(col, end=' ')
            print('\n')
    
    # given that user inputs a row, want to check whether something is a valid move (is column within bounds, etc)
    # Then, place that players token in the correct spot of the board
    def turn(self, col, player):
        if not 0 <= col < len(self.board[0]):
            return False
        
        for i in range(len(self.board)-1, -1, -1):
            if self.board[i][col] == 0:
                self.board[i][col] = player
                self.print_board()
                return True
           
        return False

# Play the game
connectFour = ConnectFour()
connectFour.play()

print(5+6)