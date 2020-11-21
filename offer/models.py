from time import time
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# автоматическое создание уникального слага
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

# класс Предложение
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
