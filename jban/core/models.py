from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractUser):
    preferred_class = models.CharField(max_length=16, default='swordman')
#
#
# class Skill(models.Model):
#     pass
#
#
# class Rune(models.Model):
#     pass


class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = ArrayField(base_field=models.IntegerField())
    default_class = models.CharField(default='swordman', max_length=16)
    runes = ArrayField(base_field=models.IntegerField())

