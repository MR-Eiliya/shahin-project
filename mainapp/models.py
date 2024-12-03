from django.db import models
from django.core.validators import MaxValueValidator


class Contact(models.Model):
    name = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255, blank=True)
    phone = models.CharField(max_length = 11, null=True)
    #email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-created_date"]
    
    
    def __str__(self):
        return self.name
    

class NewsLetter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email