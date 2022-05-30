from django.db import models


class Digest (models.Model):
    title = models.CharField(max_length=100)
    digest_text = models.TextField()

    def __str__(self):
        return self.title


class Review (models.Model):
    title = models.CharField(max_length=100)
    review_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
