from django.http import HttpResponse
from django.template import loader

from .models import BoardState

import re
from termcolor import colored
# Create your views here.
def board(request):
    url_path  = request.path #get move 
    move = re.findall(r'chess/board/(.*)',url_path)[0]
    print(colored(move,"red"))
    BoardState.newMove(move=move)
    
    current_board_state = BoardState.objects.order_by('id').last()

    template = loader.get_template('chess/test.html')
    context = {
        'current_board_state': current_board_state
    }
    return HttpResponse(template.render(context,request))
