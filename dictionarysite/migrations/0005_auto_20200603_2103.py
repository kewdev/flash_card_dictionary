# Generated by Django 3.0.7 on 2020-06-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionarysite', '0004_auto_20200603_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordtranslation',
            name='word',
        ),
        migrations.AddField(
            model_name='phrase',
            name='translation',
            field=models.ManyToManyField(related_name='_phrase_translation_+', to='dictionarysite.Phrase', verbose_name='Перевод'),
        ),
        migrations.AddField(
            model_name='word',
            name='translation',
            field=models.ManyToManyField(related_name='_word_translation_+', to='dictionarysite.Word', verbose_name='Перевод'),
        ),
        migrations.DeleteModel(
            name='PhraseTranslation',
        ),
        migrations.DeleteModel(
            name='WordTranslation',
        ),
    ]
