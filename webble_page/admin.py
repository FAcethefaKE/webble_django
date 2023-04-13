from django.contrib import admin
from .models import Author, Book, ReadingProgress, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'get_genres')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'country')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(ReadingProgress)
admin.site.register(Genre)
