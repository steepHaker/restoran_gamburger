# Generated by Django 4.2.2 on 2023-07-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_application', '0004_alter_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='namePage1',
            field=models.CharField(default='', max_length=100, verbose_name='Название страницы'),
        ),
    ]
