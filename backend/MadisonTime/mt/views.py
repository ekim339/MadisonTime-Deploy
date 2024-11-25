from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView)
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.views import PasswordChangeView
from allauth.account.models import EmailAddress
from mt.models import Post, Comment, Course
from mt.forms import PostForm, CommentForm, CourseForm
from mt.functions import confirmation_required_redirect

# Create your views here.
def home(request):
  return render(request, 'mt/homepage.html')

def board(request):
  return render(request, 'mt/board.html')

@login_required
def timetable(request):
  if request.method == "POST":
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('timetable')
    else:
      render(request, 'mt/timetable.html', {'form':form})
  else:
    form = CourseForm()

  courses = Course.objects.filter(author=request.user)

  return render(request, 'mt/timetable.html', {'form':form, 'courses':courses})
  # return render(request, 'mt/timetable.html')

def delete_post(request, post_id):

  if not request.user.is_authenticated:
    raise PermissionDenied

  post = get_object_or_404(Post, id=post_id)

  if request.user != post.author:
    raise PermissionDenied

  post.delete()
  return redirect('home')

def delete_comment(request, comment_id):

  if not request.user.is_authenticated:
    raise PermissionDenied

  comment = get_object_or_404(Comment, id=comment_id)

  if request.user != comment.author:
    raise PermissionDenied
  
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

  # def test_func(self, user):
  #   return EmailAddress.objects.filter(user=user, verified=True).exists()
  
  def get_success_url(self):
    return reverse("post-detail", kwargs={"post_id":self.object.id})
  
  # FormMixin
  def get_context_data(self, **kwargs):
    context = super(PostDetailView, self).get_context_data(**kwargs)
    context['form'] = CommentForm(initial={'post':self.object})

    comment_id = self.request.GET.get("edit_comment")

    if comment_id:
      try:
        if not self.request.user.is_authenticated:
          raise PermissionDenied

        comment_to_edit = Comment.objects.get(id=comment_id, post=self.object)

        if self.request.user != comment_to_edit.author:
          raise PermissionDenied

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

    # access control for comments
    if not request.user.is_authenticated:
      return redirect(f"{reverse('account_login')}?next={self.request.path}")
    
    if not EmailAddress.objects.filter(user=request.user, verified=True).exists():
      return confirmation_required_redirect(request)

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
  
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Post
  form_class = PostForm
  template_name = "mt/post_form.html"

  # UserPassesTestMixin
  redirect_unauthenticated_users = True
  raise_exception = confirmation_required_redirect

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse("post-detail", kwargs={"post_id":self.object.id})
  
  def test_func(self, user):
    return EmailAddress.objects.filter(user=user, verified=True).exists()
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  form_class = PostForm
  template_name = "mt/post_form.html"
  pk_url_kwarg = 'post_id'

  raise_exception = True

  def get_success_url(self):
    return reverse("post-detail", kwargs={"post_id":self.object.id})
  
  def test_func(self, user):
    post = self.get_object()
    return post.author == user

class CustomPasswordChangeView(PasswordChangeView):
  def get_success_url(self):
    return reverse("home")