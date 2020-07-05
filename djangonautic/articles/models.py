from django.db import models
from tinymce import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=100)
    title_ko = models.CharField(max_length=100,default='')
    slug = models.SlugField()
    body = models.TextField(default='')
    body_ko = models.TextField(default='')
    description = HTMLField('Content', blank=True)
    description_ko = HTMLField('Content_ko', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    prevNode = models.SlugField(blank=True)
    nextNode = models.SlugField(blank=True)
    tagString = models.CharField(max_length=100,default='')
    is_ready = models.BooleanField(default=False)
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
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments',default='')
    name = models.CharField(max_length=80)
    body = models.TextField(default='')
    date_comment = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_comment']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)