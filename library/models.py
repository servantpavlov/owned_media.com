from django.db import models
from django.utils import timezone

class BookCategory(models.Model):
    category = models.CharField(verbose_name="Category", max_length=10)

class BookAuthor(models.Model):
    author = models.CharField(verbose_name="Author", max_length=20)

"""まだマイグレーションしない
class User(models.Model):
    user = models.TextField(verbose_name="User", max_length=20)
"""

class BookImage(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return f"{self.id}:{self.name}"

"""まだマイグレーションしない
class BooKArticle(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    published_at = models.DateField(verbose_name="Published_at")
    category = models.ForeignKey(BookCategory, verbose_name="Category", on_delete=models.PROTECT)
    author = models.ForeignKey(BookAuthor, verbose_name="author", on_delete=models.PROTECT)
    summary = models.CharField(verbose_name="Summary", max_length=100)
    cover = models.ForeignKey(BookImage, verbose_name="Cover", on_delete=models.PROTECT)
    detail = models.TextField(verbose_name="Detail")
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name="Created_at", default=timezone.now())
"""