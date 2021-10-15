from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(max_length=80)

class BirthdayForm(forms.Form):
    birthyear = forms.IntegerField(max_value=2050, min_value=0)

class OrderForm(forms.Form):
    burgers = forms.IntegerField(min_value=0)
    fries = forms.IntegerField(min_value=0)
    drinks = forms.IntegerField(min_value=0)

class HundredForm(forms.Form):
    number = forms.IntegerField()

class StringForm(forms.Form):
    string = forms.CharField(max_length=200)

class CatDogForm(forms.Form):
    string = forms.CharField(max_length=200)

class LoneSumForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()