from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
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
            return render_to_response('registration/login.html', args)
    else:
        return render_to_response('registration/login.html', args)


def log_out(request):
    logout(request)
    return redirect('/login/')