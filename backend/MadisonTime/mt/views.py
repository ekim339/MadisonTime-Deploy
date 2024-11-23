from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView,
  DeleteView)
from django.views.generic.edit import FormMixin
from django.urls import reverse
from mt.models import Post, Comment
from mt.forms import PostForm, CommentForm


# Create your views here.
def home(request):
  return render(request, 'mt/homepage.html')

def board(request):
  return render(request, 'mt/board.html')

def timetable(request):
  return render(request, 'mt/timetable.html')

def delete_post(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  post.delete()
  return redirect('home')

def delete_comment(request, comment_id):
  comment = get_object_or_404(Comment, id=comment_id)
  post_id = comment.post.id
  comment.delete()
  return redirect('post-detail', post_id=post_id)

class HomepageView(ListView):
  model = Post
  template_name = "mt/homepage.html"
  context_object_name = "posts"
  paginate_by = 4
  ordering = ["-dt_created"]

class PostDetailView(FormMixin, DetailView):
  model = Post
  pk_url_kwarg = "post_id"
  form_class = CommentForm
  template_name = "mt/post_detail.html"

  def get_success_url(self):
    return reverse("post-detail", kwargs={"post_id":self.object.id})
  
  def get_context_data(self, **kwargs):
    context = super(PostDetailView, self).get_context_data(**kwargs)
    context['form'] = CommentForm(initial={'post':self.object})

    comment_id = self.request.GET.get("edit_comment")

    if comment_id:
      try:
        comment_to_edit = Comment.objects.get(id=comment_id, post=self.object)
        context['edit_form'] = CommentForm(instance=comment_to_edit)
        context['edit_comment'] = comment_to_edit
      except Comment.DoesNotExist:
        context['edit_form'] = None
        context['edit_comment'] = None
    else:
      context['edit_form'] = None
      context['edit_comment'] = None

    return context

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()

    # view identifies the request as an edit request
    if 'edit_comment_id' in request.POST:
      comment_id = request.POST['edit_comment_id']
      comment_to_edit = Comment.objects.get(id=comment_id, post=self.object)
      form = CommentForm(request.POST, instance=comment_to_edit)
    else:
      form = self.get_form();

    if form.is_valid():
      return self.form_valid(form)
    else:
      return self.form_invalid(form)
    
  def form_valid(self, form):
    if not form.instance.pk:
      form.instance.author = self.request.user
      form.instance.post = self.get_object()
    form.save()
    return super(PostDetailView, self).form_valid(form)

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
