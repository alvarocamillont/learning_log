from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


def logout_view(request):
    """Faz logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
