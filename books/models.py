from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractUser, UserManager)
import django.utils.timezone
from django.contrib.postgres.fields import ArrayField


# class MyUserManager(UserManager):
#     def create_user(self, email, name, password, alias=None):
#         user = self.model(email = self.normalize_email(email), name = name)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, name, password):
#         user = self.create_user(email, name, password)
#         user.is_staff()
#         user.is_superuser = True
#         user.save()
#         return user

# class User(AbstractUser):

#     class Meta:
#         db_table = 'users'

#     username = None
#     email = models.CharField(max_length=255, unique=True)
#     name = models.CharField(max_length=255, unique=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [email, name]

#     objects = MyUserManager()


class MyUserManager(UserManager):
    def create_user(self, email, name, password, **extra_fields):
        user = self.model(email = self.normalize_email(email), name = name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        user = self.create_user(email, name, password, **extra_fields)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user

class User(AbstractUser):

    class Meta:
        db_table = 'users'

    username = None
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=False)
    rated_books = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    first_name = models.CharField(blank=True, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    date_joined = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    groups = models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()




