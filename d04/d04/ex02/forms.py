from django import forms

class Myform(forms.Form):
    text = forms.CharField(required=True)