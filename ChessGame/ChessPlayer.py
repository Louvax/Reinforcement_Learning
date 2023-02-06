import chess
import random
import numpy as np
from stockfish import Stockfish

class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, board.turn)
        moves = np.argwhere(valids==1)
        return random.choice(moves)[0]

class StockFishPlayer():
    def __init__(self, game, elo=1000):
        self.stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 30})
        self.stockfish.set_elo_rating(elo)

    def play(self, board):
        self.stockfish.set_fen_position(board.fen())
        uci_move = self.stockfish.get_best_move()
        move = chess.Move.from_uci(uci_move)
        return move.from_square*64+move.to_square