from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, unique=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    nick_name = models.CharField(max_length=16)
    email = models.EmailField(max_length=256, unique=True)
    mobile_no = models.CharField(null=True, max_length=14, unique=True)
    location = models.CharField(max_length=10)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    update_time = models.TimeField(null=True)