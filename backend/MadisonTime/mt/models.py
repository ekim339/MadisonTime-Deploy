from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from colorfield.fields import ColorField
from .validators import (
  validate_no_special_characters, 
  validate_time_from, 
  validate_time_to
)

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
  author = models.ForeignKey(User, related_name='authored_posts', on_delete=models.CASCADE)
  content = models.TextField()
  image1 = models.ImageField(upload_to="post_pics", blank=True)
  image2 = models.ImageField(upload_to="post_pics", blank=True)
  image3 = models.ImageField(upload_to="post_pics", blank=True)
  dt_created = models.DateTimeField(auto_now_add=True)
  dt_updated = models.DateTimeField(auto_now=True)
  edited = models.BooleanField(default=False)
  likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
  dislikes = models.ManyToManyField(User, related_name="disliked_posts", blank=True)

  def __str__(self):
    return self.title

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
  
  def num_likes(self):
    return self.likes.count()
  
class Comment(models.Model):
  content = models.TextField()
  dt_created = models.DateTimeField(auto_now_add=True)
  dt_updated = models.DateTimeField(auto_now=True)
  edited = models.BooleanField(default=False)

  author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)
  dislikes = models.ManyToManyField(User, related_name="disliked_comments", blank=True)

  def __str__(self):
    return f"{self.author.username} on {self.post.title}"

  def save(self, *args, **kwargs):
    if self.pk:
      original = Comment.objects.get(pk=self.pk)
      if self.content != original.content:
        self.edited = True
        self.dt_updated = timezone.now()
    super().save(*args, **kwargs)

  def num_likes(self):
    return self.likes.count()
  
class Course(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=50, blank=True)
  time_from = models.TimeField(null=True, validators=[validate_time_from])
  time_to = models.TimeField(null=True, validators=[validate_time_to])
  color = ColorField(default="ff0000", null=True)
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
  
  def clean(self):
    super().clean()  # Call the parent class's clean method
    errors = {}
    
    if self.time_from >= self.time_to:
      if not (self.time_to.hour == 0 and self.time_to.minute == 0):
        errors["time_from"] = "Start time must be earlier than end time."
        # raise ValidationError({"time_from" : "Start time must be earlier than end time."})
      
    if not (self.mon or self.tue or self.wed or self.thu or self.fri or self.sat or self.sun):
        errors["mon"] = "At least one day must be selected."
        # raise ValidationError({"mon": "At least one day must be selected."})

    if errors:
      raise ValidationError(errors)

  author = models.ForeignKey(User, on_delete=models.CASCADE)
  
