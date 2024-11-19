from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

# Create your models here.
class User(AbstractUser):
  nickname = models.CharField(
    max_length=20, 
    unique=True, 
    null=True, 
    validators=[validate_no_special_characters],
    error_messages = {"unique" : "This username is already taken."},
  )

  def __str__(self):
    return self.email
  
class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  image1 = models.ImageField(upload_to="post_pics", blank=True)
  image2 = models.ImageField(upload_to="post_pics", blank=True)
  image3 = models.ImageField(upload_to="post_pics", blank=True)
  dt_created = models.DateTimeField(auto_now_add=True)
  dt_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title