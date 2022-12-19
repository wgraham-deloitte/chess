from tkinter import Tk, Canvas, Frame, BOTH
from PIL import Image, ImageTk
import os
from setupBoard import makeBoard, placePieces 

class Board(Frame):

    def __init__(self):
        
        super().__init__()
        self.pieces = self.loadPieces()
        self.initUI()

    def loadPieces(self):
        
        paths = []
        dir = "./ChessPieces"
        for path in os.listdir(dir):
            paths.append(dir + "/" + path)

        paths.sort()

        black_pieces = []
        white_pieces = []

        for piece in paths:
            img = Image.open(piece)
            img = ImageTk.PhotoImage(img.resize((64, 64)))
            if "b_" in piece:
                black_pieces.append(img)
                continue
            white_pieces.append(img)

        return [white_pieces, black_pieces]

    def initUI(self):

        self.master.title("Chess")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self, bg="black", height=645, width=645)
        canvas.pack()

        canvas = makeBoard(canvas)
        canvas = placePieces(canvas, self.pieces)

def main():

    root = Tk()
    root.geometry("660x655+400+150")
    board = Board()
    root.mainloop()


if __name__ == '__main__':
    main()