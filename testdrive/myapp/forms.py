from django import forms

CARS = ((1, "Ferrari SF90"), (2, "Dodge Challenger"), (3, "Bmw M5 F90 Competiton"))

class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = forms.CharField(label='Телефон')
    email = forms.CharField(label='Почта')
    car = forms.ChoiceField(label='Авто', choices=CARS)
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)
