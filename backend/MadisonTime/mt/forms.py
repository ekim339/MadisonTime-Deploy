from django import forms
from .models import User, Post

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
