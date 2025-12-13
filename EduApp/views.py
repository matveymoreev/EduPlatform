from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, "pages_main/main_page.html")

def exam_subjects(request):
    return render(request, "pages_main/exam_subjects_page.html")

def account(request):
    return render(request, "pages_main/account_page.html")



