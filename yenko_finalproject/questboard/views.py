from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView


from .models import QuestBoard, QuestCard


class BoardListView(ListView):
    template_name = 'board_list.html'
    queryset = QuestBoard.objects.all().order_by('subject_name')


def questboard_view(request, id):
    board = QuestBoard.objects.get(id=id)
    quest_list = board.quests.all().order_by('-stars')

    return render(
        request,
        "board_detail.html",
        {
            'board': board,
            'quest_list': quest_list
        }
    )