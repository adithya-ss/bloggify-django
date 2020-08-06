from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    #Define the variables or fields for individual blog posts.
    blog_title = models.CharField(max_length=255)
    blog_page_header = models.CharField(max_length=255)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_body = RichTextField(blank=True, null=True)
    # blog_body = models.TextField()
    blog_pub_date = models.DateField(auto_now_add=True)
    blog_category = models.CharField(max_length=255, default="Popular Quotes")
    blog_image = models.ImageField(null=True, blank=True, upload_to="image_dir/")

    #Blog post entries on the admin page.
    def __str__(self):
        return self.blog_title + ' || By: ' + str(self.blog_author)

    def get_absolute_url(self):
        # return reverse('blog_detail', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    comment_body = models.TextField()
    commented_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.blog_title, self.user_name)