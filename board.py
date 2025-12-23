class Board:
    def __init__(self):
        self._board = [[0 for _ in range(7)] for _ in range(6)]
        self._ROW_LEN = 6
        self._COL_LEN = 7

    def __str__(self):
        # Provide a readable string representation of the board
        return "\n".join("|".join(str(cell) for cell in row) for row in self._board)

    def print_board(self) -> None:
        # Print the pretty representation of the board
        print(f"board: \n\n{self}\n")
        
    def _can_place(self, col: int) -> bool: 
        for row in range(5, -1, -1):
            if self._board[row][col] == 0:
                return True
        return False
    
    def place_disc(self, col: int, disc: int) -> int:
        if self._can_place(col):
            for row in range(5, -1, -1):
                if self._board[row][col] == 0:
                    self._board[row][col] = disc
                    return row
        return -1
    
    def check_board_full(self) -> bool:
        """Return True if no more discs can be placed.
        In normal play this is equivalent to checking that every top cell is non-zero,
        because discs stack from the bottom up."""
        for col in range(self._COL_LEN):
            if self._board[0][col] == 0:
                return False
        return True
    
    def check_win(self, disc: int, row: int, col: int) -> bool:
        if any(
            self._check_horizontal_win(disc, row, col),
            self._check_vertical_win(disc, row, col),
            self._check_diagnol_down_win(disc, row, col),
            self._check_horizontal_win(disc, row, col)
        ): return True
        
        return False
        
    def _check_horizontal_win(self, disc: int, row: int, col: int) -> bool:
        count = 1
        for cur_col in range(col - 1, col - 4, - 1):
            if self._check_cell(row, cur_col) == disc:
                count += 1
            else:
                break
                        
        for cur_col in range(col + 1, col + 4, + 1):
            if self._check_cell(row, cur_col) == disc:
                count += 1
            else:
                break
        
        return count >= 4
    
    def _check_vertical_win(self, disc: int, row: int, col: int) -> bool:
        count = 1
        
        for cur_row in range(row - 1, row - 4, - 1): 
            if self._check_cell(cur_row, col) == disc:
                count += 1
            else:
                break
        
        for cur_row in range(row + 1, row + 4, + 1):
            if self._check_cell(cur_row, col) == disc:
                count += 1
            else:
                break
        
        return count >= 4
    
    
    def _check_diagnol_down_win(self, disc: int, row: int, col: int) ->  bool:
        count = 1
        
        cur_row = row - 1
        cur_col = col - 1
        for _ in range(4):
            if self._check_cell(cur_row, cur_col) == disc:
                count += 1
                
                cur_row -= 1
                cur_col -= 1
            else:
                break
            
        cur_row = row + 1
        cur_col = col + 1
        for _ in range(4):
            if self._check_cell(cur_row, cur_col) == disc:
                count += 1
                
                cur_row += 1
                cur_col += 1
            else:
                break
            
        return count >= 4

    def _check_diagnol_up_win(self, disc: int, row: int, col: int) -> bool:
        count = 1
        
        cur_row = row + 1
        cur_col = col - 1
        for _ in range(4):
            if self._check_cell(cur_row, cur_col) == disc:
                count += 1
                
                cur_row += 1
                cur_col -= 1
            else:
                break
        
        cur_row = row - 1
        cur_col = col + 1
        for _ in range(4):
            if self._check_cell(cur_row, cur_col) == disc:
                count += 1
                
                cur_row -= 1
                cur_col += 1
            else:
                break
            
        return count >= 4
            
        
    def _check_cell(self, row: int, col: int) -> int:
        if 0 <= row < self._ROW_LEN and 0 <= col < self._COL_LEN:
            return self._board[row][col]
        


# vertical row + 1, row + 2, row + 3, row - 1, row -2, row -3
# horizontal col + 1, col + 2, col + 3, col -1, col - 2, col - 3
# diagnol going down row - 1, col +1/-1 
# diagnol going up row + 1, col +1/-1 

test_board = Board()
test_board.print_board()
# test_board.place_disc(2, 1)
# test_board.place_disc(1, 1)
# test_board.place_disc(0, 1)
# test_board.place_disc(3, 1)
# test_board.print_board()
# print(test_board._check_horizontal_win(1, 5, 2))

# Minimal checks for check_board_full
# (top-row check is reliable when using place_disc; direct board mutation can break this invariant)
assert test_board.check_board_full() is False

# Simulate a full board by filling every top cell and re-check
for c in range(test_board._COL_LEN):
	test_board._board[0][c] = 1
assert test_board.check_board_full() is True
