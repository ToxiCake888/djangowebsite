# Generated by Django 5.2.1 on 2025-05-29 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('email', models.EmailField(max_length=80, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
