'''Models are python objects that directly correspond to
TABLES in the database
'''

from django.db import models
from .fen_string_helpers import update_board_position, update_active_color, update_castling_availability, update_en_passant_target, update_halfmove_clock, update_fullmove_counter
import re

####MODELS###############
class BoardState(models.Model):
    fen = models.CharField(max_length=100, null=True)
    board_position = models.CharField(max_length=71, null=True)
    active_color = models.CharField(max_length=1)
    castle_info = models.CharField(max_length=9, null=True) #shorten
    en_passant_target = models.CharField(max_length=4, null=True)
    halfmove_clock = models.IntegerField(default=0)
    fullmove_counter = models.IntegerField(default=1)

    @classmethod
    def newGame(cls):
        n = cls.objects.count()
        cls.objects.all().delete()

        starting_boardstate = BoardState()
        starting_boardstate.board_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        starting_boardstate.active_color = "w"
        starting_boardstate.castle_info = "KQkq"
        starting_boardstate.en_passant_target = '-'
        starting_boardstate.halfmove_clock = 0
        starting_boardstate.fullmove_counter = 1
        starting_boardstate.fen = ' '.join([starting_boardstate.board_position,
                                            starting_boardstate.active_color,
                                            starting_boardstate.castle_info,
                                            starting_boardstate.en_passant_target,
                                            str(starting_boardstate.halfmove_clock),
                                            str(starting_boardstate.fullmove_counter)])
        starting_boardstate.save()

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
        """
        This function takes in the move made, and updates the last available
        board state fen_string to reflect the new board
        """
        board_state = cls.objects.order_by('id').last()

        new_board_position = update_board_position(board_state.board_position, move)
        new_active_color = update_active_color(board_state.active_color)
        new_castle_info = update_castling_availability(board_state.castle_info)
        new_en_passant_target = update_en_passant_target(board_state.board_position, new_board_position)
        new_halfmove_clock = update_halfmove_clock(board_state.halfmove_clock)
        new_fullmove_counter = update_fullmove_counter(board_state.fullmove_counter, new_active_color)

        new_fen = ' '.join([new_board_position, new_active_color, new_castle_info, new_en_passant_target, str(new_halfmove_clock), str(new_fullmove_counter)])

        #create new board state and store in database
        BoardState.objects.create(fen=new_fen,
                board_position=new_board_position,
                active_color=new_active_color,
                castle_info=new_castle_info,
                en_passant_target=new_en_passant_target,
                halfmove_clock=new_halfmove_clock,
                fullmove_counter=new_fullmove_counter)

    def __str__(self):
        return self.board_position
