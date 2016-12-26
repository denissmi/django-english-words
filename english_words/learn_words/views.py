from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from .models import EnglishWord, RussianWord


def show_words(request, model_name):
    context = {
        'word_list': None,
        'warning_message': None
    }
    try:
        try:
            user = User.objects.get(username=request.user.username)
        except ObjectDoesNotExist:
            context['warning_message'] = 'You are not authorized.'
            return render(request, 'show_words.html', context)
        word_list = model_name.objects.filter(author=user.id)
    except ObjectDoesNotExist:
        raise Http404("Words do not exist")
    context['word_list'] = word_list
    context['warning_message'] = 'No words are available.'
    return render(request, 'show_words.html', context)


def show_english(request):
    return show_words(request, EnglishWord)


def show_russian(request):
    return show_words(request, RussianWord)
