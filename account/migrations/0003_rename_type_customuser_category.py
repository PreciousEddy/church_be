# Generated by Django 4.0.8 on 2023-01-03 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_options_customuser_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='type',
            new_name='category',
        ),
    ]