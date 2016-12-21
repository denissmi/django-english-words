from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import EnglishWord, RussianWord


def show_english(request):
    try:
        word_list = EnglishWord.objects.all()
    except ObjectDoesNotExist:
        raise Http404("English Words do not exist")
    context = {
        'word_list': word_list,
    }
    return render(request, 'show_words.html', context)


def show_russian(request):
    try:
        word_list = RussianWord.objects.all()
    except ObjectDoesNotExist:
        raise Http404("Russian Words do not exist")
    context = {
        'word_list': word_list,
    }
    return render(request, 'show_words.html', context)
