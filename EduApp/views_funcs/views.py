from encodings import undefined

from django.shortcuts import render,redirect
from django.http import HttpResponse

# наща таблица пользователя в БД
from EduApp.models import User
# пользователь из стандартной таблицы регистрации БД
from django.contrib.auth.models import User as DefUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def main(request):

    return render(request, "pages_main/main_page.html")



def oge_subjects(request):
    data = {
        "exam": "ОГЭ",
        "edu": "10 класс",
        "exam_details": "основному государственному экзамену",
        "subj": "OGE",
            }
    return render(request, "pages_main/exam_subjects_page.html", context=data)



def acc(request):
    return render(request, "pages_main/account_page.html")



def ege_subjects(request):
    data = {
        "exam": "ЕГЭ",
        "edu": "институт",
        "exam_details": "единому государственному экзамену",
        "subj": "EGE",
            }
    return render(request, "pages_main/exam_subjects_page.html", context=data)



def number(request):
    data = {
        "text": "На тарелке лежат одинаковые на вид пирожки: 4 с мясом, 8 с капустой и 3 с вишней. Петя наугад берёт один пирожок. Найдите вероятность того, что пирожок окажется с вишней.",
        "difficulty": "базовый",
        "object": "Арифметика",
        "Explanation": "Всего пирожков: 4 + 8 + 3 = 15. Пирожков с вишней: 3. Вероятность = 3/15 = 1/5 = 0.2",
        "done": 0,
        "right": 0,
        "Errors": 0,
    }
    return render(request, "pages_main/number_page.html")

def books(request):
    return render(request, "pages_main/books_page.html")

# войти в аккаунт
def login_page(request):
    reg_data = {}
    # проверяем, что запрос был на отправку данных формы на сервер
    if request.method == "POST":
        # получаем данные из запроса из полей формы email и password
        reg_data["email"] = request.POST.get["email"]
        reg_data["password"] = request.POST.get["password"]
    # проверить, что есть в БД
    return render(request, "pages_main/login_page.html")

# выйти из аккаунта
def logout_page(request):
    # ДОДЕЛАТЬ ВЫХОД
    # logout(request)
    return render(request, "pages_main/logout_page.html")

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
        return redirect("/")

    return render(request, "pages_main/auth_page.html", context=context)
