"""
URL configuration for EduPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from EduApp.views_funcs import subject_views
from EduApp.views_funcs import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.main),
    path("OGE_subjects/", views.oge_subjects),
    path("acc/", views.acc),
    path("EGE_subjects/", views.ege_subjects),
    re_path(r"^books", views.books),
    path("tst/", subject_views.tst),
    path("number/", views.number),



    path("OGE_math/", subject_views.tst),
    path("EGE_math/", subject_views.tst),
    path("OGE_russian/", subject_views.tst),
    path("EGE_russian/", subject_views.tst),
    path("OGE_informatics/", subject_views.tst),
    path("EGE_informatics/", subject_views.tst),
    path("OGE_physics/", subject_views.tst),
    path("EGE_physics/", subject_views.tst),
    path("OGE_biology/", subject_views.tst),
    path("EGE_biology/", subject_views.tst),
    path("OGE_chemistry/", subject_views.tst),
    path("EGE_chemistry/", subject_views.tst),
    path("OGE_history/", subject_views.tst),
    path("EGE_history/", subject_views.tst),
    path("OGE_social_studies/", subject_views.tst),
    path("EGE_social_studies/", subject_views.tst),
    path("OGE_literature/", subject_views.tst),
    path("EGE_literature/", subject_views.tst),
    path("OGE_english/", subject_views.tst),
    path("EGE_english/", subject_views.tst),
    path("OGE_geography/", subject_views.tst),
    path("EGE_geography/", subject_views.tst),


    #ссылки регистрации
    path('login/', views.login_page),
    path('accounts/login/', views.login_page),
    path('logout/', views.logout_page),
    path('reg/', views.auth_page),


]
