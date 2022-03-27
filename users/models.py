from django.db import models 
from django.views import View

class User(models.Model):
    user         = models.CharField(max_length=100)
    email        = models.CharField(max_length=100, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    etc_info     = models.CharField(max_length=300, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'