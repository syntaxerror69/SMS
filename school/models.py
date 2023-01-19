from django.db import models

# Create your models here.

CITY_CHOICE = (
    ('Purnea','Purnea'),
    ('Patna','Patna'),
    ('Kolkata','Kolkata'),
    ('Mumbai','Mumbai'),
    ('Ahmadabad','Ahmadabad'),
    ('Bengaluru','Bengaluru'),
)

class Students(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200, choices= CITY_CHOICE)
  

    def __str__(self):
        return self.name
       

