from django.db import models

# Create your models here.
class myModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    quote_text = models.TextField(max_length=100)
    category = models.CharField(max_length=100)
    additional_details = models.TextField(max_length=100)