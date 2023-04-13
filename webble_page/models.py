from django.utils.timezone import now
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=False)
    surname = models.CharField(max_length=80, blank=False)
    country = models.CharField(max_length=80, blank=False)
    birthday = models.DateField(default=now)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publishing_date = models.DateField()
    genre = models.CharField(max_length=50)

    def get_authors(self):
        return ', '.join(str(author) for author in self.authors.all())

    def get_absolute_url(self):
        return reverse('book', args=[str(self.id)])

    def __str__(self):
        return f'{self.title} - {self.genre}'


class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    last_page_read = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.book.title} ({self.last_page_read})'
