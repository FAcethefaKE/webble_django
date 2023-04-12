from django.contrib import admin

from .models import User, Author, Book, ReadingProgress

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(ReadingProgress)
