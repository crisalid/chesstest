#!/usr/bin/python
# Importing basic libraries to process user input
import sys, getopt

def coordToPos(x, y):
    ''' Converting numerical coordinates to board cells '''    
    r = 'abcdefgh'[x - 1] + str(y)
    return r

def chessPieceMoves(piece, pos, printChessBoard = False):
    ''' Calculating moves for each piece. Also drawing a nice map of moves. '''
    x = "abcdef".find(pos[:1])+1
    y = int(pos[1:])
    if not (x >= 1 and x <= 8 and y >= 1 and y <= 8):
       print("Bad coordinates, try again ",coord[1:])
       sys.exit(2);
    yi = 8 
    positions = []
    board = ''
    while yi >= 1:        
        xi = 1
        while xi <= 8:
            here = False
            dx = abs(xi - x)
            dy = abs(yi - y)
            if piece == 'rook':
                here = (yi == y or xi == x)
            if piece == 'bishop':
                here = (dx == dy)
            if piece == 'queen':
                here = (yi == y or xi == x or dx == dy)
            if piece == 'knight':
                here = (dx == 2 and dy == 1 or dx == 1 and dy == 2)
            if dx == 0 and dy == 0:
                here = False
            if here:
                board = board + 'XX'
                positions.append(coordToPos(xi, yi))
            else:
                board = board + '  '
            xi = xi + 1
        board += "\n"        
        yi = yi - 1

    positions.sort()
    if printChessBoard:
        result = board
    else:
        result = ", ".join(positions)
    return result

def main(argv):
    ''' Processing user input, handling exceptions, outputting result '''
    piece = ''
    coord = ''
    printChessBoard = False
    try:
        opts, args = getopt.getopt(argv,"hp:c:bt", ["help", "piece=", "coord=", "board"])
    except getopt.GetoptError:
        print("chess.py -p <piece> -c <coord> [-b]")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('chess.py -p <piece> -c <coord>')
            sys.exit()
        elif opt in ("-p", "--piece"):
            piece = arg
        elif opt in ("-c", "--coord"):
            coord = arg
        elif opt in ("-b", "--board"):
            printChessBoard = True
         
    pieces = ['knight', 'rook', 'queen', 'bishop']
    if not piece in pieces:
        print("Bad chess piece, known pieces are:", ", ".join(pieces))
        sys.exit(2)

    if len(coord) != 2:
        print("Bad coordinates! coordinate sample: 'd2'");
        sys.exit(2);
	   
    result = chessPieceMoves(piece, coord, printChessBoard)
    print(result)
if __name__ == "__main__":
    main(sys.argv[1:])
