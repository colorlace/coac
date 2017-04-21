from django.http import HttpResponse
from django.template import loader

from .models import BoardState

# Create your views here.
def board(request):
    current_board_state = BoardState.objects.order_by('id').first()

    template = loader.get_template('chess/test.html')
    context = {
        'current_board_state': current_board_state
    }
    return HttpResponse(template.render(context,request))
