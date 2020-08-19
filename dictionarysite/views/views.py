from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from django.views.generic import TemplateView
from dictionarysite import urlconsts


def index(request):
    if isinstance(request.user, AnonymousUser):
        return redirect(urlconsts.INSTRUCTIONS_PAGE_URL)
    else:
        return redirect(urlconsts.LIST_WORD_URL)


class Instructions(TemplateView):
    template_name = 'dictionarysite/index.html'
