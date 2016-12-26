from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from .models import EnglishWord, RussianWord


def show_english(request):
    try:
        user = User.objects.get(username=request.user.username)
        word_list = EnglishWord.objects.filter(author=user.id)
    except ObjectDoesNotExist:
        raise Http404("English Words do not exist")
    context = {
        'word_list': word_list,
    }
    return render(request, 'show_words.html', context)


def show_russian(request):
    try:
        user = User.objects.get(username=request.user.username)
        word_list = RussianWord.objects.filter(author=user.id)
    except ObjectDoesNotExist:
        raise Http404("Russian Words do not exist")
    context = {
        'word_list': word_list,
    }
    return render(request, 'show_words.html', context)
