from board import Board
from player import Player
from enum import Enum

#orchestrator to keep track of game state
#run_game -> player win or draw
    # -> runs game until complete
    
#reset game
    # resets state
    
#start new game
    
#check turn

#switch turn

class GameState(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    WON = "Won"
    DRAW = "Draw"

class Game:
    def __init__(self):
        self._player1 = None
        self._player2 = None
        self._board = Board()
        self._turn = self._player1
        self._game_state = GameState.NOT_STARTED
        
    def start_new_game(self) -> None:
        self._board = Board()
        print("New Game Started \n")
        player1 = input("Please enter first player name: \n\n")
        player2 = input("Please enter second player name: \n\n")
        self._player1 = Player(player1, 1)
        self._player2 = Player(player2, 2)
        self._turn = self._player1
        self._game_state = GameState.IN_PROGRESS
        self.run_game()
        
    def _switch_turn(self) -> None:
        self._turn = self._player2 if self._turn == self._player1 else self._player1
    
    def _make_move(self) -> tuple:
        move = input(f"{self._turn.name} please choose a column: \n")
        
        while not self._validate_move(move):
            move = input("Please choose a valid column: \n")

        col = int(move.strip()) - 1
        row = self._board.place_disc(col, self._turn.number)
        
        return (row, col)
        
    def _validate_move(self, move: str) -> bool:
        possible_move = move.strip()
        
        if possible_move.isdigit() and 0 < int(possible_move) < 8:
            if self._board.can_place(int(possible_move) - 1):
                return True
        return False
    
    def run_game(self) -> None:
        while self._game_state == GameState.IN_PROGRESS:
            self._display_turn()
            self._board.print_board()
            
            row, col = self._make_move()
            
            if self._board.check_board_full():
                self._game_state = GameState.DRAW
                
            if self._board.check_win(self._turn.number, row, col):
                self._game_state = GameState.WON
            
            if self._game_state == GameState.IN_PROGRESS:
                self._switch_turn()
        
        self._board.print_board()
        
        if self._game_state == GameState.WON:
            self._display_winner()
            
        if self._game_state == GameState.DRAW:
            self._display_draw()
            
    def _display_turn(self) -> None:
        print(f"{self._turn.name}'s turn \n")
                    
    def _display_winner(self) -> None:
        print(f"{self._turn.name} won!! \n")
        
    def _display_draw(self) -> None:
        print("Its a draw! \n")
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
    
        
        
    
        
        
    