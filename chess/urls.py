from django.urls import path, re_path

from . import views

from django.conf.urls import url

app_name = 'chess'
urlpatterns = [
    #e.g. /chess/board
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    #FIXME?
    re_path(r'board/[a-z][1-9]-[a-z][1-9]', views.board, name='board_change'),
    path('board/newgame', views.board),
]
