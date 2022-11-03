import chess
from algorithms import Negamax, heuristic

class Game:
    def __init__(self):
        self.board = chess.Board()
    
    def make_move(self):
        print("Making move (before Negamax)")
        agent = Negamax(self.board, self.board.turn, 1, heuristic(self.board))
        
        move = agent.get_move()
        print("Making move (after Negamax)")
        self.board.push(move)
    
    def start(self):
        while not self.board.is_checkmate():
            print("Will make move")
            self.make_move()
            print("Made move")
            print(self.board)
            print('\n')
    

game = Game()
game.start()