from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def log_in(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/learn_words/show/english/')
        else:
            args['login_error'] = "User is not found"
            return render(request, 'registration/login.html', args)
    else:
        return render(request, 'registration/login.html', args)


def log_out(request):
    logout(request)
    return redirect('/login/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            login(request, new_user)
            return redirect('/learn_words/show/english/')
        else:
            args['form'] = new_user_form
    return render('registration/register.html', args)