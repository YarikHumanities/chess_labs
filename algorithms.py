import chess

class heuristic:
    def __init__(self, board: chess.Board):
        self.board = board

    def evaluate_сell(self, cell: int, color: chess.Color) -> int:
        score = 0
        if (self.board.piece_type_at(cell)==color):
            score=score+1
        if (self.board.color_at(cell) != color):
            return score-1

        return score  

    def evaluate(self, color: chess.Color) -> int:
        score = 0

        for i in range(64):
            score += self.evaluate_сell(chess.SQUARES[i], color)
       

        if (self.board.is_checkmate()):
            if (self.board.turn == color):
                score=score+(-9999)
            else:
                score=score+(9999)

        return score


class Negamax:
    def __init__(self, board: chess.Board, color: chess.Color, depth: int, heuristic: heuristic):
        self.board = board
        self.color = color
        self.depth = depth
        self.heuristic = heuristic

    def get_move(self):
        max_move = chess.Move.null
        max_ = float('-inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.algorithm(0)
            self.board.pop()

            if score > max_:
                max_ = score
                max_move = move

        return max_move

    def algorithm(self, depth):
        if depth == self.depth:
            return self.heuristic.evaluate(self.color)

        max_ = float('-inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.algorithm(depth + 1)
            self.board.pop()

            if score > max_:
                max_ = score

        return max_


