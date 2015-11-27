from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

VISIBILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),  
)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    synopsis = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[self.id])

class Review(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

    def __unicode__(self):
        return self.text

class Vote(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie, blank=True, null=True)
    review = models.ForeignKey(Review, blank=True, null=True)

    def __unicode__(self):
        return "%s upvoted" % (self.user.username)