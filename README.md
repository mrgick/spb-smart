# Санкт-Петербург - умный город.
Данный проект является прототипом сайта, который был создан участниками "<a href="https://hacklife.fun/">Хакатона</a>".
Вы можете посмотреть сайт на http://nick100lay.pythonanywhere.com/.
***

***
## Команда Code&Luck (ПсковГУ)
### Люди, участвовавшие в создании прототипа:
1. <b>Капитан </b><a href="https://github.com/mrgick/">mrgick</a> <i>(Кодинг, дизайн и презентация)</i>
2. <a href="https://github.com/miha6g/">miha6g</a> <i>(Дизайн и презентация)</i>
3. <a href="https://github.com/tweek36/">tweek36</a> <i>(Кодинг)</i>
4. <a href="https://github.com/nick100lay/">nick100lay</a> <i>(Кодинг и настройка)</i>
5. <a>Егор</a> <i>(Видео и презентация)</i>
***

>Использовался фреймворк "<a href="https://www.djangoproject.com/">Django 3</a>".

***
## Тестовые пользователи (логин: пароль):
* <b>admin: admin</b> - суперпользователь
***

***
## Запуск сервера локально
### Что нужно сделать:
1. Установить <a href="https://www.python.org/">python</a> версии 3.8.6 вместе с <a href="https://pypi.org/project/pip/">pip</a>
2. Открыть терминал (cmd.exe на Windows) и прописать `pip install Django=3.1.3` 
3. Склонировать репозиторий себе на диск и перейти в директорию проекта, где находится файл manage.py (`cd %Путь, куда вы склонировали проект%`)  
4. Прописать `python manage.py runserver` или `python3 manage.py runserver`
5. Открыть браузер и в адресной строке прописать локальный IP адрес машины, на которой запущен сервер, с портом 8000 (`%Локальный_IP%:8000`)
***

***
## Возможности проекта на данный момент:
* Реализован вход, выход и временная регистрация пользователей.
* Реализовано создание, просмотр, оценивание и сортировка по рейтингу предложений.
* Реализованы 3 вкладки типа постов: топ, в процессе, архив.
* На сайте реализовано разделение пользователей на группы (права):
  * <b>moderator</b> (просмотр, добавление, изменение и удаление предложений; вход в админ панель; просмотр пользователей);
  * <b>vlast</b> (просмотр, добавление, изменение предложений; вход в админ панель); 
  * <b>обычный пользователь</b> (просмотр, добавление предложений).

## Дальнейшие изменения, чтобы довести проект до полноценного:
* Реализовать систему комментариев
* Реализовать отсылку новых предложений к модераторам на проверку
* Реализовать дополнительные меню для аккаунтов с группой модератор, власть (реализовать изменение, удаление предложений не через админ панель)
* Реализовать профиль пользователя
* Реализовать регистрацию через вк и госуслуги
* Переработать дизайн
***
