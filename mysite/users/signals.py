from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

# @receiver(post_save , sender=User)
# def build_profile(sender,created,instance,**kwargs):
#     if created:
#         Profile.objects.create(myname=instance.username,location="noida")
#         instance.profile.save()




