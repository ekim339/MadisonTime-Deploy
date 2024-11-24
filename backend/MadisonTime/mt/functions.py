from django.shortcuts import redirect, reverse
from allauth.account.utils import send_email_confirmation

# def confirmation_required_redirect(self, request):
#   # send email to user who haven't confirmed their email
#   send_email_confirmation(request, request.user)
#   return redirect("account_email_confirmation_required")

# def confirmation_required_redirect_for_comment(request):
#   # send email to user who haven't confirmed their email
#   send_email_confirmation(request, request.user)
#   return redirect("account_email_confirmation_required")

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