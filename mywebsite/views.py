from django.shortcuts import render

def index(request):
    context = {
        "heading": "Home Page",
    }
    return render(request, "index.html", context)