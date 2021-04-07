from django.shortcuts import render

from django.views.generic import ListView


from .models import Questboard


class QuestListView(ListView):
    template_name = 'home.html'
    queryset = Questboard.objects.all().order_by('-stars')