"""
Definition of urls for DjangoWeb.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
#Not good for production
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^profile$', app.views.profile, name='profile'),
    url(r'^family$', app.views.family, name='family'),
    url(r'^recipes$', app.views.recipes, name='recipes'),
    url(r'^findRecipes$', app.views.findRecipes, name='findRecipes'),
    url(r'^invite$', app.views.invite, name='invite'),
    #url(r'^Comment$', app.views.about, name='Comment'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()