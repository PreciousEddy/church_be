# Generated by Django 4.0.8 on 2023-01-22 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_publication_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='tags',
        ),
    ]