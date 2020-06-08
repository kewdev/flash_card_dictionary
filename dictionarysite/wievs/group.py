from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from dictionarysite import urlconsts
from dictionarysite.models import Group
from dictionarysite.forms import GroupForm


class ListGroup(ListView):
    model = Group
    template_name = 'dictionarysite/group/list_group.html'
    context_object_name = 'group_list'


class DetailGroup(DetailView):
    model = Group
    template_name = 'dictionarysite/group/detail_group.html'
    context_object_name = 'group'


class CreateGroup(CreateView):
    model = Group
    template_name = 'dictionarysite/group/create_group.html'
    form_class = GroupForm


class UpdateGroup(UpdateView):
    model = Group
    template_name = 'dictionarysite/group/update_group.html'
    form_class = GroupForm


class DeleteGroup(UpdateView):
    model = Group
    context_object_name = 'group'
    template_name = 'dictionarysite/group/delete_group.html'
    form_class = GroupForm
