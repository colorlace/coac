from django.conf.urls import url

from . import views

app_name = 'chess'
urlpatterns = [
    #e.g. /chess/board
    url(r'^board/$', views.board, name='board'),
]


