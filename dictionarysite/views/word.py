from django.urls import reverse
from django.utils.encoding import uri_to_iri
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from dictionarysite import urlconsts
from dictionarysite.models import Word
from dictionarysite.forms import WordForm


class ListWord(ListView):
    model = Word
    template_name = 'dictionarysite/word/list_word.html'
    # paginate_by = 50

    def get_queryset(self):
        search_word = self.request.GET.get("word")
        if not search_word:
            return Word.objects.filter(is_not_display=False, user=self.request.user)
        return Word.objects.filter(word__icontains=uri_to_iri(search_word), user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_word"] = self.request.GET.get("word")
        return context


class DetailWord(DetailView):
    model = Word
    context_object_name = 'word'
    template_name = 'dictionarysite/word/detail_word.html'


class CreateWord(CreateView):
    model = Word
    template_name = 'dictionarysite/word/create_word.html'
    form_class = WordForm

    def form_valid(self, form):
        word = form.save(commit=False)
        word.rank = 5
        word.user = self.request.user
        word.save()
        form.save()
        return super().form_valid(form)


class UpdateWord(UpdateView):
    model = Word
    form_class = WordForm
    template_name = 'dictionarysite/word/update_word.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_action_url"] = urlconsts.INDEX_PAGE_URL
        context["create_action_url"] = urlconsts.CREATE_WORD_URL
        context["word"] = Word.objects.get(slug=self.kwargs.get('slug'))
        return context

    def get_success_url(self):
        return reverse(urlconsts.UPDATE_WORD_URL, kwargs={'slug': Word.objects.get(word=self.request.POST["word"]).slug})


class DeleteWord(UpdateView):
    model = Word
    context_object_name = 'word'
    template_name = 'dictionarysite/word/delete_word.html'
    form_class = WordForm
