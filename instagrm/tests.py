from django.test import TestCase
from .models import Post, UserProfile, User, Comment

# Create your tests here.
class PostTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name="brian", last_name="kiiru",
                         username="briankiiru", email="kiirubrian21@gmail.com",)
        self.user.save()
        self.profile = UserProfile(user=self.user, bio="None",
                                   followers=0, following=0,)
        self.profile.save()
        self.test_post = Post(name="Post", caption="test caption", 
                              profile = self.user, user_profile=self.profile)
        self.test_post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_post, Post))

class UserTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name="brian", last_name="kiiru",
                         username="briankiiru", email="brian@gmail.com",)

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

class UserProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name="brian", last_name="kiiru",
                         username="briankiiru", email="brian@gmail.com",)
        self.user.save()
        self.profile = UserProfile(user=self.user, bio="None",
                                   followers=0, following=0,)
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))