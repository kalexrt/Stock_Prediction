from django.db import models

# Create your models here.
class TeamMember(models.Model):
    membername = models.CharField(max_length=20)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')