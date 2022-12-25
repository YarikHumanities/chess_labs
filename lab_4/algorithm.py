import chess
import random


class Node:
    def __init__(self, state: chess.Board, parent: 'Node', action: chess.Move):
        self.state = state
        self.parent = parent
        self.action = action

        self.unexplored_moves = list(self.state.legal_moves)
        random.shuffle(self.unexploredMoves)
        self.color = self.state.turn
        self.children = []

        self.wins = 0
        self.simulations = 0