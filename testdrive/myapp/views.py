from django.shortcuts import render
from .forms import UserForm, CARS
from django.http import HttpResponse, HttpResponseRedirect

users = [
    {'name': 'Смирнов Д.В.',
     'phone': '8(952)345-85-12',
     'email': 'smirnov@gmal.com',
     'car': 'Ferrari SF90 Stradale'},
    {'name': 'Сидоров К.В',
     'phone': '8(988)745-22-93',
     'email': 'sidorov@gmal.com',
     'car': 'Dodge Challenger'},
    {'name': 'Моралин А.С.',
     'phone': '8(938)345-34-12',
     'email': 'moralin@gmal.com',
     'car': 'Bmw M5 F90 Competiton'}
]

def index(request):
    return render(request, "index.html", context={"users": users})

def about(request):
    return render(request, "about.html")

def record(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            phone = userform.cleaned_data["phone"]
            email = userform.cleaned_data["email"]
            car = int(userform.cleaned_data["car"])
            comment = userform.cleaned_data["comment"]
            car = list((filter(lambda elem: elem[0] == car, CARS)))[0][1]

            users.append({"name": name, "phone": phone, "email": email, "car": car})
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "record.html", {"form": userform})