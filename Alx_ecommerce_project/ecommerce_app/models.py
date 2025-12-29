from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model represents each product post.
    - product: name of the product
    - catagory: catagory of product
    - post_date: automatically records date/time when created
    - marchant: foreign key referencing Django's built-in User model
    """

    productname = models.CharField(max_length=200)
    catagory = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    marchant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.product
