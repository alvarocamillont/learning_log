from django.shortcuts import render


def index(request):
    """Página inicial da aplição"""
    return render(request, 'learning_logs/index.html')

