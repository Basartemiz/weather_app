from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_query=models.CharField(max_length=255)
    class Meta:
        unique_together = ('user', 'user_query')  # no duplicate query