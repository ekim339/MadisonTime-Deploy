from django import forms
from .models import User, Post, Comment, Course
from colorfield.fields import ColorWidget

class SignupForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["nickname"]

  def signup(self, request, user):
    user.nickname = self.cleaned_data["nickname"]
    user.save()

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = [
      'title',
      'content',
      'image1',
      'image2',
      'image3'
    ]
    widgets = {
      'content': forms.Textarea(attrs={"rows":7, "cols":10}),
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = [
      'content'
    ]
    widgets = {
      'content': forms.Textarea(attrs={"rows":3, "cols":10}),
    }

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = [
      'name',
      'location',
      'time_from',
      'time_to',
      'color',
      'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun',
    ]
    widgets = {
      'time_from': forms.TimeInput(attrs={"type":"time"}),
      'time_to':forms.TimeInput(attrs={"type":"time"}),
      'color' : ColorWidget()
    }