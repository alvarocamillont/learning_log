from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    """Classe para o formulário de cadastro de assuntos"""
    class Meta:
        model = Topic
        fields = ['text']
        label = {'text': ''}
