from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    class_id = models.IntegerField()
    about = models.CharField(max_length=300)
    birth_date = models.DateField()
    course_cnt = models.IntegerField()
    hours = models.IntegerField()
    progress = models.IntegerField()
    activity = models.IntegerField()





class Task(models.Model):
    topic = models.CharField(max_length=300, default="")
    task_topic = models.CharField(max_length=300, default="")
    task = models.CharField(max_length=300, default="")
    example = models.CharField(max_length=300, default="")
    task_type = models.CharField(max_length=300, default="")
    difficulty = models.CharField(max_length=300, default="")
    mark = models.IntegerField()
    subject = models.CharField(max_length=300, default="")





