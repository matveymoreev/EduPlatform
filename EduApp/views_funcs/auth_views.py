from encodings import undefined

from django.shortcuts import render, redirect
from django.http import HttpResponse

# наща таблица пользователя в БД
from EduApp.models import User
# пользователь из стандартной таблицы регистрации БД
from django.contrib.auth.models import User as DefUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# войти в аккаунт
def login_page(request):
    pagename = "pages_main/login_page.html"
    context = {}
    context["errors"] = -1
    # проверяем, что запрос был на отправку данных формы на сервер
    if request.method == "POST":
        # получаем данные из запроса из полей формы email и password
        username = request.POST.get("email", "undefined")
        password = request.POST.get("password", "undefined")
        # попытка авторизации
        usr = authenticate(username=username, password=password)
        # если не получилось аутентифицировать пользователя
        if not usr:
            context["errors"] = "Не удалось войти"
            return render(request, pagename, context)
        # авторизуемся
        login(request, usr)
        return redirect("/")

    # если просто зашли на страницу
    return render(request, pagename, context)

# выйти из аккаунта
# @login_required
def logout_page(request):
    logout(request)
    return redirect("/")

# авторизоваться
def auth_page(request):
    reg_data = {}
    context = {}
    if (request.method == "POST"):
        reg_data["name"] = request.POST.get("user_name", "undefined")
        reg_data["surname"] = request.POST.get("surname", "undefined")
        reg_data["email"] = request.POST.get("email", "undefined")
        reg_data["password"] = request.POST.get("password", "undefined")
        reg_data["password_repeat"] = request.POST.get("password_repeat", "undefined")
        reg_data["age"] = int(request.POST.get("age", -1))
        reg_data["check_terms"] = request.POST.get("check_terms", "undefined")
        reg_data["user_class"] = request.POST.get("user_class", "undefined")

        # обращаемся к таблице User в БД, получаем через objects все записи в таблице
        # фильтруем данные по параметру email
        if (len(User.objects.filter(email=reg_data["email"])) or len(DefUser.objects.filter(email=reg_data["email"]))):
            context["errors"] = "Логин: Пользователь с таким логином уже существует!"
            # возвращаем страницу с выводом ошибки
            return render(request, "pages_main/auth_page.html", context=context)
        # проверка возраста
        if (reg_data["age"] > 100):
            context["errors"] = "Дата рождения: Ошибка даты рождения!"
            return render(request, "pages_main/auth_page.html", context=context)
        # проверяем совпадение полей пароль и повторить пароль
        if (reg_data["password"] != reg_data["password_repeat"]):
            context["errors"] = "Пароль: Ошибка при повторении пороля!"
            return render(request, "pages_main/auth_page.html", context=context)

        # если ошибок в заполнении формы не было, идем дальше

        # добавляем пользователя в нашу таблицу в БД
        user = User.objects.create(name=reg_data["name"], age=reg_data["age"], surname=reg_data["surname"], email=reg_data["email"], password=reg_data["password"],
                                   class_id=0, about="",  birth_date="2003-12-12", course_cnt=0, hours=0, progress=0, activity=0)
        # добавляем пользователя в стандартную таблицу зарегистрированных пользователей
        usr = DefUser.objects.create_user(reg_data["email"], reg_data["email"], reg_data["password"], first_name=reg_data["name"], last_name=reg_data["surname"])
        # системная функция авторизации
        login(request, usr)
        # если успешно вошли, меняем кнопки регистрации и войти на кнопку аккаунта
        context["logIn"] = True
        # если авторизация прошла успешно, переходим на главную страницу
        # return render(request, "pages_main/main_page.html")
        return redirect("/")

    return render(request, "pages_main/auth_page.html", context=context)
