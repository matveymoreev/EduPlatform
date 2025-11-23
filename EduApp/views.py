from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("asdasdasda")

def home2(request):
    return HttpResponse("123123")

def lol(request):
    return HttpResponse("asda")

