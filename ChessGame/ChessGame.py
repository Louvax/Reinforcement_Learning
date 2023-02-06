from Game import Game
import numpy as np
import chess


class ChessGame(Game):
    def __init__(self):
        pass

    def getInitBoard(self):
        return chess.Board()

    def getBoardSize(self):
        return (8, 8, 6)

    def getActionSize(self):
        return 8 * 8 * 73

    def getNextState(self, board, player, action):
        move = chess.Move(action // 64, action % 64)

        if not board.turn:
            move = chess.Move(
                chess.square_mirror(move.from_square),
                chess.square_mirror(move.to_square),
            )
        board = board.copy()
        if move in board.legal_moves:
            board.push(move)
        else:
            move = chess.Move.from_uci(move.uci() + "q")
            if move in board.legal_moves:
                board.push(move)
            else :
                assert False, "%s not in %s" % (str(move), str(list(board.legal_moves)))
        
        return board, -player

    def getValidMoves(self, board, player):
        valid_moves = board.legal_moves
        valids = [0]*self.getActionSize()

        for move in board.legal_moves:
            valids[move.from_square*64+move.to_square]=1
        
        return valids
    
    def getGameEnded(self, board, player):
        result = board.outcome()
        if result is None : 
            return 0
        else : 
            if result.winner is not None :
                return result.winner
            else:
                return 1e-3
    
    def getCanonicalForm(self, board, player):
        
        if board.turn :
            return board
        else:
            return board.mirror()

    def getSymmetries(self, board, pi):
        return [(board, pi)]

    def stringRepresentation(self, board):
        return board.fen()

    def toArray(self, board):
        a = [0]*(8*8*6)
        for i, j in board.piece_map().items():
            a[i*6+j.piece_type-1] = 1 if j.color else -1
        return np.array(a)


