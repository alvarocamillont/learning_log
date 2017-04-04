"""Modelos da APP Learning Logs"""
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text


class Entry(models.Model):
    """Detalhes sobre o assunto"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        retorno = self.text[:50]
        if len(self.text) > 50:
            retorno += "..."

        return retorno
