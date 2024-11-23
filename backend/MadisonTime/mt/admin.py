from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Comment

# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields" : ("nickname",)}),)

admin.site.register(Post)
admin.site.register(Comment)

# super user: ekim339, ekim339@wisc.edu, madisontime
# user 1: testuser, test@gmail.com, testingsignup
# user 1: test2@gmail.com, testuser2, testingsignup
# user 3: test3@gmail.com, testuser3, Testingsignup^^00