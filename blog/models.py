from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
     
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/deafult.jpg')
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    login_required = models.BooleanField(default = False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-created_date"]
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    
    def __str__(self):
        return self.name