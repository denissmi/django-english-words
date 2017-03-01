from django.contrib import admin

from .models import EnglishWord, RussianWord


class AdminEnglishWord(admin.ModelAdmin):
    fields = ['word', 'translation', 'author']


class AdminRussianWord(admin.ModelAdmin):
    fields = ['word', 'translation', 'author']

admin.site.register(EnglishWord, AdminEnglishWord)
admin.site.register(RussianWord, AdminRussianWord)