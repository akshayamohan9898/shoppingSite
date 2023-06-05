from django.db import models

# Create your models here.

class item(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    features=models.CharField(max_length=200)
    price=models.IntegerField()
    star=models.IntegerField(default=0)
    


    def __str__(self):
        return str(self.id)+":"+(self.name)
