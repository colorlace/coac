from django.conf.urls import url

from . import views

app_name = 'chess'
urlpatterns = [
    #e.g. /chess/board
    url(r'^board/$', views.board, name='board'),
    #FIXME?
    url(r'^board/[a-z][1-9]-[a-z][1-9]$', views.board, name='board_change'),
    url(r'^board/newgame', views.board),
]


