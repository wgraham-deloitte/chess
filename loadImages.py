import os
from PIL import Image, ImageTk

def loadPieces():
        
    paths = []
    dir = "./ChessPieces"

    for path in os.listdir(dir):
        paths.append(dir + "/" + path)

        paths.sort()

        black_pieces = []
        white_pieces = []

    for piece in paths:
        img = Image.open(piece)
        img = ImageTk.PhotoImage(img.resize((48, 48)))
        if "b_" in piece:
            black_pieces.append(img)
            continue
        white_pieces.append(img)

    return [white_pieces, black_pieces]

def loadBoard(CANVAS_WIDTH, CANVAS_HEIGHT):

    board = Image.open("chessboard-with-letters-and-numbers-vector-1071722 2.jpeg")
    board = ImageTk.PhotoImage(board.resize((CANVAS_WIDTH, CANVAS_HEIGHT)))

    return board