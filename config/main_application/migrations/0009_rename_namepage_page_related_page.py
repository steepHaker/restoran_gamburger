# Generated by Django 4.2.2 on 2023-07-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_application', '0008_remove_page_namepage1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='namePage',
            new_name='related_Page',
        ),
    ]