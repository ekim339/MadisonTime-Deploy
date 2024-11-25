from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from colorfield.fields import ColorField
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
  edited = models.BooleanField(default=False)

  def save(self, *args, **kwargs):
    if self.pk:
      original = Post.objects.get(pk=self.pk)
      if (self.title != original.title or 
        self.content != original.content or 
        self.image1 != original.image1 or
        self.image2 != original.image2 or
        self.image3 != original.image3):
        self.edited = True
        self.dt_updated = timezone.now()
    super().save(*args, **kwargs)

  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
class Comment(models.Model):
  content = models.TextField()
  dt_created = models.DateTimeField(auto_now_add=True)
  dt_updated = models.DateTimeField(auto_now=True)
  edited = models.BooleanField(default=False)

  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

  def save(self, *args, **kwargs):
    if self.pk:
      original = Comment.objects.get(pk=self.pk)
      if self.content != original.content:
        self.edited = True
        self.dt_updated = timezone.now()
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.author.username} on {self.post.title}"
  
class Course(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=50, blank=True)
  time_from = models.TimeField()
  time_to = models.TimeField()
  color = ColorField(default="ff0000")
  mon = models.BooleanField(default=False)
  tue = models.BooleanField(default=False)
  wed = models.BooleanField(default=False)
  thu = models.BooleanField(default=False)
  fri = models.BooleanField(default=False)
  sat = models.BooleanField(default=False)
  sun = models.BooleanField(default=False)

  def __str__(self):
    return self.name
  
  def get_days(self):
    days = []
    if self.mon:
      days.append("mon")
    if self.tue:
      days.append("tue")
    if self.wed:
      days.append("wed")
    if self.thu:
      days.append("thu")
    if self.fri:
      days.append("fri")
    if self.sat:
      days.append("sat")
    if self.sun:
      days.append("sun")
    return days
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  
