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



def tst(request):
    data_task = {
        "topic": "Действия с десятичными дробями",
        "task_topic": "Задание на выполнение арифметических действий с десятичными дробями: сложение, вычитание, умножение и деление. Особое внимание уделяется правильной расстановке запятой при умножении и делении десятичных дробей.",
        "task": "Вычислите:",
        "example": "3,25 × 0,4",
        "task_type": "Краткий ответ (десятичная дробь)",
        "difficulty": "базовый",
        "mark": 1,
        "subject": "Алгебра",
        "exam": "ОГЕ",
    }

    data_title = {
        "object": "математика",
        "object2": "математике",
        "numders": 0,
        "title": """ОГЭ по математике — обязательный экзамен для всех выпускников 9 классов. Он проверяет базовые математические знания и умения, необходимые для повседневной жизни и продолжения образования. Результаты экзамена учитываются при поступлении в профильные 10-11 классы и колледжи.
                    назови этот абзац 1 словом""",
        "time_minutes": 235,
        "time_hours": "3 часа 55 минут",
        "test_count": 25,
        "write_task_count": "19 базовых, 6 повышенной сложности",
        "max_scores": 31,
        "details": "8 за алгебру, 7 за геометрию, 16 за реальную математику",
    }

    #русский
    if request.path == "/OGE_russian/":
        data_title["object"] = "русский"
        data_title["object2"] = "русскому"
        data_title["test_count"] = 19
        data_title["write_task_count"] = "5 заданий-работа с текстом, 9-база 7-9 класс, 5-работа с сочинением"
        data_title["max_scores"] = 37
        data_title["details"] = "первая часть-6 баллов, вторая часть-11 баллов, третья часть-7"
        data_title["title"] = "ОГЭ по русскому языку — обязательный экзамен для всех выпускников 9 классов. Он проверяет владение нормами языка, умение создавать письменные высказывания и понимать прочитанный текст. Результаты экзамена являются ключевым критерием для получения аттестата и необходимы для поступления в любые учреждения среднего профессионального образования."
        data_title["numders"] = 19

    #информатика
    if request.path == "/OGE_informatics/":
        data_title["object"] = "информатика"
        data_title["object2"] = "информатике"
        data_title["time_minutes"] = "150 минут"
        data_title["time_hours"] = "2 часа 30 минут"
        data_title["test_count"] = 16
        data_title["write_task_count"] = "10 базовых, 6 повышенных"
        data_title["max_scores"] = 21
        data_title["details"] = "первая часть-12 баллов, вторая часть-9 баллов"
        data_title["title"] = "ОГЭ по информатике — экзамен по выбору для выпускников 9 классов. Он проверяет понимание основ информационных процессов, алгоритмического мышления, знание устройства компьютера и умение решать практические задачи, в том числе с написанием простых программ. Результаты экзамена необходимы для поступления в ИТ-профильные классы, колледжи в сфере программирования и информационных технологий."
        data_title["numders"] = 16

    #общество
    if request.path == "/OGE_social_science/":
        data_title["object"] = "обществознание"
        data_title["object2"] = "обществознанию"
        data_title["test_count"] = 24
        data_title["write_task_count"] = "6 заданий с развернутым ответом, в т.ч. мини-сочинение"
        data_title["max_scores"] = 35
        data_title["details"] = "часть 1 - 26 баллов, часть 2 - 9 баллов"
        data_title[
            "title"] = "ОГЭ по обществознанию — один из самых популярных экзаменов по выбору у выпускников 9 классов. Он проверяет знания о человеке и обществе, сферах социальной жизни, основах права, политики и экономики. Результаты экзамена важны для поступления в социально-гуманитарные, правовые или экономические профильные классы и колледжи."
        data_title["numders"] = 24

    #география
    if request.path == "/OGE_geography/":
        data_title["object"] = "география"
        data_title["object2"] = "географии"
        data_title["test_count"] = 30
        data_title[
            "write_task_count"] = "3 задания с развернутым ответом (анализ данных, решение географической задачи)"
        data_title["max_scores"] = 31
        data_title["details"] = "часть 1 - 27 баллов, часть 2 - 4 балла"
        data_title[
            "title"] = "ОГЭ по географии — экзамен по выбору для выпускников 9 классов. Он оценивает знание географических объектов, закономерностей природы, населения и хозяйства мира и России, а также умение работать с картами и статистическими данными. Результаты экзамена учитываются при поступлении в профильные классы географического, экономического или экологического направления, а также в соответствующие колледжи."
        data_title["numders"] = 30

    #биология
    if request.path == "/OGE_biology/":
        data_title["object"] = "биология"
        data_title["object2"] = "биологии"
        data_title["test_count"] = 28
        data_title[
            "write_task_count"] = "4 задания с развернутым ответом (работа с текстом, анализ опыта, решение задачи)"
        data_title["max_scores"] = 45
        data_title["details"] = "часть 1 - 35 баллов, часть 2 - 10 баллов"
        data_title[
            "title"] = "ОГЭ по биологии — экзамен по выбору для выпускников 9 классов. Он оценивает знания о живой природе, строении и процессах жизнедеятельности организмов, экологических взаимосвязях. Результаты экзамена важны для поступления в профильные классы естественно-научного направления, медицинские, аграрные или педагогические колледжи."
        data_title["numders"] = 28

    #физика
    if request.path == "/OGE_physics/":
        data_title["object"] = "физика"
        data_title["object2"] = "физике"
        data_title["test_count"] = 25
        data_title[
            "write_task_count"] = "6 заданий с развернутым ответом (качественная задача, расчетные задачи, анализ экспериментов)"
        data_title["max_scores"] = 43
        data_title["details"] = "часть 1 - 31 балл, часть 2 - 12 баллов"
        data_title[
            "title"] = "ОГЭ по физике — экзамен по выбору для выпускников 9 классов. Он проверяет понимание физических законов и явлений, умение решать расчётные и экспериментальные задачи, объяснять процессы в природе и технике. Результаты экзамена являются важным критерием для поступления в физико-математические или инженерно-технические профильные классы, а также в техникумы и колледжи соответствующего профиля."
        data_title["numders"] = 25

    #история
    if request.path == "/OGE_history/":
        data_title["object"] = "история"
        data_title["object2"] = "истории"
        data_title["test_count"] = 24
        data_title[
            "write_task_count"] = "7 заданий с развернутым ответом (анализ исторического источника, личности, события)"
        data_title["max_scores"] = 37
        data_title["details"] = "часть 1 - 30 баллов, часть 2 - 7 баллов"
        data_title[
            "title"] = "ОГЭ по истории — экзамен по выбору для выпускников 9 классов. Он оценивает знание ключевых событий, процессов и личностей отечественной и всеобщей истории, умение анализировать исторические источники и работать с хронологией. Результаты экзамена необходимы для зачисления в историко-правовые, гуманитарные или культурологические профильные классы и колледжи."
        data_title["numders"] = 24

    #химия
    if request.path == "/OGE_chemistry/":
        data_title["object"] = "химия"
        data_title["object2"] = "химии"
        data_title["test_count"] = 24
        data_title["write_task_count"] = "5 заданий с развернутым ответом (расчетные задачи, анализ эксперимента)"
        data_title["max_scores"] = 40
        data_title["details"] = "часть 1 - 28 баллов, часть 2 - 12 баллов (с реальным экспериментом +5 баллов)"
        data_title[
            "title"] = "ОГЭ по химии — экзамен по выбору для выпускников 9 классов. Он оценивает знание основных химических понятий, законов, классов веществ, умение составлять уравнения реакций и решать расчётные задачи. Результаты экзамена учитываются при поступлении в химико-биологические, медицинские или инженерные профильные классы, а также в колледжи химического, фармацевтического или медицинского направления."
        data_title["numders"] = 24

    #англ
    if request.path == "/OGE_english/":
        data_title["object"] = "английский"
        data_title["object2"] = "английскому"
        data_title["test_count"] = 36
        data_title["write_task_count"] = "Письмо (задание 35) и устная часть (задания 2-4 в говорении)"
        data_title["max_scores"] = 68
        data_title["details"] = "аудирование - 14, чтение - 14, грамматика - 10, письмо - 10, говорение - 20"
        data_title[
            "title"] = "ОГЭ по английскому языку — экзамен по выбору для выпускников 9 классов. Он оценивает уровень практического владения языком через аудирование, чтение, грамматику, письмо и устную речь (говорение). Результаты экзамена важны для поступления в лингвистические профильные классы, колледжи с языковым уклоном или международными программами."
        data_title["numders"] = 36

    #литература
    if request.path == "/OGE_literature/":
        data_title["object"] = "литература"
        data_title["object2"] = "литературе"
        data_title["test_count"] = "2 комплекта (на выбор)"
        data_title["write_task_count"] = "4 развернутых ответа (анализ фрагмента, сравнение, сочинение)"
        data_title["max_scores"] = 39
        data_title["details"] = "часть 1 - 26 баллов, часть 2 - 13 баллов"
        data_title[
            "title"] = "ОГЭ по литературе — экзамен по выбору для выпускников 9 классов. Он проверяет знание литературных произведений, умение анализировать текст, понимать авторский замысел и формулировать собственные развернутые суждения. Результаты экзамена учитываются при зачислении в гуманитарные или филологические профильные классы и колледжи."
        data_title["numders"] = "2 комплекта"


    return render(request, "pages_main/tst_page.html", context=data_title)

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
        reg_data["age"] = int(request.POST.get("age", -1))
        reg_data["check_terms"] = request.POST.get("check_terms", "undefined")
        reg_data["user_class"] = request.POST.get("user_class", "undefined")

        if (len(User.objects.filter(email=reg_data["email"])) or len(DefUser.objects.filter(email=reg_data["email"]))):
            context["errors"] = "Логин: Пользователь с таким логином уже существует!"
            return render(request, "pages_main/auth_page.html", context=context)
        if (reg_data["age"] > 100):
            context["errors"] = "Дата рождения: Ошибка даты рождения!"
            return render(request, "pages_main/auth_page.html", context=context)
        if (reg_data["password"] != reg_data["password_repeat"]):
            context["errors"] = "Пароль: Ошибка при повторении пороля!"
            return render(request, "pages_main/auth_page.html", context=context)


        # добавляем пользователя в нашу таблицу в БД
        user = User.objects.create(name=reg_data["name"], age=reg_data["age"], surname=reg_data["surname"], email=reg_data["email"], password=reg_data["password"],
                                   class_id=0, about="",  birth_date="2003-12-12", course_cnt=0, hours=0, progress=0, activity=0)
        # добавляем пользователя в стандартную таблицу зарегистрированных пользователей
        usr = DefUser.objects.create_user(reg_data["email"], reg_data["email"], reg_data["password"], first_name=reg_data["name"], last_name=reg_data["surname"])
        login(request, usr)
        # если успешно вошли, меняем кнопки регистрации и войти на кнопку аккаунта
        context["logIn"] = True
        return redirect("/")

    return render(request, "pages_main/auth_page.html", context=context)







