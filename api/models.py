from django.db import models

# Create your models here.
class Task(models.Models):
    title=models.Charfield(max_lenght=200)
    completed=models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
