"""
Definition of views.
"""

from app import forms #auto added by django for forms
from django.http import HttpResponseRedirect #forms
from django.shortcuts import render #forms
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.conf.urls.static import static

from .forms import NameForm

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
            'title':'Title Placeholder',
            'picture':'Picture Placeholder',
            'ingredients':'Ingredients PH',
            'comments':'Comments PH',
            'favourite':'favourite button PH',
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
            'search':'Search',
            'sortBy':'Select the search criteria:',
            'sortOrder':'Select the order you wish for them to appear in:',
            'searchbar':'search bar PH',
        }
    )

def invite(request):
    #Holder for sending e-mails
    send_mail('Subject here','Here is the message.','HostHeritageRecipes@gmail.com',['flippersticker@hotmail.com'],fail_silently=False)
    """Renders the invite page."""
    assert isinstance(request, HttpRequest)
    #Testing sending mail when visiting the invite page
    return render(
        request,
        'app/invite.html',
        {
            'title':'Invite Others',
            'firstName':'First Name entry form',
            'lastName':'Last Name entry form',
            'email':'e-mail entry form',
            'message':'message entry form',
            #'sendmail':send_mail('Subject here','Here is the message.','HostHeritageRecipes@gmail.com',['flippersticker@hotmail.com'],fail_silently=False),
        }
    )


def getname(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid(): #calling is valid function from the form. 
            return HttpResponseRedirect('/thanks/') #placeholder to check comment is valid
    else:
        form = NameForm()
    return render(request, 'Comment.html',{'form': form})

#issue with the form as a function is we have nothing to render??
#Think that is why it is throwing an error when I try to assign a url
#Returns get_name is not a valid view fucntion
