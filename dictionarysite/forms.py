from django import forms
from dictionarysite.models import Word, Group, Language


class WordForm(forms.ModelForm):
    #groups = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all())

    class Meta:
        model = Word
        fields = ['word', 'translation', 'note', 'priority', 'is_not_display']


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ['name']
