from django.db import models


class Answer(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Вопрос')
    option1 = models.CharField(max_length=255, null=True, verbose_name='Первый вариант ответа')
    option2 = models.CharField(max_length=255, null=True, verbose_name='Ворой вариант ответа')

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.pk} - {self.name}'
    

class Results(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Буквенный результат')
    description = models.TextField(max_length=1000, null=True, verbose_name='Описание')
    file = models.FileField(upload_to='files', null=True, verbose_name='Файл с подробным описанием')
    

    class Meta:
        verbose_name = 'Результаты'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'Результат №{self.pk} - {self.name}'
    

class Persons(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Имя')
    phone = models.IntegerField(null=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=255, null=True, verbose_name='Email')
    result = models.ForeignKey(Results, on_delete=models.CASCADE, verbose_name='Результат пользователя')
    score = models.IntegerField(null=True, verbose_name='Общий балл')
    user_ie = models.IntegerField(null=True, verbose_name='user_ie')
    user_sn = models.IntegerField(null=True, verbose_name='user_sn')
    user_tf = models.IntegerField(null=True, verbose_name='user_tf')
    user_jp = models.IntegerField(null=True, verbose_name='user_ip')

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name} - {self.email}'