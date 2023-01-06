
GRID_SPACING = 80
OFFSET = 5

rookRule = []
bishopRule = []
queenRule = []

def append(list, *args):
    for i in args:
        list.append(i)
    return list

for i in range(1, 8):
    rookRule = append(rookRule, (0, i), (0, -i), (i, 0), (-i, 0))
    bishopRule = append(bishopRule, (i, i), (-i, i), (-i, -i), (i, -i))
    queenRule = append(queenRule, (0, i), (0, -i), (i, 0), (-i, 0), (i, i), (-i, i), (-i, -i), (i, -i))

rules = {   "p": [(0, 1), (0, 2), (1, 1), (-1, 1)],
            "P": [(0, -1), (0, -2), (1, -1), (-1, -1)],
            "r": rookRule
        }

print(rules.get("r"))

def getLegalMoves(board, piece, x, y):

    possibleMoves = []

    if piece == "p":
            
        if board.getPiece(x, y + 1) == "1":
            possibleMoves.append((0, 1))

            if y == 1 and board.getPiece(x, y + 2) == "1":
                possibleMoves.append((0, 2))

        if board.getPiece(x + 1, y + 1).isupper():
            possibleMoves.append((1, 1))

        if board.getPiece(x - 1, y + 1).isupper():
            possibleMoves.append((-1, 1))
    
    if piece == "P":

        if board.getPiece(x, y - 1) == "1":
            possibleMoves.append((0, -1))

            if y == 6 and board.getPiece(x, y - 2) == "1":
                possibleMoves.append((0, -2))

        if board.getPiece(x + 1, y - 1).islower():
            possibleMoves.append((1, -1))

        if board.getPiece(x - 1, y - 1).islower():
            possibleMoves.append((-1, -1))

    return possibleMoves

def highlightMoves(moves, x, y):

    highlights = []

    for i in range(len(moves)):
        
        x0, y0 = ((x + moves[i][0])*GRID_SPACING) + GRID_SPACING/2, ((y + moves[i][1])*GRID_SPACING) + GRID_SPACING/2
        x1, y1 = x0 + 10, y0 + 10
        highlights.append((x0, y0, x1, y1))
    
    return highlights