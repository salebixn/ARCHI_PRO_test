# Generated by Django 4.1.7 on 2023-04-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Вопросы', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AddField(
            model_name='answer',
            name='number_image',
            field=models.ImageField(null=True, upload_to='numbers_images', verbose_name='Изображение номера вопроса'),
        ),
    ]
