from django.shortcuts import redirect
from django.urls import reverse
from django.utils.encoding import uri_to_iri
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from dictionarysite import urlconsts
from dictionarysite.models import Word, Language, Group
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

    def get(self, request, *args, **kwargs):
        count_of_languages = Language.objects.filter(user=self.request.user).count()
        if count_of_languages == 0:
            return redirect(urlconsts.CREATE_LANGUAGE_URL)
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        language_slug = self.request.GET.get('language_slug', None)
        group_slug = self.request.GET.get('group_slug', None)
        initial_values = super().get_initial()
        if language_slug is not None:
            initial_values['language'] = Language.objects.get(slug=language_slug)
            return initial_values
        if group_slug is not None:
            initial_values['groups'] = Group.objects.get(slug=group_slug)
            return initial_values
        return initial_values

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = self.request.user

        return form_kwargs


class UpdateWord(UpdateView):
    model = Word
    template_name = 'dictionarysite/word/update_word.html'
    form_class = WordForm

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def get_success_url(self):
        return reverse(urlconsts.UPDATE_WORD_URL,
                       kwargs={'slug': Word.objects.get(word=self.request.POST["word"]).slug})


class DeleteWord(DeleteView):
    model = Word
    context_object_name = 'word'
    template_name = 'dictionarysite/word/delete_word.html'
    form_class = WordForm

    def get_success_url(self):
        return reverse(urlconsts.LIST_WORD_URL)
