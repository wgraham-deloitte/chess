from tkinter import Tk, Canvas, Frame, BOTH
import setupBoard
from setupBoard import X_OFFSET, Y_OFFSET, X_GRID, Y_GRID
from loadImages import loadBoard, loadPieces
from calculateLegalMoves import getLegalMoves, highlightMoves

START_POS = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

CANVAS_WIDTH = 750
CANVAS_HEIGHT = 750

class Board(Frame):

    def __init__(self):
        
        super().__init__()
        self.FEN = START_POS
        self.initUI()

        self.mouseX = None
        self.mouseY = None
        self.geo = []

    def initUI(self):

        self.boardImage = loadBoard(CANVAS_HEIGHT, CANVAS_WIDTH)
        self.pieceImages = loadPieces()

        self.master.title("Chess")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, bg="white", height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.canvas.pack()                   

        self.board = self.canvas.create_image(0, 0, image=self.boardImage, anchor="nw")
        self.canvas = setupBoard.read(self.FEN, self.canvas, self.pieceImages)

    def showLegalMoves(self, event):

        x, y = self.getMousePos(event)
        
        x = int((x - X_OFFSET) // X_GRID)
        y = int((y - Y_OFFSET) // Y_GRID)

        if self.mouseX != x or self.mouseY != y:
            for i in self.geo:
                self.canvas.delete(i)
            self.mouseX = x
            self.mouseY = y
        
        piece = self.getPiece(x, y)

        moves = getLegalMoves(self, piece, x, y)
        highlights = highlightMoves(moves, x, y)

        for i in highlights:
            self.geo.append(self.canvas.create_oval(i[0], i[1], i[2], i[3], fill="lime"))

    def getPiece(self, x: int, y: int) -> str:

        if(x < 0 or x >= 8 or y < 0 or y >= 8):
            return "-1"

        oldStr = self.FEN.split()[0].split("/")[y]
        newStr = ""
        for i in range(len(oldStr)):
            
            if not oldStr[i].isnumeric():
                newStr += oldStr[i]
                continue
            
            for j in range(int(oldStr[i])):
                newStr += "1"       

        return newStr[x]

    def getClickPos(self, event):
        print(event.x, event.y)

    def getMousePos(self, event):

        x = event.x
        y = event.y
        return (x, y)


def main():

    root = Tk()
    root.geometry(str(CANVAS_WIDTH + 10) + "x" + str(CANVAS_HEIGHT + 10) + "+100+100")
    board = Board()
    root.bind('<Motion>', board.showLegalMoves)
    root.bind('<Button-1>', board.getClickPos)

    root.mainloop()

if __name__ == '__main__':
    main()