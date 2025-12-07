from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, "main_page.html")

def exam_subjects(request):
    return render(request, "exam_subjects_page.html")



