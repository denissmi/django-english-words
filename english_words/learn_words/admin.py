from django.contrib import admin

from .models import EnglishWord
from .models import RussianWord

admin.site.register(EnglishWord)
admin.site.register(RussianWord)