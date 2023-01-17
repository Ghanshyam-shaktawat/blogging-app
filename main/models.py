from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, date
from tinymce.models import HTMLField

from django.conf import settings
User = settings.AUTH_USER_MODEL

STATUS_CHOICES = [
    ('d', 'draft'),
    ('p', 'published'),
    ('t', 'takendown')
]

class Category(models.Model):
    """Making category for blogs"""
    cate = models.CharField("Post's Category", max_length=125, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.cate
    
    def save(self, *args, **kwargs):
        self.cate = self.cate.lower()
        return super(Category, self).save(*args, **kwargs)
    
    
class Post(models.Model):
    """Storing the blog title with date published"""
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    snippets = models.CharField(max_length=200)
    body= HTMLField()
    slug = models.SlugField(max_length=80, unique=True, null=False, help_text="This field take uer input")
    image= models.ImageField('Image', upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=125, related_name='posts')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    featured = models.BooleanField(null=True)
    
    def __str__(self):
        """Format to show in admin panel"""
        return self.title + ' | Author: ' + str(self.author)
    
    def get_absolute_url(self):
        """Redirects me to the post-detail page after i created a post."""
        return reverse('main:post-detail', args=[str(self.slug)])
    