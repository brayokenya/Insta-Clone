from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^profile/(\d+)", views.profile, name="profile"),
    url(r"^like/(\d+)", views.like, name="like"),
    url(r"^like-post/(\d+)", views.like_post, name="like_post"),
    url(r"^post/(\d+)", views.post, name="post"),
    url(r"^search/", views.search, name="search"),
]