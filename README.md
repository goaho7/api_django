## Описание
Публичное api на django с доступом по токену.

### Используемые технологии
- Python
- Django
- Django Rest framework
- Docker, Docker Compose
- Postgres
- Nginx

### Запуск проекта:

Клонировать репозиторий:

``` git clone git@github.com:goaho7/api_django.git ``` 

Запустить docker-compose:

``` docker compose up ```


Выполнить миграции:

``` docker compose exec backend python manage.py migrate ```

Выполнить команду сборки статики:

``` docker compose exec backend python manage.py collectstatic ```

Создать суперпользователя:

``` docker compose exec backend python manage.py createsuperuser ```

### В API доступны следующие эндпоинты:

* ```api/v1/generate```  POST-запрос с параметрами "id", "capibara_format", "capibara_slang" и "capcapibara_phrasesibara_format":
```
{
    "id": {"type": "number"},
    "capibara_format": {"type": "string"},
    "capibara_slang": {"type": "string"},
    "capibara_phrases": {"type": "array"}
}
```
* ```/api/v1/statement/{id}``` GET-запрос – вернет файл xlsx формата с записью из БД по id. Если таковых нет, возвращает {"status": "not available"}.
* ```/api/v1/statements/{capibara_slang}``` GET-запрос – вернет файл xlsx формата с записями из БД сгруппированных по capibara_slang. Если таковых нет, возвращает {"status": "not available"}.


### Автор проекта:

[Александр Савельев](https://github.com/goaho7)