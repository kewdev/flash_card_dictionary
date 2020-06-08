# Generated by Django 3.0.7 on 2020-06-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionarysite', '0005_auto_20200603_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='note',
            field=models.TextField(null=True, verbose_name='Заметки'),
        ),
        migrations.AlterField(
            model_name='word',
            name='groups',
            field=models.ManyToManyField(null=True, to='dictionarysite.Group', verbose_name='Группы'),
        ),
        migrations.AlterField(
            model_name='word',
            name='knowledge_level',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Уровень знания'),
        ),
        migrations.AlterField(
            model_name='word',
            name='popularity',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Популярность слова'),
        ),
        migrations.AlterField(
            model_name='word',
            name='translation',
            field=models.ManyToManyField(null=True, related_name='_word_translation_+', to='dictionarysite.Word', verbose_name='Перевод'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.TextField(db_index=True, verbose_name='Слово'),
        ),
        migrations.DeleteModel(
            name='Phrase',
        ),
    ]
