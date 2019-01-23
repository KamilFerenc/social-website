from django.db import models
from django.conf import settings


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True,
                                     help_text='Use format "2000-01-31"')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile user {}.'.format(self.user.username)
