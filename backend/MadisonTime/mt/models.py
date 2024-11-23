from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
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