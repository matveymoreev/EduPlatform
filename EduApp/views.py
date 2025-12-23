from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, "pages_main/main_page.html")



def oge_subjects(request):
    data = {"exam": "ОГЭ", "edu": "10 класс", "exam_details": "основному государственному экзамену"}
    return render(request, "pages_main/exam_subjects_page.html", context=data)



def account(request):
    return render(request, "pages_main/account_page.html")



def ege_subjects(request):
    data = {"exam": "ЕГЭ", "edu": "институт", "exam_details": "единому государственному экзамену"}
    return render(request, "pages_main/exam_subjects_page.html", context=data)



def tst(request):
    return render(request, "pages_main/tst_page.html")




def book(request):
    return render(request, "pages_main/book_page.html")



