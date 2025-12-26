from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    class_id = models.CharField(max_length=2)
    about = models.CharField(max_length=300)
    birth_date= models.DateField()
    course_cnt = models.IntegerField()
    hours = models.IntegerField()
    progress = models.IntegerField()
    activity = models.IntegerField()




class Task(models.Model):
    description = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    number = models.IntegerField()
    # number_of_hours = models.IntegerField()
    answers = models.CharField(max_length=300)
    goodAnswers = models.IntegerField()
    badAnswers = models.IntegerField()



'''
#описание, заголовок, номер, количество решений, ответ
    def __init__(self, description, title, number, number_of_solutions, answer):
        self.description = description
        self.title = title
        self.number = number
        self.number_of_solutions = number_of_solutions
        self.answer = answer'''



