from django.db import models
from django.core.validators import RegexValidator

class Contestant(models.Model):
    email=models.EmailField(max_length=80, primary_key=True)
    fullName=models.CharField(max_length=150)
    phone=models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^(\+7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$')]
    )
    organization=models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.email
