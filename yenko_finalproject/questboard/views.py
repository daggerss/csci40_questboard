from django.shortcuts import render

from django.views.generic import ListView


from .models import QuestCard


class QuestListView(ListView):
    template_name = 'home.html'
    queryset = QuestCard.objects.all().order_by('-stars')