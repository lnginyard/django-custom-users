from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from customuser.settings import AUTH_USER_MODEL
from customuser_app.forms import AddCustomUser, LoginForm
from customuser_app.models import MyUser


def index(request):
    html = "index.html"
    content = AUTH_USER_MODEL
    if request.user.is_authenticated:
        return render(request, html, {"content": content})
    return redirect("/login/")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, "login_form.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def adduser_view(request):
    if request.method == "POST":
        form = AddCustomUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            new_user = MyUser.objects.last()
            new_user.set_password(raw_password=data['password'])
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
        return render(request, "adduser_form.html", {"form": form})
    form = AddCustomUser()
    return render(request, "adduser_form.html", {"form": form})
