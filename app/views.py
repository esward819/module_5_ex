from django.shortcuts import render
from app.forms import HelloForm, BirthdayForm, OrderForm, HundredForm, StringForm, CatDogForm, LoneSumForm
# Create your views here.
def root(request):
    form = HelloForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        return render(request, "root.html", {"form": form, "name":name})
    else:
        return render(request, "root.html", {"form": form})

def birthday(request):
    form = BirthdayForm(request.GET)
    if form.is_valid():
        answer = 2050 - form.cleaned_data["birthyear"]
        return render(request, "birthday.html", {"form": form, "answer":answer})
    else:
        return render(request, "birthday.html", {"form": form})

def food(request):
    form = OrderForm(request.GET)
    if form.is_valid():
        burgers = 4.5 * form.cleaned_data["burgers"]
        fries = 1.5 * form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = burgers + fries + drinks
        return render(request, "food.html", {"form": form, "burgers": burgers, "fries": fries, "drinks": drinks, "total": total})
    else:
        return render(request, "food.html", {"form": form})

def hundred(request):
    form = HundredForm(request.GET)
    if form.is_valid():
        number = form.cleaned_data["number"]
        return render(request, "hundred.html", {"form": form, "number": number})
    else:
        return render(request, "hundred.html", {"form": form})

def string_splosion(request):
    form = StringForm(request.GET)
    if form.is_valid():
        string = form.cleaned_data["string"]
        result = ""
        for i in range(len(string)):
            result = result + string[:i+1]
        return render(request, "string.html", {"form": form, "result": result})
    else:
        return render(request, "string.html", {"form": form})

def cat_dog(request):
    form = CatDogForm(request.GET)
    if form.is_valid():
        string = form.cleaned_data["string"]
        cat = 0
        dog = 0
        cat_dog = False
        for i in range(len(string)):
            if string[i:i+3] == "cat":
                cat += 1
            elif string[i:i+3] == "dog":
                dog += 1
        if cat == dog:
            cat_dog = True
        return render(request, "cat_dog.html", {"form": form, "cat_dog": cat_dog})
    else:
        return render(request, "cat_dog.html", {"form": form})

def lone_sum(request):
    form = LoneSumForm(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]
        result = 0
        if a == b == c:
            pass
        elif b == c:
            result = a
        elif a == c:
            result = b
        elif a == b:
            result = c
        else:
            result = (a+b+c)
        return render(request, "lone_sum.html", {"form": form, "result": result})
    else:
        return render(request, "lone_sum.html", {"form": form})
