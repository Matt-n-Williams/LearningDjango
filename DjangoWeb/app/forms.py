"""
Definition of forms.
"""

from django import forms #form library 
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

#Building basic comment form w/max char=240

from django import forms

class NameForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea)
    #parent_id = forms.CharField(widget=forms.HiddenInput, required = False)
    #lifted from djangoproject.com/en/2.a/topics/forums/

