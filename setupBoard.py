from tkinter import Canvas

X_GRID = 77
Y_GRID = 73

X_OFFSET = 105
Y_OFFSET = 68

WHITE, BLACK = 0, 1
BISHOP, KING, KNIGHT, PAWN, QUEEN, ROOK = 0, 1, 2, 3, 4, 5

pieceChars = {  "r": [BLACK, ROOK],
                "n": [BLACK, KNIGHT],
                "b": [BLACK, BISHOP],
                "q": [BLACK, QUEEN],
                "k": [BLACK, KING],
                "p": [BLACK, PAWN],
                "P": [WHITE, PAWN],
                "R": [WHITE, ROOK],
                "N": [WHITE, KNIGHT],
                "B": [WHITE, BISHOP],
                "Q": [WHITE, QUEEN],
                "K": [WHITE, KING]
             }

def read(FEN: str, canvas: Canvas, pieceImages) -> Canvas:

    #layout, turn, castling, enPassent, halfmoves, fullmoves
    layout = FEN.split()[0]
    row, col = 0, 0

    for letter in layout:

        if(letter in pieceChars.keys()):
            canvas = placePiece(pieceChars[letter], row, col, canvas, pieceImages)
            row += 1
            continue

        if(letter == "/"):
            col += 1
            row = 0
            continue

        for i in range(int(letter)):
            row += 1
    
    return canvas
        
def placePiece(pieceIdx, row: int, col: int, canvas: Canvas, pieceImages) -> Canvas:

    canvas.create_image(row*X_GRID + X_OFFSET, col*Y_GRID + Y_OFFSET, image=pieceImages[pieceIdx[0]][pieceIdx[1]], anchor="nw")

    return canvas
