from django.contrib import admin
from .models import User, Author, Book, ReadingProgress


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'genre')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'title')


admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(ReadingProgress)
