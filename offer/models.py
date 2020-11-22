from time import time
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.contrib.auth.models import User

class UsersRatedRecord(models.Model):
    user_pk = models.IntegerField()
    rating  = models.IntegerField()
    
    def __str__(self):
        username = str(User.objects.get(pk=self.user_pk))
        return 'Rating Record< User: ' + username + ', Rating: ' + str(self.rating) + ' >'



def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Offer(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.TextField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=150, default="https://i.imgur.com/8gzzetz.jpg")
    rating = models.IntegerField(default=0)
    ACTIVE = "ac"
    INPROC = "ip"
    ARCHIVE = "ar"

    OFTYPE =[
    (ACTIVE, "active"),
    (INPROC, "in_the_process"),
    (ARCHIVE, "archive")
    ]

    oftype = models.CharField(
        max_length=2,
        choices=OFTYPE,
        default=ACTIVE,
    )

    users_rated = models.ManyToManyField(UsersRatedRecord, blank=True)

    def has_user_rated(self, user): # Return an user rate. None if not valid  
        record = self.users_rated.filter(user_pk=user.pk)
        if record.count() == 0:
            return None
        return record[0].rating 
    
    def delete_user_rated(self, user):
        record = self.users_rated.filter(user_pk=user.pk)
        if record.count() == 0:
            return
        record[0].delete()
    
    def add_user_rated(self, user, rating):
        return self.users_rated.create(user_pk=user.pk, rating=rating)

        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('offer_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        offer_name = f'{self.title}'
        return offer_name

    class Meta:
        ordering = ['-rating']



