from tkinter import Tk, Canvas, Frame, BOTH
import setupBoard
from loadImages import loadBoard, loadPieces

START_POS = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Gonna have to have some sort of system where:

#   if(mouseOverPiece):
#       legalMoves = calculateLegalMoves(piece, FEN)
#       applyHighlight(legalMoves)
# 
#   def calculateLegalMoves(piece, FEN):
# 
#       pieceRules = {rook: rules,
#                     knight: rules,
#                     etc: etc}
#
#       blockedMoves = calcBlockedMoves()

class Board(Frame):

    def __init__(self):
        
        super().__init__()
        self.board = loadBoard()
        self.pieceImages = loadPieces()
        self.initUI()

    def initUI(self):

        self.master.title("Chess")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self, bg="black", height=645, width=645)
        canvas.pack()

        canvas.create_image(5, 5, image=self.board, anchor="nw")

        canvas = setupBoard.read(START_POS, canvas, self.pieceImages)

def main():

    root = Tk()
    root.geometry("660x655+400+150")
    board = Board()
    root.mainloop()


if __name__ == '__main__':
    main()