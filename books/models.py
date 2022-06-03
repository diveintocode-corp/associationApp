from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f'{self.title}, {self.content}'
