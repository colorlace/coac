from django.db import models

# Create your models here.

class PieceMove(models.Model):
    piece_move = models.CharField(max_length=10)

class BoardState(models.Model):
    board_state = models.CharField(max_length=70)

    def __str__(self):
        return self.board_state
