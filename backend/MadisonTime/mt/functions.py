from django.shortcuts import redirect, reverse
from allauth.account.utils import send_email_confirmation
from .models import Course

def confirmation_required_redirect(*args, **kwargs):
  if len(args) == 2:
    self, request = args
  elif len(args) == 1:
    request = args[0]
  else:
    raise ValueError("Invalid arguments")
  
  # send email to user who haven't confirmed their email
  send_email_confirmation(request, request.user)
  return redirect("account_email_confirmation_required")

def calculateDuration(time_from, time_to):
  time_from_hrs = time_from.hour + time_from.minute / 60
  time_to_hrs = time_to.hour + time_to.minute / 60
  if time_to_hrs == 0:
    duration = 24 - time_from_hrs
  else:
    duration = time_to_hrs - time_from_hrs
  return duration

def calculatePosition(time_from):
  time_from_start = (time_from.hour - 6) + time_from.minute / 60
  return time_from_start

def get_courses_with_dimensions(user):
    # Annotate courses with height and position based on their time
    courses = Course.objects.filter(author=user)
    for course in courses:
        duration = calculateDuration(course.time_from, course.time_to)
        time_from_start = calculatePosition(course.time_from)
        course.height = duration * 5.555555  # Scale factor for display
        course.position = time_from_start * 5.555555  # Scale factor for display
    return courses