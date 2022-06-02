# __Проект «API для Yatube»__

## __Описание__:

API соцсети Yatube для публикации постов.

## __Установка__:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:InsomniaTSO/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## __Примеры запросов__:

Получение JWT-токена:

```
POST http://127.0.0.1:8000/api/v1/jwt/create/
```

Получить список всех публикаций:

```
GET http://127.0.0.1:8000/api/v1/posts/
```

Добавление новой публикации:

```
POST http://127.0.0.1:8000/api/v1/posts/
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Получение всех комментариев к публикации:

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Добавление нового комментария к публикации:

```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
{
"text": "string"
}
```

Получение списка доступных сообществ:

```
GET http://127.0.0.1:8000/api/v1/groups/
```

Возвращает все подписки пользователя, сделавшего запрос:

```
GET http://127.0.0.1:8000/api/v1/follow/
```

Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса:
```
http://127.0.0.1:8000/api/v1/follow/
{
"following": "string"
}
<<<<<<< HEAD
```
=======
```
>>>>>>> af272eed4dd6030a60c43eabe22756f4d3dfe331
