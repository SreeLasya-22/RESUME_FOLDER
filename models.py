from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.TextField()
    languages = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    experience = models.TextField()
    acknowledgment = models.TextField()
    hobbies = models.TextField()

    def __str__(self):
        return self.name


