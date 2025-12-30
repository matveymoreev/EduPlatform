from encodings import undefined

from django.shortcuts import render,redirect
from django.http import HttpResponse

from EduApp.models import User

from django.contrib.auth.models import User as Usr
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def main(request):



    return render(request, "pages_main/main_page.html")



def oge_subjects(request):
    data = {"exam": "ОГЭ", "edu": "10 класс", "exam_details": "основному государственному экзамену"}
    return render(request, "pages_main/exam_subjects_page.html", context=data)



def acc(request):
    return render(request, "pages_main/account_page.html")



def ege_subjects(request):
    data = {"exam": "ЕГЭ", "edu": "институт", "exam_details": "единому государственному экзамену"}
    return render(request, "pages_main/exam_subjects_page.html", context=data)



def tst(request):
    return render(request, "pages_main/tst_page.html")

def number(request):
    return render(request, "pages_main/number_page.html")




def books(request):
    return render(request, "pages_main/books_page.html")




def login_page(request):
    reg_data = {}
    if request.method == "POST":
        reg_data["email"] = request.POST.get["email"]
        reg_data["password"] = request.POST.get["password"]
    return render(request, "pages_main/login_page.html")




def logout_page(request):
    return render(request, "pages_main/logout_page.html")

def auth_page(request):
    reg_data = {}
    context = {}
    if (request.method == "POST"):
        reg_data["name"] = request.POST.get("user_name", "undefined")
        reg_data["surname"] = request.POST.get("surname", "undefined")
        reg_data["email"] = request.POST.get("email", "undefined")
        reg_data["password"] = request.POST.get("password", "undefined")
        reg_data["password_repeat"] = request.POST.get("password_repeat", "undefined")
        reg_data["age"] = request.POST.get("age", -1)
        reg_data["check_terms"] = request.POST.get("check_terms", "undefined")
        reg_data["user_class"] = request.POST.get("user_class", "undefined")

        if len(User.objects.filter(email=reg_data("email"))):
            context["errors"] = {"login": "Пользователь с таким логином уже существует!"}
            return render(request, "pages_main/auth_page.html", context)
        if (reg_data["age"] > 100):
            context["errors"] = {"Дата рождения": "Ошибка даты рождения!"}
            return render(request, "pages_main/auth_page.html", context)
        if (reg_data["password"] == reg_data["password_repeat"]):
            context["errors"] = {"Пароль": "Ошибка при повторении пороля!"}
            return render(request, "pages_main/auth_page.html", context)




        """user = User.objects.create(name=reg_data["name"], age=reg_data["age"], surname=reg_data["surname"], email=reg_data["email"], password=reg_data["password"],
                                   class_id=0, about="",  birth_date=0, course_cnt=0, hours=0, progress=0, activity=0)"""
        usr = Usr.objects.create_user(reg_data["email"], reg_data["email"], reg_data["password"], first_name=reg_data["name"], last_name=reg_data["surname"])
        login(request, usr)
        return redirect("/")


    return render(request, "pages_main/auth_page.html")







