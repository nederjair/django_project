from django.db import models

# Create your models here.
class PageModel(models.Model):
    title = models.CharField(max_length=60, blank=True)
    permalink = models.CharField(max_length=12, unique=True, blank=True)
    update_date = models.DateTimeField('Last Updated', blank=True)
    body_text = models.TextField('Page Content', blank=True)
    def __str__(self):
        return self.title

