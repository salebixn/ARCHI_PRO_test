# Generated by Django 4.1.7 on 2023-04-03 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_answer_options_answer_number_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='number_image',
        ),
    ]
