from django.db import models

# Create your models here.
class Outputs(models.Model):
    op=models.CharField(max_length=1000)