from django.db import models, migrations
# from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed
from member.models import Person

# Create your models here.

class Group(models.Model):
    
    Name = models.CharField(max_length=150)
    About = models.CharField(max_length=1000)
    Media = models.ImageField(upload_to='uploads/',default="")
    Username = models.ForeignKey(Person, on_delete=models.CASCADE)


    def save(self):
        # group = self
        super().save()
        super().save(using='farming')
        # return group
        return self.id
    
    def deleteRecordFarming(self):
        super().delete(using='farming')
        
    def deleteRecordIgrow(self):
        super().delete()
    
    class Meta:
        db_table = 'group'


class GroupMembership(models.Model):
    
    GroupName = models.ForeignKey(Group, on_delete=models.CASCADE)
    GroupMember = models.ForeignKey(Person, on_delete=models.CASCADE)
    # joined_on = models.DateTimeField(default=datetime.now, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self):
        super().save()
        super().save(using='farming')

    
    class Meta:
        
        unique_together = [['GroupName', 'GroupMember']]


class GroupSoilTag(models.Model):

    class Meta:
        db_table = 'GroupSoilTag'

    SoilTagGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    soilTag = models.CharField(max_length=150)

    def save(self):
        super().save()
        super().save(using='farming')
    
    def deleteRecordFarming(self):
        super().delete(using='farming')
        
    def deleteRecordIgrow(self):
        super().delete()

    class Meta:
        unique_together = [['SoilTagGroup', 'soilTag' ]]


class GroupPlantTag(models.Model):

    class Meta:
        db_table = 'PlantTag'

    PlantTagGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    plantTag = models.CharField(max_length=150)

    def save(self):
        super().save()
        super().save(using='farming')
    
    def deleteRecordFarming(self):
        super().delete(using='farming')
        
    def deleteRecordIgrow(self):
        super().delete()

    class Meta:
        unique_together = [['PlantTagGroup', 'plantTag' ]]

