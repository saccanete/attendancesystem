from django.db import models
from datetime import datetime

class eventList(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    event = models.CharField(max_length=200)
    time = models.DateTimeField(null=True,blank=True)
    
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.lastname,self.firstname,self.level,self.course,self.gender,self.event,self.time