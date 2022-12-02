from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

class Stock(models.Model):
    barcode=models.CharField(max_length=13,primary_key=True)
    name=models.CharField(max_length=100)
    cost=models.FloatField(round(2))
    retail=models.FloatField(round(2))

    def __str__(self):
        return self.barcode,self.name,self.cost,self.retail
        
    
      
