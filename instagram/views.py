from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, User, UserProfile, Comment
from .forms import UserForm, UserProfileForm, CommentForm, PostForm
from django.core.exceptions import ObjectDoesNotExist
from .filters import UserFilter


# Create your views here.
@login_required
def index(request):
    current_user = request.user
    print(current_user)
    current_profile = UserProfile.objects.get(user_id=current_user)
    posts = Post.objects.all()[::-1]
    comments = Comment.objects.all()

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)

            post.profile = current_user
            post.user_profile = current_profile

            post.save()
            post_form = PostForm()
            return HttpResponseRedirect(reverse("index"))

    else:
        post_form = PostForm()

    

    return render(request, "instagram/index.html", context={"posts":posts,
                                                           "current_user":current_user,
                                                           "current_profile":current_profile,
                                                           "post_form":post_form,
                                                           "comments":comments})

def post(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post__id=id)
    current_user = request.user
    current_profile = UserProfile.objects.get(id = current_user.id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            return redirect("post", post.id)

    else:
        comment_form = CommentForm()

    return render(request, "instagram/post.html", context={"post":post,
                                                          "current_user":current_user,
                                                          "current_profile":current_profile,
                                                          "comment_form":comment_form,
                                                          "comments":comments,})


def like(request, id):
    post = Post.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("index"))


def like_post(request, id):
    post = Post.objects.get(id = id)
    post.likes += 1
    post.save()
    return redirect("post", post.id)


@login_required
def search(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_user = UserProfile.search_by_user(search_term)
        message = f"{search_term}"
        user = User.objects.all()
        context = {
            "user":user,
            "message":message,
            "profile":searched_user
        }
        return render(request,'instagram/search_results.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagram/search_results.html',{"message":message})


    # if request.method == "GET":
    #     user_list = User.objects.all()
    #     user_filter = UserFilter(request.GET,queryset=user_list)

    #     context = {
    #         'filter':user_filter,
    #     }
    #     return render(request,'instagram/search_results.html',context)

    
    

@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = UserProfile.objects.get(user_id=user)
    posts = Post.objects.filter(profile__id=id)[::-1]
    return render(request, "instagram/profile.html", context={"user":user,
                                                             "profile":profile,
                                                             "posts":posts})

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("user_login")) #raise error/ flash

        else:
            return HttpResponseRedirect(reverse("user_login")) #raise error/ flash
    else:
        return render(request, "auth/login.html", context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))


def register(request):
    registered = False
    

    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = UserProfile()
            user_profile.user = user
            # user_profile.save()
            user_profile.save()
            registered = True
            

            return HttpResponseRedirect(reverse("user_login"))

        else:
            pass

    else:
        user_form = UserForm()
        

    return render(request, "auth/register.html", context={"user_form":user_form,
                                                          "registered":registered})


                                            
        