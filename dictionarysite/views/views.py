from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect
from django.utils.encoding import iri_to_uri, uri_to_iri
from django.views.generic import TemplateView
from dictionarysite.models import Word


class Instructions(TemplateView):
    template_name = 'dictionarysite/index.html'
    context_object_name = 'word_list'

    def get_queryset(self):
        search_word = self.request.GET.get("word")
        if not search_word:
            return Word.objects.filter(is_not_display=False, user=self.request.user)
        return Word.objects.filter(word__icontains=uri_to_iri(search_word), user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_word"] = self.request.GET.get("word")
        return context


def index(request):
    if isinstance(request.user, AnonymousUser):
        return redirect("instructions_page_url")
    else:
        return redirect("list_word_url")
