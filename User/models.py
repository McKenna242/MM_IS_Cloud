from django.db import models
from django.conf import settings
# Create your models here.

class Member(models.Model):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    groups = models.ForeignKey('User.Group', on_delete=models.CASCADE, null = 'true')
    invited = models.BooleanField(default = False)
    accepted = models.BooleanField(default = False)

class Group(models.Model):
    groupName = models.CharField(max_length=50, default='GROUPNAME')
    groupCreator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    #members = models.ForeignKey('User.Member', on_delete=models.CASCADE, null = 'true')

    
    
#make make member from groupcreator? ? 