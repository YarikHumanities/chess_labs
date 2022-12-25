import chess
import random
import chess.engine
import math

class Node:
    def __init__(self, state: chess.Board, parent: 'Node', action: chess.Move):
        self.state = state
        self.parent = parent
        self.action = action

        self.unexplored_moves = list(self.state.legal_moves)
        self.color = self.state.turn
        self.children = []

        self.wins = 0
        self.simulations = 0

        random.shuffle(self.unexplored_moves)

class MctsAgent():
    def __init__(self, board: chess.Board, color: chess.Color):
        self.board = board
        self.color = color

    def algorithm(self):
        quant_of_simulations = 20;
        root = Node(self.board, None, None)

        for _ in range(quant_of_simulations):

            #SELECTION
            max_node = root
            while (not max_node.unexplored_moves) and max_node.children:
                # print(self.ucb)
                selection = max(max_node.children, key = self.ucb)
                root = selection

            leaf = root

            if len(leaf.unexplored_moves) > 0:
                child = self.expand(leaf)
            else:
                child = leaf

            score = self.simulate(child)

            # print("Before backpropagating")
            self.backup(child, score)
            # print("After backpropagating")

        print("Max move selection: ")
        move = max(root.children, key=lambda node: node.simulations)
        print(move.state)

        return move.action

    def ucb(self, node: Node):
        if node.simulations == 0:
            return float('inf')

        return (node.simulations - node.wins / node.simulations) + (math.sqrt(2) * math.sqrt(math.log(node.parent.simulations) / node.simulations))
      


    def expand(self, node: Node):
        action = node.unexplored_moves.pop()
        copy_state = node.state.copy()
        copy_state.push(action)
        child = Node(copy_state, node, action)
        node.children.append(child)

        return child

    def simulate(self, node: Node):
        board = node.state.copy()

        while not board.is_game_over():
            possible_moves = list(board.legal_moves)
            move = random.choice(possible_moves)
            board.push(move)

        score = node.state.result(claim_draw=True)

        if score == '1-0':
            wdl = chess.engine.Wdl(wins=1000, draws=0, losses=0)
        elif score == '0-1':
            wdl = chess.engine.Wdl(wins=0, draws=0, losses=1000)
        else:
            wdl = chess.engine.Wdl(wins=0, draws=1000, losses=0)

        return chess.engine.PovWdl(wdl, node.state.turn)

    def backup(self, node: Node, result: int):
        node.wins += result.pov(node.color).expectation()
        node.simulations += 1

        current_node = node
        while current_node.parent is not None:
            current_node.parent.wins += result.pov(current_node.parent.color).expectation()
            current_node.parent.simulations += 1
            current_node = current_node.parent