# Generated by Django 3.0.7 on 2020-06-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionarysite', '0011_auto_20200605_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='is_not_display',
            field=models.BooleanField(default=False, verbose_name='Не отображать слово на главной странице'),
        ),
    ]
