from django.db import models

class Mixin(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    created = models.DateField(auto_now=True)
    