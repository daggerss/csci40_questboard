"""yenko_finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from questboard.views import (BoardListView, BoardCreateView,
                              questboard_view, BoardUpdateView,
                              QuestCreateView, QuestUpdateView,
                              signup_view)

urlpatterns = [
    path('', BoardListView.as_view(), name='index'),
    path('questboard/', BoardListView.as_view(), name='board-list'),
    path('questboard/new/', BoardCreateView.as_view(), name='board-create'),
    path('questboard/<int:id>/', questboard_view, name='board-detail'),
    path(
        'questboard/<int:id>/update',
        BoardUpdateView.as_view(),
        name='board-update'
    ),
    path(
        'questboard/<int:id>/new_quest',
        QuestCreateView.as_view(),
        name='quest-create'
    ),
    path(
        'quest/<int:id>/update',
        QuestUpdateView.as_view(),
        name='quest-update'
    ),
    path('quest/<int:id>/signup', signup_view, name='quest-signup'),
    path('admin/', admin.site.urls),
]
