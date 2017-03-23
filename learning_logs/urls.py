"""Define padrões de url para learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Pagina Inicial
    url(r'^$', views.index, name='index'),
]
