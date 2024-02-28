from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     picture=models.ImageField(default="profilepic.jpg",upload_to="profile_pictures")
#     location=models.CharField(max_length=50)
    
#     def __str__(self):

#         return self.user.username


class Info(models.Model):
    raj=models.OneToOneField(User, on_delete=models.CASCADE)
    place=models.CharField(max_length=100)
    img=models.ImageField(default="imgpic.jpg",upload_to="display_pictures")
    gender=models.CharField(max_length=20,default="Male")

    def __str__(self):
        return self.raj.username