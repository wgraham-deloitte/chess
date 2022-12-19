from tkinter import Tk, Canvas, Frame, BOTH
from PIL import Image, ImageTk
import os

GRIDSPACING = 80
BOARD_OFFSET = 5
PIECE_OFFSET = 13

WHITE, BLACK = 0, 1
BISHOP, KING, KNIGHT, PAWN, QUEEN, ROOK = 0, 1, 2, 3, 4, 5

def makeBoard(canvas: Canvas) -> Canvas:

    darkSquare = True
    for row in range(8):

        darkSquare = not darkSquare
        for column in range(8):
            
            c = "white"
            if darkSquare:

                c = "BlanchedAlmond"

            darkSquare = not darkSquare
                    
            canvas.create_polygon(  row*GRIDSPACING + BOARD_OFFSET, column*GRIDSPACING + BOARD_OFFSET, 
                                    (row+1)*GRIDSPACING + BOARD_OFFSET, column*GRIDSPACING + BOARD_OFFSET,
                                    (row+1)*GRIDSPACING + BOARD_OFFSET, (column+1)*GRIDSPACING + BOARD_OFFSET, 
                                    row*GRIDSPACING + BOARD_OFFSET, (column+1)*GRIDSPACING + BOARD_OFFSET,
                                    fill=c, outline="black")
    return canvas

def placePieces(canvas: Canvas, pieces) -> Canvas:
    
    ORDER = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]

    for i in range(8):
        #back row
        canvas.create_image(i*GRIDSPACING + PIECE_OFFSET, 7*GRIDSPACING + PIECE_OFFSET, image=pieces[WHITE][ORDER[i]], anchor="nw")
        canvas.create_image(i*GRIDSPACING + PIECE_OFFSET, 0*GRIDSPACING + PIECE_OFFSET, image=pieces[BLACK][ORDER[i]], anchor="nw")
        #pawns
        canvas.create_image(i*GRIDSPACING + PIECE_OFFSET, 6*GRIDSPACING + PIECE_OFFSET, image=pieces[WHITE][PAWN], anchor="nw")
        canvas.create_image(i*GRIDSPACING + PIECE_OFFSET, 1*GRIDSPACING + PIECE_OFFSET, image=pieces[BLACK][PAWN], anchor="nw")

    return canvas