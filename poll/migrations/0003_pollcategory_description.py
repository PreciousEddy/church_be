# Generated by Django 4.0.8 on 2023-01-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_alter_poll_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollcategory',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]