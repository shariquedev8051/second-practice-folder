from django import forms

class GeekForm(forms.Form):
    name = forms.CharField()
    geek_field = forms.FileField()



