from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
    return HttpResponse(html_content)


def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
# Create your views here.
