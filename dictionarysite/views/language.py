from django.views.generic import ListView, CreateView, UpdateView, DetailView
from dictionarysite.models import Language
from dictionarysite.forms import LanguageForm


class ListLanguage(ListView):
    template_name = 'dictionarysite/language/list_language.html'
    context_object_name = 'language_list'
    # paginate_by = 50

    def get_queryset(self):
        return Language.objects.filter(user=self.request.user)


class DetailLanguage(DetailView):
    model = Language
    template_name = 'dictionarysite/language/detail_language.html'
    context_object_name = 'language'


class CreateLanguage(CreateView):
    model = Language
    template_name = 'dictionarysite/language/create_language.html'
    form_class = LanguageForm

    def form_valid(self, form):
        word = form.save(commit=False)
        word.user = self.request.user
        word.save()
        form.save()
        return super().form_valid(form)


class UpdateLanguage(UpdateView):
    model = Language
    template_name = 'dictionarysite/language/update_language.html'
    form_class = LanguageForm


class DeleteLanguage(UpdateView):
    model = Language
    context_object_name = 'language'
    template_name = 'dictionarysite/language/delete_language.html'
    form_class = LanguageForm
