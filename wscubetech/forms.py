from django import forms

class UserForms(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    phoneno = forms.CharField()
    