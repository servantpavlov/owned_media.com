from django.db import models
from django.utils import timezone

class BookCategory(models.Model):
    category = models.CharField(verbose_name="Category", max_length=10)

    def __str__(self):
        return self.category

class BookAuthor(models.Model):
    author = models.CharField(verbose_name="Author", max_length=20)

    def __str__(self):
        return self.author

class User(models.Model):
    user = models.CharField(verbose_name="User", max_length=20)
    
    def __str__(self):
        return self.user

class BookArticle(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    published_at = models.DateField(verbose_name="Published_at", blank=True)
    category = models.ForeignKey(BookCategory, verbose_name="Category", on_delete=models.PROTECT)
    author = models.ForeignKey(BookAuthor, verbose_name="author", on_delete=models.PROTECT, blank=True)
    summary = models.CharField(verbose_name="Summary", max_length=100, blank=True)
    cover = models.ImageField(verbose_name="Cover", upload_to="img/", blank=True)
    detail = models.TextField(verbose_name="Detail", blank=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name="Created_at", default=timezone.now)

    def __str__(self):
        return f"{self.title}-{self.author}"