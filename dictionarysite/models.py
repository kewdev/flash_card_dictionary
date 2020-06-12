from time import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from dictionarysite import urlconsts

from pytils.translit import slugify


def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))


class Language(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь",
                             on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    name = models.CharField("Язык", max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(urlconsts.DETAIL_LANGUAGE_URL, kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Group(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь",
                             on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    name = models.CharField("Название группы", max_length=200)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(urlconsts.DETAIL_GROUP_URL, kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Word(models.Model):
    # TODO: прописать help_text, default
    user = models.ForeignKey(User, verbose_name="Пользователь",
                             on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    word = models.TextField("Слово", db_index=True)
    translation = models.TextField("Перевод", null=True, blank=True)
    language = models.ForeignKey(Language, verbose_name="Язык", on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField(Group, verbose_name="Группы", null=True, blank=True)
    # TODO использовать  Field.choices
    priority = models.PositiveSmallIntegerField("Приоритет изучения", null=True, blank=True, default=10)
    note = models.TextField("Заметки", null=True, blank=True)
    rank = models.PositiveSmallIntegerField("Популярность слова", null=True, blank=True, default=0)
    creation_date_time = models.DateTimeField("Дата создания", auto_now_add=True, db_index=True)
    is_not_display = models.BooleanField("Не отображать слово на главной странице", default=False)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.word)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(urlconsts.DETAIL_WORD_URL, kwargs={'slug': self.slug})   # url reversing

    def __str__(self):
        return self.word
