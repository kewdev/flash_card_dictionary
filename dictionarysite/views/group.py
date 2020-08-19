from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from dictionarysite import urlconsts
from dictionarysite.models import Group, Word
from dictionarysite.forms import GroupForm


class ListGroup(ListView):
    template_name = 'dictionarysite/group/list_group.html'
    context_object_name = 'group_list'
    # paginate_by = 50

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)


class DetailGroup(DetailView):
    model = Group
    template_name = 'dictionarysite/group/detail_group.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word_list'] = Word.objects.filter(groups__slug=self.get_object().slug)
        return context


class CreateGroup(CreateView):
    model = Group
    template_name = 'dictionarysite/group/create_group.html'
    form_class = GroupForm

    def form_valid(self, form):
        word = form.save(commit=False)
        word.user = self.request.user
        word.save()
        form.save()
        return super().form_valid(form)


class UpdateGroup(UpdateView):
    model = Group
    template_name = 'dictionarysite/group/update_group.html'
    form_class = GroupForm


class DeleteGroup(DeleteView):
    model = Group
    context_object_name = 'group'
    template_name = 'dictionarysite/group/delete_group.html'
    form_class = GroupForm

    def get_success_url(self):
        return reverse(urlconsts.LIST_GROUP_URL)
