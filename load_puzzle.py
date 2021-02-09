import chess
import chess.variant
import json

puzzle_jsons = []
with open('crazyhouse_puzzles.json') as infile:
    for line in infile:
        puzzle_jsons.append(json.loads(line))

board = chess.variant.CrazyhouseBoard(puzzle_jsons[32]['initialfen'])
print(board)
print('WHITE' if board.turn else 'black')
print(str(board.pockets[0]), str(board.pockets[1]).upper())

# Notes on stockfish commands:
"""
stockfish

setoption name uci_variant value crazyhouse
position fen position fen rb1q1rk1/pp1bppp1/4pp2/3pP1N1/3P1N2/2N4P/PPP1B1P1/1K1R3R[BNPq] w - - 0 1
setoption name multipv value 10  # look at 10 moves
go depth 12  # parse this out into the top 10 moves at each level of depth

2r2r2/1QPbb1kp/2p1p3/3p1pp1/P2Pn1N1/8/1PP2PPP/R1BQK2R[BNPnp] w KQ - 0 1
"""
