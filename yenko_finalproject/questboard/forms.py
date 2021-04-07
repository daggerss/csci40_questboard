from django import forms

from .models import QuestBoard


class QuestboardForm(forms.ModelForm):

    class Meta:
        model = QuestBoard
        fields = ['subject_name', 'description', 'required_stars']