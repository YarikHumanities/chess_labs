import chess
import chess.engine
import random
import math

from algorithm import Node
from algorithm import MctsAgent

class Game:
    def __init__(self):
        self.board = chess.Board()

    def makeAgentMove(self):
        agent = MctsAgent(self.board, self.board.turn)
        move = agent.algorithm()
        self.board.push(move)

    def start(self):
        while not self.board.is_checkmate():
            print("Before move")
            self.makeAgentMove()
            print("After move")
            print(self.board)
            print('\n')


game = Game()
game.start()

    