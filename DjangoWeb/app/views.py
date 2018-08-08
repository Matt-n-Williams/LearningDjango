"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page. Check me for changes.',
            'year':datetime.now().year,
        }
    )

def profile(request):
    """Renders the Profile Page page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profile.html',
        {
            'username':'Username Placeholder',
            'commentsMade':'Comments Made Placeholder.',
            'recipeList':'Recipe List Placeholder',
            'favouriteRecipes':'Favourite Recipes Placeholder',
        }
    )

def recipes(request):
    """Renders the Recipes page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/recipes.html',
        {
            'username':'Username Placeholder',
            'commentsMade':'Comments Made Placeholder.',
            'recipeList':'Recipe List Placeholder',
            'favouriteRecipes':'Favourite Recipes Placeholder',
        }
    )

def family(request):
    """Renders the family page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/family.html',
        {
            'username':'Username Placeholder',
            'commentsMade':'Comments Made Placeholder.',
            'recipeList':'Recipe List Placeholder',
            'favouriteRecipes':'Favourite Recipes Placeholder',
        }
    )

def findRecipes(request):
    """Renders the Find Recipes page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/findRecipes.html',
        {
            'username':'Username Placeholder',
            'commentsMade':'Comments Made Placeholder.',
            'recipeList':'Recipe List Placeholder',
            'favouriteRecipes':'Favourite Recipes Placeholder',
        }
    )

def invite(request):
    """Renders the invite page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/invite.html',
        {
            'username':'Username Placeholder',
            'commentsMade':'Comments Made Placeholder.',
            'recipeList':'Recipe List Placeholder',
            'favouriteRecipes':'Favourite Recipes Placeholder',
        }
    )