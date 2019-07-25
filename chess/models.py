from django.db import models
import re
####HELPER FUNCTIONS######

def emptify(row_string):
    """
     IN: a string from 1 row in a FEN string w/empties like: 'pp5p'
     OUT: a list of chars.  adding 0s at empties like: 'pp00000p'
    """
    row_list = list(row_string)
    emptified_row = []
    for sqr in row_list:
        if '1' <= sqr <= '8':
            emptified_row.extend(list('0'*eval(sqr)))
        else: #we have a piece in this position
            emptified_row.append(sqr)
    return emptified_row

def convertBoardTo2d(fen_string):
    """
    IN: a string of the current board state in fen mode
    OUT: a list of 8 lists of 8 chars
    """
    fen_list = fen_string.split("/")
    fen_2d = []
    for row in fen_list:
        if re.search(r'[1-8]',row) == None: #no empties
            fen_2d.append(list(row))
        else: #there are empty squares
            fen_2d.append(emptify(row))
    return fen_2d

def parseMove(move):
    """
    IN: a move from an http request like b1-a3
    OUT: converted to list indices 7,1 5,0
    """
    rankfile = list(move.replace('-',''))
    print (rankfile)
    def rankToRow(rnk):
        return abs(eval(rnk)-8)
    def fileToCol(fle):
        return ord(fle)-97
    return [ rankToRow(rankfile[1]), fileToCol(rankfile[0]), rankToRow(rankfile[3]), fileToCol(rankfile[2]) ]

####MODELS###############
class BoardState(models.Model):
    board_state = models.CharField(max_length=70)
    active_color = models.CharField(max_length=1)

    @classmethod
    def newGame(cls):
        n = cls.objects.count()
        #new game? just delete all rows EXCEPT id=0 (initial state)
        for row_id in range(1,n):
            cls.objects.filter(id=row_id).delete()

    @classmethod
    def newMove(cls, move):
        #takes a string like a2-a4 and updates the BoardState model
        if move == "newgame":
            cls.newGame()
        elif move == "castle":
            cls.castle()
        else:
            cls.makeMove(move)

    @classmethod
    def makeMove(cls, move):
        fen_string = cls.objects.order_by('id').last().board_state
        positions_2d = convertBoardTo2d(fen_string)
        print(positions_2d)
        print(parseMove(move))

    def __str__(self):
        return self.board_state
