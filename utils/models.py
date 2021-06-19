import datetime
from django.db import models
from django.utils.timezone import make_aware

class AbstractAutoField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True