from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    WORK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPES)

    def __str__(self):
        return f"{self.get_work_type_display()} - {self.link}"

class Artist(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name


