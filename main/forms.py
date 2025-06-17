from .models import Contestant
from django.forms import ModelForm,TextInput
from django.db import models
from django.core.validators import RegexValidator
class RegistrationForm(ModelForm):
    class Meta:
        model=Contestant
        fields=["fullName", "organization","phone", "email"]
        widgets={
        "fullName":TextInput(attrs={
            'type':"text",
            'class':"form-control",
            'id':'floatingFullName',
            'placeholder':' '
        }),
        "organization":TextInput(attrs={
            'type':"text",
            'class':"form-control",
            'id':"floatingOrganization",
            'placeholder':" "
        }),
        "phone":TextInput(attrs={
            'type':"tel",
            'class':"form-control",
            'id':"floatingPhone",
            'data-phone-pattern': '+7 (###) ###-##-##',
            'placeholder':" ",
            'pattern': r'^(\+7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'
        }),
        "email":TextInput(attrs={
            'type':"email",
            'class':"form-control",
            'id':"floatingEmail",
            'placeholder':" "
        })

        }
    