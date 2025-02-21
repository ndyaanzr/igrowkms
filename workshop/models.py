from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed
from member.models import Person, SoilTag, PlantTag

# Create your models here.

class Workshop(models.Model):
    class Meta:
        db_table = 'Workshop'
    ProgrammeName = models.CharField(max_length=150,default="")
    Speaker=models.CharField(max_length=150, default="")
    Description=models.CharField(max_length=150,default="")
    Date = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    # Session = models.CharField(max_length=150)
    # nanti next version or bila share version ni, sila remove null=true okay
    PIC = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def save(self):
        super().save()
        super().save(using='farming')
        return self.id

    def deleteRecordFarming(self):
        super().delete(using='farming')
        
    def deleteRecordIgrow(self):
        super().delete()
        


class Booking(models.Model):
    class Meta:
        db_table = 'Booking'
    # Name = models.CharField(max_length=150)
    ProgrammeName = models.CharField(max_length=150,default="")
    Date = models.DateField()
    # Session = models.CharField(max_length=150)
    # nanti next version or bila share version ni, sila remove null=true okay
    BookWorkshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, null=True)
    Participant = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def save(self):
        super().save()
        super().save(using='farming')
    
    class Meta:
        
        unique_together = [['BookWorkshop', 'Participant']]


class WorkshopSoilTagging(models.Model):

    WorkshopSoilTag = models.ForeignKey(Workshop, related_name="soilTagging", on_delete=models.CASCADE)    
    soilTag = models.ForeignKey(SoilTag, on_delete=models.CASCADE)
   
    class Meta:  
        unique_together = [['WorkshopSoilTag', 'soilTag']]

    def save(self):
        super().save()
        super().save(using='farming')
   
    def deleteRecordFarming(self):
        super().delete(using='farming')
        
    def deleteRecordIgrow(self):
        super().delete()


class WorkshopPlantTagging(models.Model):

    WorkshopPlantTag = models.ForeignKey(Workshop, related_name="plantTagging", on_delete=models.CASCADE)    
    plantTag = models.ForeignKey(PlantTag, on_delete=models.CASCADE)
   
    class Meta:  
        unique_together = [['WorkshopPlantTag', 'plantTag']]

    def save(self):
        super().save()
        super().save(using='farming')
   
    def deleteRecordFarming(self):
        super().delete(using='farming')
        
    def deleteRecordIgrow(self):
        super().delete()

