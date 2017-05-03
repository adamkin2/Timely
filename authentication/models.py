# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core import validators
# from django.utils import timezone
#
# class User(AbstractUser):
#     identifier = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'identifier'
#     EMAIL_FIELD = 'identifier'
#
#     def get_full_name(self):
#         return '%s %s' % (self.first_name, self.last_name)
#
#     def get_short_name(self):
#         return self.first_name

