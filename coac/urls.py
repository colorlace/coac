"""coac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^chess/', include('chess.urls')),
    url(r'^admin/', admin.site.urls),
]

'''
The include() function allows referencing other URLconfs. Whenever Django
encounters include(), it chops off whatever part of the URL matched up to that
point and sends the remaining string to the included URLconf for
further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls
are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or
 under “/fun_polls/”, or under “/content/polls/”, or any other path root, and
 the app will still work

You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
'''
