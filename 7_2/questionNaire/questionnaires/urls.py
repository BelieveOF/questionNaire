"""questionNaire URL Configuration

The `urlpatterns` questionnaires routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/', views.createQuestionnaire),
    url(r'^AllLists/', views.AllLists),
    url(r'^MyLists/', views.MyLists),
    url(r'^my_questions_options/(?P<pk>[0-9]+)/$', views.my_questions_options),
    url(r'^questions_options/(?P<pk>[0-9]+)/$', views.questions_options),
    url(r'^naire_delete/(?P<pk>[0-9]+)/$', views.naire_delete),
    url(r'^naire_update/(?P<pk>[0-9]+)/$', views.naire_update),
    # url(r'^create_question/',views.create_question),
]
