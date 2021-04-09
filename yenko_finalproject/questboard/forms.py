from django import forms

from .models import QuestBoard, QuestCard


class QuestboardForm(forms.ModelForm):

    class Meta:
        model = QuestBoard
        fields = ['subject_name', 'description', 'required_stars']


class QuestGeneralForm(forms.ModelForm):

    class Meta:
        model = QuestCard
        fields = ['subject', 'quest_name', 'description',
                  'stars', 'is_for_everyone']


class FirstSignUpForm(forms.ModelForm):

    class Meta:
        model = QuestCard
        fields = ['student1']
    
    def __init__(self, *args, **kwargs):
        super(FirstSignUpForm, self).__init__(*args, **kwargs)
        self.fields['student1'].label = ''


class SecondSignUpForm(forms.ModelForm):

    class Meta:
        model = QuestCard
        fields = ['student2']

    def __init__(self, *args, **kwargs):
        super(SecondSignUpForm, self).__init__(*args, **kwargs)
        self.fields['student2'].label = ''


class ThirdSignUpForm(forms.ModelForm):

    class Meta:
        model = QuestCard
        fields = ['student3']

    def __init__(self, *args, **kwargs):
        super(ThirdSignUpForm, self).__init__(*args, **kwargs)
        self.fields['student3'].label = ''