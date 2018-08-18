"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#class UserProfile(models.Model):
#    user = models.OneToOneField(User)
#    description = models.CharField(max_length=300, default='')
#    image = models.ImageField(upload_to='profile_image', blank=True)
#
#    def _str_(self):
#        return self.user.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UserProfile.objects.create(User=kwargs['instance'])
#
#    post_save.connect(create_profile_profile, sender=User)

#@receiver(post_save, sender=User)
#def create_or_update_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#    instance.profile.save()