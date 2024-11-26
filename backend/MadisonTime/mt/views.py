from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView)
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import PermissionDenied, ValidationError
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.views import PasswordChangeView
from allauth.account.models import EmailAddress
from allauth.account.forms import ChangePasswordForm
from mt.models import User, Post, Comment, Course
from mt.forms import PostForm, CommentForm, CourseForm, NicknameChangeForm
from mt.functions import confirmation_required_redirect, calculateDuration, calculatePosition

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
      course = form.save(commit=False)  # Don't save to the database yet
      course.author = request.user      # Set the author field

      # get days input
      mon = request.POST.get("mon") == "True"
      tue = request.POST.get("tue") == "True"
      wed = request.POST.get("wed") == "True"
      thu = request.POST.get("thu") == "True"
      fri = request.POST.get("fri") == "True"
      sat = request.POST.get("sat") == "True"
      sun = request.POST.get("sun") == "True"

      # update model field
      form.mon = mon
      form.tue = tue
      form.wed = wed
      form.thu = thu
      form.fri = fri
      form.sat = sat
      form.sun = sun

      try:
          course.full_clean()  # Trigger the model's clean() method
          course.save()
          return redirect('timetable')
      except ValidationError as e:
          # Pass the error message to the template
          return render(request, 'mt/timetable.html', {
              'form': form,
              'modla_optn':True,
              'error_message': e.message_dict  # Pass error messages as a dictionary
          })

      # course.save()
      # return redirect('timetable')
    else:
      render(request, 'mt/timetable.html', {'form':form, "modal_open":True})
  else:
    form = CourseForm()

  courses = Course.objects.filter(author=request.user)
  for course in courses:
    duration = calculateDuration(course.time_from, course.time_to)
    time_from_start = calculatePosition(course.time_from)
    course.height = duration * 5.5555
    course.position = time_from_start * 5.5555

  return render(request, 'mt/timetable.html', {'form':form, 'courses':courses})
  # return render(request, 'mt/timetable.html')

@login_required
def settings(request):
    # get nickname of user before getting form
    curr_nickname = request.user.nickname

    if request.method == "POST":
      password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
      if password_change_form.is_valid():
        password_change_form.save()
        update_session_auth_hash(request, password_change_form.user) # Keep the user logged in
        return redirect('settings')
      else:
        nickname_change_form = NicknameChangeForm(request.POST, instance=request.user)
        if nickname_change_form.is_valid():
          nickname_change_form.save()
          return redirect('settings')
        else:
          return render(request, 'mt/settings.html', 
          {
          'password_change_form': password_change_form, 
          'nickname_change_form':nickname_change_form, 
          'curr_nickname': curr_nickname
          })
    else:
      password_change_form = PasswordChangeForm(user=request.user)
      nickname_change_form = NicknameChangeForm(request.POST, instance=request.user)

    return render(request, 'mt/settings.html', 
      {
      'password_change_form': password_change_form, 
      'nickname_change_form':nickname_change_form, 
      'curr_nickname': curr_nickname
      })

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

class BoardView(ListView):
  model = Post
  template_name = "mt/board.html"
  context_object_name = "posts"
  paginate_by = 10
  ordering = ["-dt_created"]


# @login_required
# def custom_password_change(request):
#     # Initialize forms with no data for initial GET request
#     password_change_form = PasswordChangeForm(user=request.user)
#     nickname_change_form = NicknameChangeForm(instance=request.user)

#     if request.method == 'POST':
#         form_type = request.POST.get('form_type')

#         if form_type == 'password_change':
#             # Process the password change form
#             password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
#             if password_change_form.is_valid():
#                 password_change_form.save()
#                 update_session_auth_hash(request, password_change_form.user)
#                 messages.success(request, "Your password was successfully changed.")
#                 return redirect('settings')
#         elif form_type == 'nickname_change':
#             # Process the nickname change form
#             nickname_change_form = NicknameChangeForm(instance=request.user, data=request.POST)
#             if nickname_change_form.is_valid():
#                 nickname_change_form.save()
#                 messages.success(request, "Your nickname was successfully updated.")
#                 return redirect('settings')
            
#     email = request.user.email
#     nickname = request.user.nickname

#     return render(request, 'mt/settings.html', {
#         'password_change_form': password_change_form,
#         'nickname_change_form': nickname_change_form,
#         'email':email, 
#         'nickname':nickname
#     })
