from tkinter import Tk, Canvas, Frame, BOTH
from PIL import Image, ImageTk
import os
from setupBoard import loadPieces, makeBoard, placePieces 

class Board(Frame):

    def __init__(self):
        
        super().__init__()
        self.pieces = loadPieces()
        self.initUI()

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