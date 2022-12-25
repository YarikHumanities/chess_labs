import chess

class heuristic:
    def __init__(self, board: chess.Board):
        self.board = board
        self.points = {
            chess.PAWN: 1,
            chess.BISHOP: 3,
            chess.KNIGHT: 4,
            chess.ROOK: 5,
            chess.QUEEN: 8
        }

    def evaluate(self, color: chess.Color) -> int:
        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]
        score = self.material_balance() * (white - black)

        if (self.board.turn != color):
            return -score

        return score
        
    def material_balance(self):
        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]
        return (
            chess.popcount(white & self.board.pawns) - chess.popcount(black & self.board.pawns) +
            3 * (chess.popcount(white & self.board.knights) - chess.popcount(black & self.board.knights)) +
            3 * (chess.popcount(white & self.board.bishops) - chess.popcount(black & self.board.bishops)) +
            5 * (chess.popcount(white & self.board.rooks) - chess.popcount(black & self.board.rooks)) +
            9 * (chess.popcount(white & self.board.queens) - chess.popcount(black & self.board.queens))
        )

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


class Nega_scout:
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
            score = -self.algorithm(0, float('-inf'), float('inf'))
            self.board.pop()

            if score > max_:
                max_ = score
                max_move = move

        return max_move

    def algorithm(self, depth, alpha, beta):
        if depth == self.depth:
            return self.heuristic.evaluate(self.color)
        a = alpha
        b = beta
        i = 0
        for move in self.board.legal_moves:

            self.board.push(move)

            score = -self.algorithm(depth + 1, -b, -a)

            self.board.pop()

            if (score > alpha and score < beta and depth < self.depth - 1 and i > 0):
                a = -self.algorithm(depth + 1, -beta, -score)

            if score > a:
                a = score

            if a >= beta:
                return a

            b = a + 1
            i += 1

        return a
    
class Pvs:
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
            score = -self.algorithm(0, float('-inf'), float('inf'))
            self.board.pop()

            if score > max_:
                max_ = score
                max_move = move

        return max_move

    def algorithm(self, depth, alpha, beta):
        if depth == self.depth:
            return self.heuristic.evaluate(self.color)

        bSearchPv = True
        for move in self.board.legal_moves:
            self.board.push(move)

            if bSearchPv:
                #search with normal window
                score = -self.algorithm(depth + 1, -beta, -alpha)
            else:
                #search with null window
                score = -self.algorithm(depth + 1, -alpha - 1, -alpha)

                #if it failes high, do a full re-search
                if score > alpha and score < beta:
                    score = -self.algorithm(depth + 1, -beta, -alpha)

            self.board.pop()

            if (score >= beta):
                return beta

            if (score > alpha):
                alpha = score
                bSearchPv = False

        return alpha