from django.db import models
from tinymce import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    description = HTMLField('Content', blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    prevNodeTitle = models.CharField(max_length=50, blank=True)
    nextNodeTitle = models.CharField(max_length=50, blank=True)
    prevNode = models.SlugField(blank=True)
    nextNode = models.SlugField(blank=True)
    tagString = models.CharField(max_length=100,default='')
    # add in thumbnail later
    # add in author later

    def category(self):
        return self.tagString.split(",")

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + "..."

# python manage.py makemigrations
# python manage.py migrate
