from django.http.response import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from users.forms import UserForm


# Login functionality
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/login.html", context)
    else:
        context = {
            "title": "Login",

        }
        return render(request, "users/login.html", context)

#logout functionality
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))
# Login functionality
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/login.html", context)
    else:
        context = {
            "title": "Login",

        }
        return render(request, "users/login.html", context)

#logout functionality
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))

# signup functionality
def signup(request):

    if request.method == 'POST':
        
        form=UserForm(request.POST)
        if form.is_valid():
                first_name=form.cleaned_data["first_name"]
                password=form.cleaned_data["password"]
                username=form.cleaned_data["username"]
                user = User.objects.create_user(username=username, first_name=first_name, password=password)
                user.save()
                context = {
                    "message": "account created successfully",
                    "title": "TechiesPark| Registration"
                }
                return render(request, 'users/login.html', context=context)
                
        else:
                context = {
                    "title": "OnlineStore| Registration",
                    "form": form,
                }
                return render(request, 'users/registration.html', context)

    else:
        form=UserForm()
        context = {
            "title": "OnlineStore| Registration",
            "form": form,
        }
    return render(request, 'users/registration.html', context)

