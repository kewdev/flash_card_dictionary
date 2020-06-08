from django.forms import ModelForm
from dictionarysite.models import Word, Group, Language


class WordForm(ModelForm):

    class Meta:
        model = Word
        fields = ['word', 'translation', 'note', 'priority', 'is_not_display']


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name']


class LanguageForm(ModelForm):

    class Meta:
        model = Language
        fields = ['name']
