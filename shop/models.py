from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, default= '')
    last_name = models.CharField(max_length=100, default= '')
    address_line = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=2, default='')
    zip_code = models.IntegerField(default=0)
    email_address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:  # If User object has been created
            # create a userprofile from the current user instance. Pass in User object to the create function
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    # connect to the post_save signal .connect(function, sender)
    post_save.connect(create_profile, sender=User)
