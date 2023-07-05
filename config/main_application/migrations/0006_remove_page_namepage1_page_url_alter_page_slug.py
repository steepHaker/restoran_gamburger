# Generated by Django 4.2.2 on 2023-07-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_application', '0005_page_namepage1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='namePage1',
        ),
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='URL страницы'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', verbose_name='Отображение в браузере'),
        ),
    ]
