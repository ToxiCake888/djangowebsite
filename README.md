# djangowebsite

# Описание

Это сайт для регистрации на олимпиаде, присутствует запись информации об участниках в БД postgres.
Для внешнего вида использовался макет из figma и bootstrap.
Серверная часть выполнена на python django.

# Стек технологий

- Python 3.12
- Html/css
- Django
- Bootstrap
- Postgres

# Запуск

1. Иметь установленными python, pip, postgres

2. Скачать репозиторий (git clone или просто архивом)

3. Включить виртуальное окружение

Создать venv: `python -m venv venv`
Включить venv: `.\venv\Scripts\activate`

4. Установка зависимостей

`pip install -r requirements.txt`

5. Миграции

`python manage.py migrate`

6. Запуск сервера

`python manage.py runserver`

7. Открыть ссылку http://127.0.0.1:8000
   > Возможно потребуется настроить DATABASES в файле settings.py ,если c базой данных что-то будет не так и она перенесется неверно.
