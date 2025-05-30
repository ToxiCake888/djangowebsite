from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.db import IntegrityError

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("Данные формы:", request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация успешна!")
            return redirect('homePage')
        else:
            for field, errors in form.errors.items():
                print(f"Поле {field}: {', '.join(errors)}")
            messages.error(request, "ошибки в форме")

    return render(request, 'main/registration.html')

def index(request):
    return render(request, 'main/index.html')