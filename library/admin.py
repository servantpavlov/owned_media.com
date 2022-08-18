from django.contrib import admin
from .models import BookCategory, BookAuthor, BookArticle, User

admin.site.register(BookCategory)
admin.site.register(BookAuthor)
admin.site.register(BookArticle)
admin.site.register(User)
