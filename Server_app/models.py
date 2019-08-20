from django.db import models

class Student_Data(models.Model):
    S_Name = models.CharField(max_length=50)
    S_Roll = models.IntegerField()
    S_Class = models.IntegerField()
    S_Location = models.CharField(max_length=50)