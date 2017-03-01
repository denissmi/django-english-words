from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.template.context_processors import csrf
from .models import EnglishWord, RussianWord


def show_words(request, english=True):
    context = {
        'word_list': None,
        'warning_message': None,
        'english': english
    }
    context.update(csrf(request))

    try:
        user = User.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        context['warning_message'] = 'You are not authorized.'
        return render(request, 'show_words.html', context)

    if request.POST:
        delete_words(request.POST.getlist('marked_words'), english, user.id)

    try:
        if english:
            word_list = EnglishWord.objects.filter(author=user.id)
        else:
            word_list = RussianWord.objects.filter(author=user.id)
    except ObjectDoesNotExist:
        raise Http404("Words do not exist")

    context['word_list'] = word_list
    context['warning_message'] = 'No words are available.'

    return render(request, 'show_words.html', context)


def delete_words(marked_words, english, user_id):
    if english:
        EnglishWord.objects.filter(word__in=marked_words, author=user_id).delete()
    else:
        RussianWord.objects.filter(word__in=marked_words, author=user_id).delete()


def show_english(request):
    return show_words(request)


def show_russian(request):
    return show_words(request, english=False)


def add_word(request):
    extra_symbols = ['.', ';']
    context = {}
    context.update(csrf(request))

    if request.POST:
        english = remove_extra_spaces(request.POST['english'])
        russian = split_words(request.POST['russian'])
        context['english'] = english
        context['russian'] = ', '.join(russian)

        try:
            user = User.objects.get(username=request.user.username)
        except ObjectDoesNotExist:
            context['warning_message'] = 'You are not authorized.'
            return render(request, 'add_word.html', context)

        for word in russian:
            if True in (symbol in word for symbol in extra_symbols):
                context['warning_message'] = word + ' russian word is not correct. ' \
                                     'Probably you entered one of ' + ' '.join(extra_symbols) + ' symbols.'
                return render(request, 'add_word.html', context)

        save_english(english, russian, user)
        save_russian(english, russian, user)
    return render(request, 'add_word.html')


def remove_extra_spaces(word):
    return ' '.join(word.split())


def split_words(words):
    return [remove_extra_spaces(word) for word in words.split(',') if word]


def save_english(english, russian, user):
    try:
        english_word = EnglishWord.objects.get(word=english, author=user.id)
        translation = english_word.translation.split(',')
        for word in russian:
            if word not in translation:
                translation.append(word)
        english_word.translation = ','.join(translation)
        english_word.save()
    except ObjectDoesNotExist:
        english_word = EnglishWord(word=english, translation=','.join(russian), author=user)
        english_word.save()


def save_russian(english, russian, user):
    for word in russian:
        try:
            russian_word = RussianWord.objects.get(word=word, author=user.id)
            translation = russian_word.translation.split(',')
            if english not in translation:
                translation.append(english)
            russian_word.translation = ','.join(translation)
            russian_word.save()
        except ObjectDoesNotExist:
            russian_word = RussianWord(word=word, translation=english, author=user)
            russian_word.save()
