from django import forms
from dictionarysite.models import Word, Group, Language


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation', 'note', 'priority', 'groups', 'language']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.language_slug = kwargs.pop('language_slug', None)
        super(WordForm, self).__init__(*args, **kwargs)

        self.fields['groups'].queryset = Group.objects.filter(user=self.user)
        self.fields['groups'].widget = forms.CheckboxSelectMultiple(choices=Group.objects.filter(user=self.user))

        self.fields['language'].queryset = Language.objects.filter(user=self.user)

    def save(self, commit=True):
        word = super(WordForm, self).save(commit=False)
        word.user = self.user
        word.save()
        word.groups.set(self.cleaned_data['groups'])
        return word


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
