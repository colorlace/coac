from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import BoardState

import re
from termcolor import colored, cprint

def index(request):
    return HttpResponse("Welcome to the Castle on a Cloud")

# Create your views here.
def board(request):
    url_path  = request.path #get move
    cprint(f'URL PATH: {colored(url_path, "red")}', "cyan")
    #TODO: avoid using the hardcoded request path string here.
    move = re.findall(r'chess/board/(.*)',url_path)[0]
    cprint(f'MOVE (fen code): {colored(move, "red")}', "cyan")

    #try:
    BoardState.newMove(move=move)
    #except:
    #    raise Http404("Invalid move")

    current_board_state = BoardState.objects.order_by('id').last()

    template = loader.get_template('chess/board_template.html')
    context = {
        'current_board_state': current_board_state
    }
    return HttpResponse(template.render(context,request))

    #return render(request, 'chess/test.html', {'current_board_state': current_board_state})
