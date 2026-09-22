import uuid
from django.contrib.auth.models import User
from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100) 
    company = models.CharField(max_length=100, default='') 
    date_range = models.CharField(max_length=50, default='')
    description = models.TextField() 
    is_active = models.BooleanField(default=False) 
    starred_by = models.ManyToManyField(
        User, related_name="starred_experiences", blank=True
    )

    def __str__(self):
        return f"{self.title} - {self.company}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_skills", blank=True
    )

    def __str__(self):
        return self.name