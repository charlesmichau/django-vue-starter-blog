from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# Create your models here.

# General information for the entire website


class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = '1. Site'

    def __str__(self):
        return self.name


# New user model
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatars/%Y/%m/%d/',
        default='users/avatars/default.jpg', blank=True
    )
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = '2. Users'

    def __str__(self):
        return self.username


# Category model
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = '3. Categories'

    def __str__(self):
        return self.name


# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = '4. Tags'

    def __str__(self):
        return self.name


# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = RichTextField()
    featured_image = models.ImageField(
        upload_to='posts/featured_images/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    # Each post can receive likes from multiple users, and each user can like multiple posts
    likes = models.ManyToManyField(
        User, related_name='post_like', default=None, blank=True)

    # Each post belong to one user and one category.
    # Each post has many tags, and each tag has many posts.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, default=None)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = '5. Posts'

    def __str__(self):
        return self.title

    def get_number_of_likes(self):
        return self.likes.count()


# Comment model
class Comment(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    # Each post can receive likes from multiple users, and each user can like multiple posts
    likes = models.ManyToManyField(User, related_name='comment_like')

    # Each comment belongs to one user and one post
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = '6. Comments'

    def __str__(self):
        if len(self.content) > 50:
            comment = self.content[:50] + '...'
        else:
            comment = self.content
        return comment

    def get_number_of_likes(self):
        return self.likes.count()


class Highlight(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    property1 = models.CharField(max_length=100, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
