from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (CreateView, ListView,
                                  UpdateView)


from .models import QuestBoard, QuestCard

from .forms import QuestboardForm, QuestGeneralForm


class BoardCreateView(CreateView):
    template_name = 'questboard/board_create.html'
    form_class = QuestboardForm
    queryset = QuestBoard.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class BoardListView(ListView):
    template_name = 'questboard/board_list.html'
    queryset = QuestBoard.objects.all().order_by('subject_name')


def questboard_view(request, id):
    board = QuestBoard.objects.get(id=id)
    quest_list = board.quests.all().order_by('-stars')

    return render(
        request,
        "questboard/board_detail.html",
        {
            'board': board,
            'quest_list': quest_list
        }
    )


class BoardUpdateView(UpdateView):
    template_name = 'questboard/board_update.html'
    form_class = QuestboardForm
    queryset = QuestBoard.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuestBoard, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class QuestCreateView(CreateView):
    template_name = 'quest/quest_create.html'
    form_class = QuestGeneralForm
    queryset = QuestCard.objects.all()

    def get_initial(self):
        id_ = self.kwargs.get("id")
        board = get_object_or_404(QuestBoard, id=id_)
        return {'subject': board}

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        id_ = self.kwargs.get("id")
        return reverse('board-detail', kwargs={'id':id_})


class QuestUpdateView(UpdateView):
    template_name = 'quest/quest_update.html'
    form_class = QuestGeneralForm
    queryset = QuestCard.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuestCard, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        id_ = self.object.subject_id
        return reverse('board-detail', kwargs={'id':id_})