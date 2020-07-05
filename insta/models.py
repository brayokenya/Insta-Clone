from django.db import models
import datetime as dt

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    
    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()
    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Location(models.Model):
    loc = models.CharField(max_length =30)

    def __str__(self):
        return self.loc

class Category(models.Model):
    cat = models.CharField(max_length = 30)
    def __str__(self):
        return self.cat

class Update(models.Model):
    photo_image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length =60)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.caption

    @classmethod
    def todays_insta(cls):
        today = dt.date.today()
        insta = cls.objects.all()
        return insta

    @classmethod
    def days_insta(cls,date):
        insta = cls.objects.filter(pub_date__date = date)
        return insta
    
    @classmethod
    def search_by_category(cls,search_term):
        picture = cls.objects.filter(category__cat__icontains=search_term)
        return picture
        
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def filter_by_location(cls, location):
        image_location = Update.objects.filter(location__name=location).all()
        return image_location

    def __str__(self):
        return self.caption

    class Meta:
        ordering=["-pub_date"]  

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ["-pk"]


class Follow(models.Model):
    # follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    # followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'