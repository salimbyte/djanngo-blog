from django.db import models
from accounts.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.CharField(max_length=500, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    is_edited = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog_images')


    def __str__(self) -> str:
        return f'{self.title}'

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.body}'
