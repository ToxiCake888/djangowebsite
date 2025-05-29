from .models import Contestant
from django.forms import ModelForm,TextInput

class RegistrationForm(ModelForm):
    class Meta:
        model=Contestant
        fields=["email", "fullName","password"]
        widgets={"email":TextInput(attrs={
            'type':"email",
            'class':"form-control",
            'id':"floatingEmail",
            'placeholder':"name@example.com"
        }),
        "fullName":TextInput(attrs={
            'type':"text",
            'class':"form-control",
            'id':"floatingFullName",
            'placeholder':"Your full name"
        }),
        "password":TextInput(attrs={
            'type':"password",
            'class':"form-control",
            'id':"floatingPassword",
            'placeholder':"Password"
        }),
        }