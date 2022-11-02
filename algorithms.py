import chess

class Negamax:
    def __init__(self, board: chess.Board, color: chess.Color, depth: int, heuristic: Heuristic):
        self.board = board
        self.color = color
        self.depth = depth
        self.heuristic = heuristic

    def negamax(self):
        if depth == self.depth:
            return 0



class heuristic:
    def __init__(self, board: chess.Board):
        self.board = board
      

    def evaluate(self, color: chess.Color):
        score = 0

        for i in range(64):

            if (self.board.piece_type_at(cell)==color):
                score = score+1

            if (self.board.color_at(cell) != color):
                score = score-1

        return score


        if (self.board.is_checkmate()):
            if (self.board.turn == color):
                score=score+(-9999)
            else:
                score=score+(9999)

        return score
