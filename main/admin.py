from django.contrib import admin
from .models import Answer, Results, Persons


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'option1', 'option2')
    readonly_fields = ('name', 'option1', 'option2')


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'file')
    readonly_fields = ('name', 'description', 'file')


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'email', 'result',
                    'score', 'user_ie', 'user_sn', 'user_tf', 'user_jp')
    readonly_fields = ('name', 'phone', 'email', 'result',
                       'score', 'user_ie', 'user_sn', 'user_tf', 'user_jp')