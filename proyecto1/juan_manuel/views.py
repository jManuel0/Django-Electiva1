from django.shortcuts import render


def index(request):
    return render(request, "juan_manuel/index.html")
