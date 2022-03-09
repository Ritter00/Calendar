from django.forms import ModelForm, Textarea, DateInput
from django import forms
from .models import Note


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ('start_time','title', 'text')
        labels = {
            'start_time': 'Дата',
            'title': 'Заголовок',
            'text':'Заметка',
        }
        widgets = {
            'text': Textarea(attrs={'cols': 120, 'rows': 10}),
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }