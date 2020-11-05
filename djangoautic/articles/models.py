from django.db import models
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='defult.jpg', blank = True)

    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

  #  def save(self,*args, **kwargs):
   #     if not self.slug:
    #        self.slug = slugify(self.title)
    #   super(Article, self).save(self,*args, **kwargs)