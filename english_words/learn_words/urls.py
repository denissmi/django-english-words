from django.conf.urls import url
from learn_words import views

urlpatterns = [
    url(r'^show/english/$', views.show_english, name='show_english'),
    url(r'^show/russian/$', views.show_russian, name='show_russian'),
]
