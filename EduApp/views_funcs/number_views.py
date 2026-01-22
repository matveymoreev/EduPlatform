from encodings import undefined

from django.shortcuts import render, redirect

# модели
from EduApp.models import (User, Task_list_math, Task_list_russian, Task_list_informatics,
                            Task_list_physics, Task_list_biology, Task_list_chemistry,
                           Task_list_history, Task_list_social_studies, Task_list_literature,
                           Task_list_english, Task_list_geography)

def number(request):
    data = {
        "tasks": {
            "text": "На тарелке лежат одинаковые на вид пирожки: 4 с мясом, 8 с капустой и 3 с вишней. Петя наугад берёт один пирожок. Найдите вероятность того, что пирожок окажется с вишней.",
            "difficulty": "базовый",
            "object": "Арифметика",
            "Explanation": "Всего пирожков: 4 + 8 + 3 = 15. Пирожков с вишней: 3. Вероятность = 3/15 = 1/5 = 0.2",
            "done": 0,
            "right": 0,
            "Errors": 0,
        }
    }
    #
    # # математика
    # if request.path == "/OGE_russian/number/":
    #     objs = Task_list_math.objects.all()
    #
    # # русский
    # if request.path == "/OGE_russian/number/":


    return render(request, "pages_main/number_page.html")