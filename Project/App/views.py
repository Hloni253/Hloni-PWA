from django.shortcuts import render, redirect
from .models import AppModel

def page(request):
    if request.user.is_authenticated:
        return render(request, "App/beh.html")
    else:
        return redirect('home')

def home(request):
    apps = AppModel.objects.all()

    context = {
        "apps":apps
        }
    return render(request, "App/home.html", context)

def my_app(request, id):
    app = AppModel.objects.get(id=id)

    context = {
        "app":app,
        }

    return render(request, "App/app.html", context)
