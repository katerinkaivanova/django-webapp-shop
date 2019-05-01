1. Добавила super user django geekbrains

2. Организовала выдачу сообщения об успешной отправке письма с кодом подтверждения в окне регистрации пользователя.

3. Реализовала активацию пользователя при переходе по ссылке из письма.

Из-за ошибки "Error activation user :
('You have multiple authentication backends configured and
therefore must provide the `backend` argument or set the `backend` attribute on the user.',)"

Добавила backend auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend').
Я так поняла, что это из-за нескольких конфигураций backend в AUTHENTICATION_BACKENDS?
Необходимо будет везде однозначно указывать?

4. Создала контекстный процессор для корзины и скорректировала код контроллеров основного приложения.
Мы сделали контекстный процессор для basket в «mainapp». В других приложениях нужно отдельно создавать
контекстный процессор, если нужен тот же самый basket, например?

to do list:

1. Переехать с MacOS на Ubuntu, установить DB Browser for SQLite

2. Перевести полностью пространоство имён на namespace. Менять path на url не буду, если можно

3. Заменить везде <button> на <a>

4. Стилизовать custom admin, basket и authentication -> с красотой там всё плохо

5. Добавить paginator. В django1 был не обязателен.