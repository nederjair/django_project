from django.db import models

# Create your models here.
class AppModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    num1 = models.IntegerField()
    num2 = models.IntegerField()

    def __str__(self):
        return str(self.name)