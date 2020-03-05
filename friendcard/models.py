from django.db import models
from django.utils import timezone

# Create your models here.
class FriendCard(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField('date created')
    nickname = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    home = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField(help_text="Write the content of your bio here.")

    def __str__(self):
        return self.name

    def created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
