from django import forms


class NameForm(forms.Form):
    url_field = forms.URLField()