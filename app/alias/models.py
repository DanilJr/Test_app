from django.db import models
from django.urls import reverse
from datetime import datetime, timezone, timedelta


class Book(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=25, primary_key=True, unique=True)
    author = models.CharField(max_length=250)
    was_buplished = models.DateField()


    def get_absolute_url(self):
        return reverse('', kwargs={'book_slug': self.slug})

    class Meta:
        pass


class Alias(models.Model):
    alias = models.CharField(max_length=250, unique=True)
    target = models.ForeignKey(Book, on_delete=models.PROTECT)
    start = models.DateTimeField(default=datetime.now())
    end = models.DateTimeField(default=datetime.now()+timedelta(days=10))


    def get_absolute_url(self):
        return reverse('', kwargs={'book_slug': self.slug})


    class Meta:
        pass
