"""
В дополнение к встроенным приложениям Django,
часто используются сторонние библиотеки и приложения,
которые могут значительно облегчить разработку.
Вот список некоторых из наиболее популярных и полезных приложений,
которые часто добавляются в `INSTALLED_APPS`:

1. **`rest_framework`** (Django REST framework)
   - Используется для создания RESTful API.
   - Установка: `pip install djangorestframework`
   ```python
   'rest_framework',
   ```

2. **`corsheaders`** (Django CORS Headers)
   - Позволяет обрабатывать запросы CORS.
   - Установка: `pip install django-cors-headers`
   ```python
   'corsheaders',
   ```

3. **`django_extensions`** (Django Extensions)
   - Предоставляет множество полезных команд и инструментов для разработки.
   - Установка: `pip install django-extensions`
   ```python
   'django_extensions',
   ```

4. **`crispy_forms`** (Django Crispy Forms)
   - Упрощает создание гибких и красивых форм.
   - Установка: `pip install django-crispy-forms`
   ```python
   'crispy_forms',
   ```

5. **`allauth`** (Django Allauth)
   - Полнофункциональная система аутентификации, регистрации и управления учетными записями.
   - Установка: `pip install django-allauth`
   ```python
   'allauth',
   'allauth.account',
   'allauth.socialaccount',
   ```

6. **`debug_toolbar`** (Django Debug Toolbar)
   - Инструмент для отладки и профилирования запросов.
   - Установка: `pip install django-debug-toolbar`
   ```python
   'debug_toolbar',
   ```

7. **`ckeditor`** (Django CKEditor)
   - Интеграция WYSIWYG-редактора CKEditor с Django.
   - Установка: `pip install django-ckeditor`
   ```python
   'ckeditor',
   ```

8. **`storages`** (Django Storages)
   - Позволяет использовать различные хранилища для медиа и статических файлов, такие как AWS S3.
   - Установка: `pip install django-storages`
   ```python
   'storages',
   ```

9. **`rest_framework.authtoken`** (Django REST framework token authentication)
   - Аутентификация на основе токенов для REST API.
   - Установка: `pip install djangorestframework`
   ```python
   'rest_framework.authtoken',
   ```

10. **`django_filters`** (Django Filter)
    - Простая система фильтрации для Django REST framework.
    - Установка: `pip install django-filter`
    ```python
    'django_filters',

11. **`drf_yasg`** (Django REST framework - Yet Another Swagger Generator)
    - Генератор документации API на основе Swagger/OpenAPI.
    - Установка: `pip install drf-yasg`
    ```python
    'drf_yasg',
    ```

12. **`django_celery_beat`** (Django Celery Beat)
    - Планировщик задач для Celery с интеграцией в Django.
    - Установка: `pip install django-celery-beat`
    ```python
    'django_celery_beat',
    ```

13. **`django_celery_results`** (Django Celery Results)
    - Хранение результатов выполнения задач Celery в базе данных Django.
    - Установка: `pip install django-celery-results`
    ```python
    'django_celery_results',
    ```

Эти приложения покрывают широкий спектр функциональности, от создания API
и аутентификации до отладки и работы с формами.
Выбирая приложения, ориентируйтесь на потребности вашего проекта.


    # ПРИМЕР
    # Добавьте эту строку в список приложений
    'rest_framework',

"""