from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
  url = models.URLField(unique=True)

  def __str__(self):
    return self.url
      
  class Admin:
    pass

class Bookmark(models.Model):
  title = models.CharField(maxlength=200)
  user = models.ForeignKey(User)
  link = models.ForeignKey(Link)

  def __str__(self):
    return '%s, %s' % (self.user.username, self.link.url)
  
  def get_absolute_url(self):
    return self.link.url
      
  class Admin:
    list_display = ('title', 'link','user')
    list_filter = ('user', )
    ordering = ('title', )
    search_fields = ('title', )


class Tag(models.Model):
  name = models.CharField(maxlength=64, unique=True)
  bookmarks = models.ManyToManyField(Bookmark)

  def __str__(self):
    return self.name
    
  class Admin:
    pass


class SharedBookmark(models.Model):
  bookmark = models.ForeignKey(Bookmark, unique=True)
  date = models.DateTimeField(auto_now_add=True)
  votes = models.IntegerField(default=1)
  users_voted = models.ManyToManyField(User)

  def __str__(self):
    return '%s, %s' % self.bookmark, self.votes
    
  class Admin:
    pass
