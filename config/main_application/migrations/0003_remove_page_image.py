# Generated by Django 4.2.2 on 2023-07-05 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_application', '0002_page_image_alter_upperslider_related_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='image',
        ),
    ]
