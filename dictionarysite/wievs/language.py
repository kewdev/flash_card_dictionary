from django.views.generic import ListView, CreateView, UpdateView, DetailView
from dictionarysite.models import Language
from dictionarysite.forms import LanguageForm


class ListLanguage(ListView):
    model = Language
    template_name = 'dictionarysite/language/list_language.html'
    context_object_name = 'language_list'


class DetailLanguage(DetailView):
    model = Language
    template_name = 'dictionarysite/language/detail_language.html'
    context_object_name = 'language'


class CreateLanguage(CreateView):
    model = Language
    template_name = 'dictionarysite/language/create_language.html'
    form_class = LanguageForm


class UpdateLanguage(UpdateView):
    model = Language
    template_name = 'dictionarysite/language/update_language.html'
    form_class = LanguageForm


class DeleteLanguage(UpdateView):
    model = Language
    context_object_name = 'language'
    template_name = 'dictionarysite/language/delete_language.html'
    form_class = LanguageForm
