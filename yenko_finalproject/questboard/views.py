from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, ListView


from .models import QuestBoard, QuestCard

from .forms import QuestboardForm


class BoardCreateView(CreateView):
    template_name = 'board_create.html'
    form_class = QuestboardForm
    queryset = QuestBoard.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


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