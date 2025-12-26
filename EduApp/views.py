from django.shortcuts import render
from django.http import HttpResponse


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

def auth(request):
    return render(request, "pages_main/auth_page.html")
def login_page(request):
    return render(request, "pages_main/login_page.html")
def logout_page(request):
    return render(request, "pages_main/logout_page.html")
def registration_page(request):
    return render(request, "pages_main/registration_page.html")



