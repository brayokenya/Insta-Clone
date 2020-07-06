from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField




class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = CloudinaryField('profile_pic')
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return self.bio


class Post(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=144, blank=True, default="Post")
    caption = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(User)
    user_profile = models.ForeignKey(UserProfile)
   
    
    def __str__(self):
        return f"{self.name} - {self.caption}"

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save()

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.comment


