# Generated by Django 3.0.7 on 2020-06-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionarysite', '0017_auto_20200612_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.TextField(db_index=True, verbose_name='Слово'),
        ),
    ]
