from django.utils.encoding import iri_to_uri, uri_to_iri
from django.views.generic import ListView
from dictionarysite.models import Word


class Index(ListView):
    template_name = 'dictionarysite/index.html'
    context_object_name = 'word_list'
    # paginate_by = 50

    def get_queryset(self):
        search_word = self.request.GET.get("word")
        if not search_word:
            return Word.objects.filter(is_not_display=False)
        return Word.objects.filter(word__icontains=uri_to_iri(search_word))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_word"] = self.request.GET.get("word")
        return context
