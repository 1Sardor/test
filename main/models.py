from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    birth = models.DateField()
    image = models.ImageField(upload_to='media/')
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name






