from django import forms
from django.core import validators
from conjecture_app.models import conjecture_model


class Collatz_Form(forms.Form):
    number=forms.IntegerField(min_value=1,max_value=100)
    
