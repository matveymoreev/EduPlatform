from encodings import undefined

from django.shortcuts import render, redirect
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

