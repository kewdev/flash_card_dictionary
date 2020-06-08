from django.urls import path

from dictionarysite import views
from dictionarysite.wievs.word import CreateWord, UpdateWord, DeleteWord, ListWord, DetailWord
from dictionarysite.wievs.group import CreateGroup, UpdateGroup, DeleteGroup, ListGroup, DetailGroup
from dictionarysite.wievs.language import CreateLanguage, UpdateLanguage, DeleteLanguage, ListLanguage, DetailLanguage
from dictionarysite import urlconsts


urlpatterns = [
    path('', views.Index.as_view(), name=urlconsts.INDEX_PAGE_URL),
    path('index/<str:word>', views.Index.as_view(), name=urlconsts.INDEX_PAGE_URL),

    path('word/', ListWord.as_view(), name=urlconsts.LIST_WORD_URL),
    path('word/list/<str:language>', ListWord.as_view(), name=urlconsts.LIST_WORD_ON_LANGUAGE_URL),
    path('word/detail/<slug:slug>/', DetailWord.as_view(), name=urlconsts.DETAIL_WORD_URL),
    path('word/create/', CreateWord.as_view(), name=urlconsts.CREATE_WORD_URL),
    path('word/update/<slug:slug>/', UpdateWord.as_view(), name=urlconsts.UPDATE_WORD_URL),
    path('word/delete/<slug:slug>/', DeleteWord.as_view(), name=urlconsts.DELETE_WORD_URL),

    path('group/', ListGroup.as_view(), name=urlconsts.LIST_GROUP_URL),
    path('group/detail/<slug:slug>/', DetailGroup.as_view(), name=urlconsts.DETAIL_GROUP_URL),
    path('group/create/', CreateGroup.as_view(), name=urlconsts.CREATE_GROUP_URL),
    path('group/update/<slug:slug>/', UpdateGroup.as_view(), name=urlconsts.UPDATE_GROUP_URL),
    path('group/delete/<slug:slug>/', DeleteGroup.as_view(), name=urlconsts.DELETE_GROUP_URL),

    path('language/', ListLanguage.as_view(), name=urlconsts.LIST_LANGUAGE_URL),
    path('language/detail/<slug:slug>/', DetailLanguage.as_view(), name=urlconsts.DETAIL_LANGUAGE_URL),
    path('language/create/', CreateLanguage.as_view(), name=urlconsts.CREATE_LANGUAGE_URL),
    path('language/update/<slug:slug>/', UpdateLanguage.as_view(), name=urlconsts.UPDATE_LANGUAGE_URL),
    path('language/delete/<slug:slug>/', DeleteLanguage.as_view(), name=urlconsts.DELETE_LANGUAGE_URL),
]
