import chess
import chess.engine
import random
import math

from algorithm import Node
class Heuristic():
    def evaluate(board: chess.Board, color: chess.Color):
        return 0


class MctsAgent():
    def __init__(self, board: chess.Board, color: chess.Color, heuristic: Heuristic):
        self.board = board
        self.color = color
        self.heuristic = heuristic

    def get_move(self):
        return 0

    def algorithm(self):
        return 0

    