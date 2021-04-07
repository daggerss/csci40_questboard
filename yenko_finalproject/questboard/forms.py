from django import forms

from .models import QuestBoard, QuestCard


class QuestboardForm(forms.ModelForm):

    class Meta:
        model = QuestBoard
        fields = ['subject_name', 'description', 'required_stars']


class NewQuestForm(forms.ModelForm):

    class Meta:
        model = QuestCard
        fields = ['subject', 'quest_name', 'description',
                  'stars', 'is_for_everyone']