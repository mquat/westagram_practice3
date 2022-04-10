from django.db import models 

class User(models.Model):
    user         = models.CharField(max_length=100)
    email        = models.CharField(max_length=100, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likes'