import uuid
from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100) 
    company = models.CharField(max_length=100, default='') 
    date_range = models.CharField(max_length=50, default='')
    description = models.TextField() 
    is_active = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.title} - {self.company}"

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=30)
    npm = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nama} - {self.npm}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20, default='')
    icon_class = models.CharField(max_length=50) 
    code_snippet = models.TextField()            

    def __str__(self):
        return self.name