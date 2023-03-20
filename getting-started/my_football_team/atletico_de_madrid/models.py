from django.db import models

# Create your models here.

class TeamCategory(models.Model):
    team_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Players(models.Model):
    team = models.ForeignKey(TeamCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    intake_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
