from django.db import models

class Contestant(models.Model):
    email=models.EmailField(max_length=80, primary_key=True)
    fullName=models.CharField(max_length=150)
    password=models.CharField(max_length=128)

    def __str__(self):
        return self.email
