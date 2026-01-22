from encodings import undefined

from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
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


@login_required
def acc(request: WSGIRequest):
    data = {
        "full_name": "Имя не указано",
        "status": "Статус не указан",
        "courses_cnt": 0,
        "hours": 0,
        "progress": 0,
        "activity_today": 0,
        "email": "",
    }

    try:
        user = User.objects.get(email=request.user.username)

        if request.method == "POST":
            # получаем данные из запроса из полей формы email и password
            inp_name = ["user_name", "surname", "email", "birthDate", "userClass", "aboutUser", "courses_cnt", "hours", "progress", "activity_today"]
            inp_data = []
            db_data = [user.name, user.surname, user.email, user.birth_date, user.class_id, user.about, user.course_cnt, user.hours, user.progress, user.activity]
            for i in range(len(inp_name)):
                t = request.POST.get(inp_name[i], 0)
                if (t == "" or t == 0 or t == "0"):
                    inp_data.append(db_data[i])
                else:
                    inp_data.append(t)
            user.name = inp_data[0]
            user.surname = inp_data[1]
            user.email = inp_data[2]
            user.birth_date = inp_data[3]
            user.class_id = inp_data[4]
            user.about = inp_data[5]
            user.course_cnt = inp_data[6]
            user.hours = inp_data[7]
            user.progress = inp_data[8]
            user.activity = inp_data[9]

            # password = request.POST.get("password", "undefined")

            user.save()

        data["full_name"] = user.name + " " + user.surname
        data["status"] = user.status
        data["courses_cnt"] = user.course_cnt
        data["hours"] = user.hours
        data["progress"] = user.progress
        data["activity_today"] = user.activity

        data["password_now"] = user.password
        data["email"] = user.email

    except Exception as e:
        print(e)


    return render(request, "pages_main/account_page.html", context=data)



def ege_subjects(request):
    data = {
        "exam": "ЕГЭ",
        "edu": "институт",
        "exam_details": "единому государственному экзамену",
        "subj": "EGE",
    }
    return render(request, "pages_main/exam_subjects_page.html", context=data)


def books(request):
    return render(request, "pages_main/books_page.html")

