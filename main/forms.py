from .models import Contestant
from django.forms import ModelForm,TextInput

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
            'placeholder':" "
        }),
        "email":TextInput(attrs={
            'type':"email",
            'class':"form-control",
            'id':"floatingEmail",
            'placeholder':" "
        })

        }