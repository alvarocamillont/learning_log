from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


def index(request):
    """Página inicial da aplição"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Mostra os detalhes de um tópico"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Cadastro de um novo tópico"""
    if request.method != 'POST':
        # Nenhum dado submetido
        # Cria formulário em branco
        form = TopicForm()
    else:
        # Dados do POST submetido: processa os Dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada ao tópico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # Nenhum dado foi submetido
        form = EntryForm()
    else:
        # Dados de post submetidos; processa os Dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}

    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Requisição Inicial;preenche o formulario com o atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'topic': topic, 'form': form, 'entry': entry}

    return render(request, 'learning_logs/edit_entry.html', context)
