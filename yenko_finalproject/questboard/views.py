from django.shortcuts import render

from django.views.generic import ListView


from .models import QuestBoard, QuestCard


class BoardListView(ListView):
    template_name = 'board_list.html'
    queryset = QuestBoard.objects.all().order_by('subject_name')


class QuestListView(ListView):
    template_name = 'quest_list.html'
    queryset = QuestCard.objects.all().order_by('-stars')