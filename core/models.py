from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete = models.CASCADE,
        related_name = 'profile'
    )
    region = models.CharField(max_length=1, choices=(
        ('B', 'Bishkek'),
        ('C', 'Chui'),
        ('N', 'Naryn'),
        ('O', 'Osh'),
    ))
    photo = models.ImageField(
        upload_to='profile_photo', null=True, blank=True
        )
    def __str__(self):
        return self.user.username
