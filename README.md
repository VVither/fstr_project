# Описание
fstr_project это тестовое REST API для внесения в базу данных информацию о перевалах

---

#### Важно
для корректной работы необходимо иметь базу данных **pereval**
В директории fstr необходимо создать файл .env с переменными

FSTR_DB_HOST=адрес сервера(localhost если хостом являетесь вы)

FSTR_DB_PORT=порт для подключения (обычно 5432)

FSTR_DB_LOGIN= логин пользователя базы данных(так как за основную СУБД взят postresql можно использовать пользователя postgres 
однако лучше создать пользователя с ограниченным доступом к базе данных)

FSTR_DB_PASS=пароль от пользователя

Данное REST API использует библиотеки django, django-rest-framework и drf-spectacular

перед началом работы убедитесь что у вас установлены данные библиотеки

**pip list**

В случае если они отсутствуют 

**pip install django, djangorestframework, drf-spectacular**

---

Для запуска необходимо находясь в директории fstr_project/fstr в консоли прописать **python manage.py runserver**

---

Более подробная документация доступна после запуска сервера по адресу **http://127.0.0.1:8000/schema/swagger/**
