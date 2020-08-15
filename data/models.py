from django.db import models

# Create your models here.


class BookModel(models.Model):

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)
