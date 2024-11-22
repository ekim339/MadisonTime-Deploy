from django.shortcuts import render
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView,
  DeleteView)
from django.urls import reverse
from mt.models import Post
from mt.forms import PostForm

# Create your views here.
def home(request):
  return render(request, 'mt/homepage.html')

def board(request):
  return render(request, 'mt/board.html')

def timetable(request):
  return render(request, 'mt/timetable.html')

class HomepageView(ListView):
  model = Post
  template_name = "mt/homepage.html"
  context_object_name = "posts"
  paginate_by = 4
  ordering = ["-dt_created"]

class PostDetailView(DetailView):
  model = Post
  template_name = "mt/post_detail.html"
  pk_url_kwarg = "post_id"

class PostCreateView(CreateView):
  model = Post
  form_class = PostForm
  template_name = "mt/post_form.html"

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse("post-detail", kwargs={"post_id":self.object.id})
  
class PostUpdateView(UpdateView):
  model = Post
  form_class = PostForm
  template_name = "mt/post_form.html"
  pk_url_kwarg = 'post_id'

  def get_success_url(self):
    return reverse("post-detail", kwargs={"post_id":self.object.id})

class PostDeleteView(DeleteView):
  model = Post
  template_name = "mt/post_confirm_delete.html"
  pk_url_kwarg = 'post_id'

  def get_success_url(self):
    return reverse("home")