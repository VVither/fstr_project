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

---

Для запуска необходимо находясь в директории fstr_project/fstr в консоли прописать **python manage.py runserver**
