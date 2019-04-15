from django import forms

from .models import Polls

class PollsForm(forms.ModelForm):
    class Meta:
        model = Polls
        fields = [
        'polls_id',
        'title',
        'questions',
        ]
