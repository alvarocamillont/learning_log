from django import forms

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    """Classe para o formulário de cadastro de assuntos"""
    class Meta:
        model = Topic
        fields = ['text']
        label = {'text': ''}


class EntryForm(forms.ModelForm):
    """Classe para detalhes do tópico"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
