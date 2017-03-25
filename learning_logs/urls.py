"""Define padrões de url para learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Pagina Inicial
    url(r'^$', views.index, name='index'),

    # Mostra todos os assuntos
    #url(r'^topics/$', views.topics, name='topics'),
]
