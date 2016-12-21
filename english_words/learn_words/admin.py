from django.contrib import admin

from .models import EnglishWord, RussianWord

admin.site.register(EnglishWord)
admin.site.register(RussianWord)