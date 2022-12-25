import chess
from algorithms import Negamax, heuristic, Nega_scout, Pvs

class Game:
    def __init__(self):
        self.board = chess.Board()
    
    def make_move(self):
        #print("Making move (before Negamax)")
        agent = Pvs(self.board, self.board.turn, 3, heuristic(self.board))
        
        move = agent.get_move()
        print("Making move (after Pvs)")
        self.board.push(move)
        
    def make_move_alternative(self):
        agent = Negamax(self.board, self.board.turn, 3, heuristic(self.board))
        
        move = agent.get_move()
        print("Making move (after Negamax)")
        self.board.push(move)

    def start(self):
        while not self.board.is_checkmate():
            #flag = 1
            print("Will make move")

            # if(self.board.turn == chess.WHITE):
            #     self.make_move()
            # if(self.board.turn == chess.BLACK):
            #     self.make_move_alternative()
            self.make_move()

            print("Made move")
            print(self.board)
            print('\n')
    

game = Game()
game.start()