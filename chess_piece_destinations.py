"""
The Task
Accept two parameters:
1.	Type of chess piece (Queen, Rook, Knight, Bishop)
2.	Current position on a chess board (for example: a2)
Return:
 A list of all the potential board positions the given piece could advance to, with one move, from the given position, with the assumption there are no other pieces on the board.

Instructions: 
Run the following command in your terminal, python should be installed.
Example:
$ python chess_piece_destinations.py --piece Bishop --startPos a1
"""

# Basic module to get user input
import sys
# Map characters to numbers and vice versa to convert chess piece coordinates to numeric values for convinience of processing and back for user output.
strToNum = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
numToStr = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}

BoardSize = 8

def defineDestinationsAllowed(piece, PosX, PosY):
    """ Destinations for a selected piece """
    if piece == 'KNIGHT':
        destinations = KnightDestinations(PosX, PosY)
    elif piece =='ROOK':
        destinations = RookDestinations(PosX, PosY)
    elif piece == 'QUEEN':
        destinations = QueenDestinations(PosX, PosY)
    elif piece == 'BISHOP':
        destinations = BishopDestinations(PosX, PosY)
    return destinations

def moveRight(fromX,fromY):
    """ Calc all destinations for Rook/Queen going right """
    destinations = []
    for i in range(BoardSize,fromX, -1):
        if i in numToStr:
                movePos = str(fromY) + str(numToStr[i])
                destinations.append(movePos)
    return destinations

def  moveLeft(fromX,fromY):
    """ Calc all destinations for Rook/Queen going left """
    destinations = []
    for i in range(1,fromX):
        if i in numToStr:
                movePos = str(fromY) + str(numToStr[i])
                destinations.append(movePos)
    return destinations

def moveUp(fromX,fromY):
    """ Calc all destinations for Rook/Queen going up """
    destinations = []
    for i in range(fromY+1,BoardSize+1):
        if i in numToStr:
                movePos = str(i) + str(numToStr[fromX])
                destinations.append(movePos)
    return destinations

def moveDown(fromX,fromY):
    """ Calc all destinations for Rook/Queen going down """
    destinations = []
    for i in range(fromY-1, 0, -1):
        if i in numToStr:
            movePos = str(i)+str(numToStr[fromX])
            destinations.append(movePos)
    return destinations

def moveUpRight(fromX,fromY,toRight,toUp):
    """ Calc all destinations for Queen/Bishop moving diagonaly up and right """    
    destinations =[]
    if toRight < toUp:
        for i in range(fromX+1, BoardSize+1):
            if i in numToStr:
                fromX = fromX + 1
                fromY = fromY + 1
                movePos = str(fromY)+str(numToStr[fromX])
                destinations.append(movePos)
    if toUp < toRight: 
        for i in range(fromY,BoardSize):
            if i in numToStr:
                fromX = fromX + 1
                fromY = fromY + 1
                movePos = str(fromY)+str(numToStr[fromX])
                destinations.append(movePos)
    if toRight == toUp:
        for i in range(fromY,BoardSize):
            if i in numToStr:
                j = i+1
                movePos = str(j) + str(numToStr[j])
                destinations.append(movePos)
    return destinations

def moveDownRight(fromX,fromY):
    """ Calc all destinations for Queen/Bishop moving diagonaly down and right """    
    destinations =[]
    for i in range(fromY-1, 0 ,-1):
        if i in numToStr:
            fromX = fromX + 1
            fromY = fromY - 1
            if fromX<BoardSize+1 and fromY>0:
                movePos = str(fromY)+str(numToStr[fromX])
                destinations.append(movePos)
    return destinations

def moveDownLeft(fromX,fromY):
    """ Calc all destinations for Queen/Bishop moving diagonaly down and left """    
    destinations =[]
    for i in range(fromY-1, 0 ,-1):
        if i in numToStr:
            fromX = fromX - 1
            fromY = fromY - 1
            if fromX>0 and fromY >0:
                movePos = str(fromY) + str(numToStr[fromX])
                destinations.append(movePos)
    return destinations

def moveUpLeft(fromX,fromY):
    """ Calc all destinations for Queen/Bishop moving diagonaly up and left """    
    destinations =[]
    for i in range(fromY+1, BoardSize+1):
        if i in numToStr:
            fromX = fromX - 1
            fromY = fromY + 1
            if fromX>0 and fromY < BoardSize+1:
                movePos = str(fromY) + str(numToStr[fromX])
                destinations.append(movePos)
    return destinations

def RookDestinations(fromX, fromY):
    """ Calc all destinations for a Rook """    
    return moveRight(fromX,fromY) + moveLeft(fromX,fromY) + moveUp(fromX,fromY) + moveDown(fromX,fromY)

def KnightDestinations(p, q):
    """ Calc destinations of a Knight """ 
    X = [ 2, 1, -1, -2, -2, -1, 1, 2 ]; 
    Y = [ 1, 2, 2, 1, -1, -2, -2, -1 ]; 
    destinations = []
    arr = []
    for i in range(1,BoardSize+1):
        x = p + X[i-1]
        y = q + Y[i-1]
        if y>0 and y < BoardSize+1:
            if x in numToStr:
                movePos = str(y)+str(numToStr[x])
                destinations.append(movePos)
    return destinations

def QueenDestinations(fromX, fromY):
    """ Calc destinations of a Queen """ 
    toRight = BoardSize - fromX
    toUp = BoardSize - fromY
    destinations = RookDestinations(fromX, fromY) + moveUpRight(fromX, fromY, toRight, toUp) + moveDownRight(fromX, fromY) + moveDownLeft(fromX, fromY) + moveUpLeft(fromX, fromY) 
    return destinations

def BishopDestinations(fromX, fromY):
    """ Calc destinations of a Bishop """ 
    toRight = BoardSize - fromX
    toUp = BoardSize - fromY
    destinations = moveUpRight(fromX, fromY, toRight, toUp) + moveDownRight(fromX, fromY) + moveDownLeft(fromX, fromY) + moveUpLeft(fromX, fromY) 
    return destinations

def printDestinations(destinations):
    """ Gathering of the output """ 
    destinations.sort()
    allDestinations = []
    for i in sorted(destinations):
        allDestinations.append(i[1] + i[0])
    return ',' .join(allDestinations)

def chess():
    """ Process input, validate, find the destinations for the piece and output it """
    inputArgs = sys.argv
    validPieces = ['QUEEN', 'ROOK', 'KNIGHT', 'BISHOP']
    piece = inputArgs[2].upper()
    inputPosition = inputArgs[4]
    if piece.upper() not in validPieces:
        raise ValueError('Wrong piece')  
    PosY = int(inputPosition[1:len(inputPosition)])
    if PosY<1 or PosY>BoardSize:
        raise ValueError('Invalid initial piece position')  
    PosX=''
    posZero = inputPosition[0].upper()
    if posZero in strToNum:
        # Number for letter
        PosX = strToNum[posZero]
    else:
        raise ValueError('Huston, We got a problem!')  
    destinations = defineDestinationsAllowed(piece, PosX, PosY)
    print(printDestinations(destinations))

# Starting point of this software masterpiece 
if __name__ == "__main__":
    chess()