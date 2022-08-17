from django.contrib import admin
from .models import BookCategory, BookAuthor, BookImage

admin.site.register(BookCategory)
admin.site.register(BookAuthor)
admin.site.register(BookImage)
