from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(verbose_name = 'NickName', max_length=50, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True, help_text='ex) YYYY-MM-DD')
    aboutMe = models.TextField(blank=True, help_text='Introduce yourself', max_length=1000)
