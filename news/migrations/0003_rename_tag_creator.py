# Generated by Django 4.2.5 on 2023-09-16 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_review_managers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Creator',
        ),
    ]